import os
import subprocess
import shutil

# Define paths
input_folder = "/input/benign_exe/test/"  # Folder containing files to be packed
output_folder = "/output/benign_exe/packed_files/"  # Base folder for packed files
packers = {
    "UPX": "upx",
    "UPX LZMA": "upx_lzma"
    #"PyInstaller": "pyinstaller",
    #"Nuitka": "nuitka"
}

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

def pack_with_upx(file_path, output_dir):
    packed_file_path = os.path.join(output_dir, os.path.basename(file_path))
    shutil.copy(file_path, packed_file_path)  # Create a copy for packing
    subprocess.run(["upx", "--force", "-9", packed_file_path], cwd=output_dir)

def pack_with_upx_lzma(file_path, output_dir):
    packed_file_path = os.path.join(output_dir, os.path.basename(file_path))
    shutil.copy(file_path, packed_file_path)  # Create a copy for packing
    subprocess.run(["upx", "--force", "--best", "--lzma", packed_file_path], cwd=output_dir)

def pack_with_pyinstaller(file_path, output_dir):
    script_path = os.path.abspath(file_path)
    subprocess.run(["pyinstaller", "--onefile", "--distpath", output_dir, script_path])

def pack_with_nuitka(file_path, output_dir):
    script_path = os.path.abspath(file_path)
    subprocess.run(["nuitka", "--onefile", "--static-libpython=no", f"--output-dir={output_dir}", script_path])

def pack_with_mpress(file_path, output_dir):
    script_path = os.path.abspath(file_path)
    subprocess.run(["wine mpress", "--onefile", "--static-libpython=no", f"--output-dir={output_dir}", script_path])

packer_functions = {
    "UPX": pack_with_upx,
    "UPX LZMA": pack_with_upx_lzma,
    "PyInstaller": pack_with_pyinstaller,
    "Nuitka": pack_with_nuitka
}

# Process files for each packer
for packer, command in packers.items():
    print(f"Processing with {packer}...")
    packer_output_dir = os.path.join(output_folder, packer)
    os.makedirs(packer_output_dir, exist_ok=True)

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)

        if os.path.isfile(file_path):
            print(f"Packing {file} using {packer}...")
            try:
                packer_functions[packer](file_path, packer_output_dir)
            except Exception as e:
                print(f"Error packing {file} with {packer}: {e}")

print("Packing completed!")
