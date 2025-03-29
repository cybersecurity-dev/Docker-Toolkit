import os
import sys
import json
import csv
from datetime import datetime
import lief
import math
import pandas as pd
import configparser
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil
import hashlib
import ssdeep

def calculate_entropy(data):
    """Calculate Shannon entropy of a byte sequence."""
    if not data:
        return 0.0
    entropy = 0
    for x in range(256):
        p_x = data.count(x) / len(data)
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
    return entropy

def calculate_sha256(file_path):
    """Calculate the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def calculate_ssdeep(data, file_path, section_name):
    """Calculate the SSDEEP fuzzy hash of a byte sequence."""
    try:
        return ssdeep.hash(data)
    except Exception as e:
        print(f"Error calculating SSDEEP for {file_path} section {section_name}: {str(e)}")
        return "N/A"

def calculate_file_ssdeep(file_path):
    """Calculate the SSDEEP fuzzy hash of an entire file."""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return ssdeep.hash(data)
    except Exception as e:
        print(f"Error calculating file SSDEEP for {file_path}: {str(e)}")
        return "N/A"

def is_pe_file(file_path):
    """Check if a file is a PE file by reading the MZ signature."""
    try:
        with open(file_path, "rb") as f:
            magic = f.read(2)
            return magic == b"MZ"
    except Exception:
        return False

def extract_pe_features(file_path, label, crash_folder, json_folder, config):
    """Extract features from a PE file using LIEF into a single dictionary based on config."""
    try:
        # Load extraction flags from config
        extract_header = config.getboolean('Extraction', 'extract_header')
        extract_sections = config.getboolean('Extraction', 'extract_sections')
        extract_import_table = config.getboolean('Extraction', 'extract_import_table')
        extract_import_functions = config.getboolean('Extraction', 'extract_import_functions')
        extract_export_functions = config.getboolean('Extraction', 'extract_export_functions')

        # Calculate hashes before parsing
        sha256 = calculate_sha256(file_path)
        ssdeep_hash = calculate_file_ssdeep(file_path)
        # Parse the PE file with LIEF
        pe = lief.parse(file_path)
        if not pe or not isinstance(pe, lief.PE.Binary):
            raise ValueError("Not a valid PE file")
#---------------------------------------------------------------------------------------------------------
        # Base feature dictionary with label
        features = {
            "file_path": file_path,
            "sha256": sha256,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ssdeep": ssdeep_hash,
            "label": label  # 0 for benign, 1 for malware
        }
#---------------------------------------------------------------------------------------------------------
        # Extract header information
        if extract_header:
            features["machine"] = hex(pe.header.machine.value)
            features["number_of_sections"] = len(pe.sections)
            features["time_date_stamp"] = pe.header.time_date_stamps
            features["size_of_optional_header"] = pe.header.sizeof_optional_header
            # Check if optional_header exists before accessing it
            if hasattr(pe, 'optional_header') and pe.optional_header is not None:
                features["image_base"] = hex(pe.optional_header.imagebase)
                features["size_of_image"] = pe.optional_header.sizeof_image
            else:
                print(f"Warning: No optional header found for {file_path}. Setting defaults.")
                features["image_base"] = "0x0"
                features["size_of_image"] = 0
#---------------------------------------------------------------------------------------------------------
        # Extract imports (table and/or functions)
        if extract_import_table or extract_import_functions:
            for imp in pe.imports:
                library_name = imp.name
                if extract_import_table:
                    features[library_name] = 1  # Mark DLL presence
                if extract_import_functions:
                    for entry in imp.entries:
                        func_name = entry.name if entry.name else f"Ordinal_{entry.ordinal}"
                        features[f"{library_name}_{func_name}"] = 1  # Mark DLL-function pair
#---------------------------------------------------------------------------------------------------------
        # Extract sections
        if extract_sections:
            for section in pe.sections:
                section_name = section.name.strip('\x00')
                features[section_name] = 1  
                section_data = bytes(section.content)  # Convert list to bytes
                entropy = calculate_entropy(section_data)
                section_ssdeep = calculate_ssdeep(section_data, file_path, section_name)
                features[f"{section_name}_entropy"] = round(entropy, 2)  # Add entropy
                features[f"{section_name}_ssdeep"] = section_ssdeep  # Add SSDEEP
#---------------------------------------------------------------------------------------------------------
        # Extract exports
        if extract_export_functions and pe.has_exports:
            export_dll = os.path.basename(file_path)  # Use filename as DLL name for exports
            #features[f"export_{export_dll}"] = 1  # Mark export DLL presence
            for exp in pe.exported_functions:
                func_name = exp.name if exp.name else f"Ordinal_{exp.ordinal}"
                #features[f"export_{export_dll}_{func_name}"] = 1
                features[f"export_{func_name}"] = 1
#---------------------------------------------------------------------------------------------------------
        # Save individual JSON file for this PE file
        if not os.path.exists(json_folder):
            os.makedirs(json_folder)
        json_file = os.path.join(json_folder, f"{sha256}.json")
        with open(json_file, 'w') as jsonfile:
            json.dump(features, jsonfile, indent=4)
        print(f"Saved individual JSON: {json_file}")

        return [features]  # Return as a single-item list

    except ValueError as e:
        print(f"Parsing error for {file_path}: {str(e)}. Moving to crash folder.")
        move_to_crash_folder(file_path, crash_folder)
        return []
    except Exception as e:
        print(f"Unexpected error for {file_path}: {str(e)}. Moving to crash folder.")
        move_to_crash_folder(file_path, crash_folder)
        return []

def move_to_crash_folder(file_path, crash_folder):
    """Move a file to the crash folder if it causes a parsing error."""
    if not os.path.exists(crash_folder):
        os.makedirs(crash_folder)
    try:
        dest_path = os.path.join(crash_folder, os.path.basename(file_path))
        shutil.move(file_path, dest_path)
        print(f"Moved {file_path} to {dest_path}")
    except Exception as e:
        print(f"Failed to move {file_path} to {crash_folder}: {str(e)}")

def save_to_csv(results, output_file):
    """Save data to a CSV file using the csv module."""
    all_keys = set()
    for result in results:
        all_keys.update(result.keys())
    fieldnames = sorted(all_keys)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval=0)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def save_to_dataframe_csv(results, output_file):
    """Save data to a CSV file using Pandas DataFrame."""
    df = pd.DataFrame(results).fillna(0)
    df.to_csv(output_file, index=False)

def save_to_pickle(results, output_file):
    """Save data to a Pickle file using Pandas DataFrame."""
    df = pd.DataFrame(results).fillna(0)
    df.to_pickle(output_file)

def process_directory(config_file):
    """Process PE files from directories in the config file using multiple threads."""
    # Load configuration
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        print(f"Error: Config file {config_file} not found.")
        sys.exit(1)
    config.read(config_file)

    try:
        benign_directory = config['Settings']['benign_directory']
        malware_directory = config['Settings']['malware_directory']
        output_prefix = config['Settings']['output_prefix']
        thread_count = int(config['Settings']['thread_count'])
        crash_folder = config['Settings']['crash_folder']
        json_folder = config['Settings']['json_folder']
        extract_pe = config.getboolean('FileTypes', 'extract_pe')
    except KeyError as e:
        print(f"Error: Missing required config parameter {str(e)} in {config_file}.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid thread_count value in {config_file}: {str(e)}.")
        sys.exit(1)

    # Check directories
    if not os.path.isdir(benign_directory):
        print(f"Error: {benign_directory} is not a directory.")
        sys.exit(1)
    if not os.path.isdir(malware_directory):
        print(f"Error: {malware_directory} is not a directory.")
        sys.exit(1)

    # Collect files with labels, filtering by file type
    all_files = []
    if extract_pe:
        benign_files = [(os.path.join(benign_directory, f), 0) for f in os.listdir(benign_directory) if is_pe_file(os.path.join(benign_directory, f))]
        malware_files = [(os.path.join(malware_directory, f), 1) for f in os.listdir(malware_directory) if is_pe_file(os.path.join(malware_directory, f))]
        all_files = benign_files + malware_files

    if not all_files:
        print(f"No files matching the specified types found in {benign_directory} or {malware_directory}.")
        sys.exit(1)

    all_results = []
    # Process files using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        future_to_file = {executor.submit(extract_pe_features, file_path, label, crash_folder, json_folder, config): file_path for file_path, label in all_files}
        for future in as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                results = future.result()
                if results:
                    all_results.extend(results)
                print(f"Completed: {file_path}")
            except Exception as e:
                print(f"Thread error processing {file_path}: {str(e)}")

    if not all_results:
        print("No features extracted from any files.")
        sys.exit(1)

    # Generate output filenames
    output_dir = os.path.dirname(benign_directory)
    csv_output = os.path.join(output_dir, f"{output_prefix}_features.csv")
    df_csv_output = os.path.join(output_dir, f"{output_prefix}_features_df.csv")
    pkl_output = os.path.join(output_dir, f"{output_prefix}_features.pkl")

    # Save combined results in CSV, DataFrame CSV, and Pickle formats
    save_to_csv(all_results, csv_output)
    save_to_dataframe_csv(all_results, df_csv_output)
    save_to_pickle(all_results, pkl_output)

    print(f"Combined features saved to:")
    print(f"  - CSV: {csv_output}")
    print(f"  - DataFrame CSV: {df_csv_output}")
    print(f"  - Pickle: {pkl_output}")
    print(f"Individual JSON files saved in: {json_folder}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_pe_features_wlief.py <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    process_directory(config_file)

if __name__ == "__main__":
    main()