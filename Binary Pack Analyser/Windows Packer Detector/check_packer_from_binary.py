import math
import csv
import json
import sys
import os
import subprocess
import hashlib


import json


def parse_diec_output(output_string):
    start_index = output_string.find('{')
    end_index = output_string.rfind('}') + 1 # +1 to include the closing }

    if start_index != -1 and end_index != 0:
        json_string = output_string[start_index:end_index]
        try:
            data = json.loads(json_string)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return json.loads({})
    else:
        print("Could not find JSON in the string.")
        return json.loads({})

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
    compiler = ""
    compiler_version = ""
    sign_tool = ""
    sign_tool_version = ""
    linker_version = ""
    linker = ""
    is_packed = bool(False)
    packer_name = ""
    packer_version = ""
    try:
        file_sha256 = calculate_sha256(pe_file_path)
        result = subprocess.run(['diec.sh', '-j', pe_file_path], capture_output=True, text=True, check=True)
        output = parse_diec_output(result.stdout)
        #output = json.loads(result.stdout)
        detects = output["detects"]
        if detects:
            first_detect = detects[0]
            values = first_detect["values"]
            
            for item in values:
                if item["type"] == "Compiler":
                    compiler = item["name"]
                    #compiler_string = item["string"]
                    compiler_version = item["version"]
                elif item["type"] == "Sign tool":
                    sign_tool = item["name"]
                    #sign_tool_string = item["string"]
                    sign_tool_version = item["version"]
                    #print(f"Sign Tool: {sign_tool_name}, {sign_tool_string}, Version: {sign_tool_version}")
                elif item["type"] == "Linker":
                    linker=item["name"]
                    linker_version=item["version"]
                elif item["type"] == "Packer":
                    packer_name = item["name"]
                    packer_version = item["version"]
                    is_packed = bool(True)
                elif item["type"] == "Archive":
                    archive_name=item["name"]
                    archive_version=item["version"]                
        
      


        return {
            'sha256' : file_sha256,
            'file_path': pe_file_path,
            'is_packed': is_packed,
            'packer_name': packer_name,
            'packer_version': packer_version,
            'compiler' : compiler,
            'compiler_version' : compiler_version,
            'sign_tool' : sign_tool,
            'sign_tool_version' : sign_tool_version,
            'linker' : linker,
            'linker_version' : linker_version,
            'pack_control_programme': 'DIE'
        }
    except subprocess.CalledProcessError as e:
        return {
            'sha256' : file_sha256,
            'file_path': pe_file_path,
            'is_packed': is_packed,
            'packer_name': packer_name,
            'packer_version': packer_version,
            'compiler' : compiler,
            'compiler_version' : compiler_version,
            'sign_tool' : sign_tool,
            'sign_tool_version' : sign_tool_version,
            'linker' : linker,
            'linker_version' : linker_version,
            'pack_control_programme': 'DIE'
        }
    except Exception as e:
        return {
            'sha256' : file_sha256,
            'file_path': pe_file_path,
            'is_packed': is_packed,
            'packer_name': packer_name,
            'packer_version': packer_version,
            'compiler' : compiler,
            'compiler_version' : compiler_version,
            'sign_tool' : sign_tool,
            'sign_tool_version' : sign_tool_version,
            'linker' : linker,
            'linker_version' : linker_version,
            'pack_control_programme': 'DIE'
        }

def save_to_csv(results, output_file):
    """Save packing analysis results to CSV."""
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['sha256', 'file_path', 'is_packed', 'packer_name', 'packer_version', 'compiler', 'compiler_version', 'sign_tool', 'sign_tool_version', 'linker', 'linker_version', 'pack_control_programme']
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