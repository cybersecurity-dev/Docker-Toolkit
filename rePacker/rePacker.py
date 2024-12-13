import os, time
import subprocess
import shutil

packers = {
    "UPX": "upx",
    "UPX_LZMA": "upx_lzma"
    #"PyInstaller": "pyinstaller",
    #"Nuitka": "nuitka"
}

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
    "UPX_LZMA": pack_with_upx_lzma,
    "PyInstaller": pack_with_pyinstaller,
    "Nuitka": pack_with_nuitka
}

def packer_process(input_folder, output_folder):
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

def main(in_dir, out_dir):
    packer_process(in_dir, out_dir)
    
if __name__ == "__main__":
    print("[" + __file__ + "]'s last modified: %s" % time.ctime(os.path.getmtime(__file__)))
    # Define paths
    in_dir = "/input/benign_exe/test/"  # Folder containing files to be packed
    out_dir = "/output/benign_exe/packed_files/"  # Base folder for packed files
    if not os.path.exists(in_dir):
        print(f"Directory: '{in_dir}' does not exist.")
        exit()         
    print(f"\n\nBINARY Directory:\t\t{in_dir}")

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    print(f"Packed BINARY Files will save:\t{out_dir}")   
    main(in_dir, out_dir)