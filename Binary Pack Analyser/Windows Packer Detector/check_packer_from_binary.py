import math
import csv
import json
import sys
import os
import subprocess
import hashlib

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

def calculate_sha256(fpath):
    sha256_hash = hashlib.sha256()
    with open(fpath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_packed_with_die(pe_file_path):
    """Check if a PE file is packed using Detect-It-Easy (diec)..."""
    try:
        file_sha256 = calculate_sha256(pe_file_path)
        result = subprocess.run(['diec.sh', '-j', pe_file_path], capture_output=True, text=True, check=True)
        output = json.loads(result.stdout)
        print(output)
        file_info = output.get('files', [{}])[0]
        is_packed = file_info.get('isPacked', False)
        packer_type = file_info.get('packer', 'Unknown')
        details = file_info.get('detects', [])
        detail_str = '; '.join([d.get('name', '') for d in details]) if details else 'No packing info from DiE'

        return {
            'sha256' : file_sha256,
            'file_path': pe_file_path,
            'is_packed': is_packed,
            'packer_type': packer_type if packer_type else 'Unknown',
            'details': detail_str,
            'pack_control_programme': 'Detect-It-Easy'
        }
    except subprocess.CalledProcessError as e:
        return {
            'sha256' : file_sha256,
            'file_path': pe_file_path,
            'is_packed': False,
            'packer_type': 'Error',
            'details': f"DiE execution failed: {e.stderr}",
            'pack_control_programme': 'Detect-It-Easy'
        }
    except Exception as e:
        return {
            'sha256' : file_sha256,
            'file_path': pe_file_path,
            'is_packed': False,
            'packer_type': 'Error',
            'details': str(e),
            'pack_control_programme': 'Detect-It-Easy'
        }

def save_to_csv(results, output_file):
    """Save packing analysis results to CSV."""
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['sha256', 'file_path', 'is_packed', 'packer_type', 'details', 'pack_control_programme']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def save_to_json(results, output_file):
    """Save packing analysis results to JSON."""
    with open(output_file, 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4)

def is_pe_file(filepath):
    """Check if a file is likely a PE file based on extension."""
    pe_extensions = {'.exe', '.dll', '.sys', '.ocx', '.scr'}
    return os.path.splitext(filepath.lower())[1] in pe_extensions

def process_directory(directory_path):
    """Process all PE files in the given directory."""
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a directory.")
        sys.exit(1)

    results = []
    pe_files = [f for f in os.listdir(directory_path) if is_pe_file(f)]

    if not pe_files:
        print(f"No PE files found in {directory_path}.")
        sys.exit(1)

    for pe_file in pe_files:
        pe_file_path = os.path.join(directory_path, pe_file)
        print(f"Processing: {pe_file_path}")

        # Check with Detect-It-Easy
        results.append(check_packed_with_die(pe_file_path))


    # Generate output filenames based on directory name
    dir_name = os.path.basename(os.path.normpath(directory_path))
    csv_output = os.path.join(directory_path, f"{dir_name}_packing.csv")
    json_output = os.path.join(directory_path, f"{dir_name}_packing.json")

    # Save results
    save_to_csv(results, csv_output)
    save_to_json(results, json_output)

    print(f"Packing analysis saved to {csv_output} and {json_output}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_packer_from_binary.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    process_directory(directory_path)

if __name__ == "__main__":
    main()