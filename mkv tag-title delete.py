import os
import subprocess

# Full path to mkvpropedit.exe
MKVPROPEDIT_PATH = r"C:\Program Files\MKVToolNix\mkvpropedit.exe"

def clean_mkv_metadata(root_folder):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".mkv"):
                file_path = os.path.join(dirpath, filename)
                print(f"Cleaning metadata: {file_path}")
                
                try:
                    subprocess.run(
                        [
                            MKVPROPEDIT_PATH, file_path,
                            "--tags", "all:",
                            "--delete-track-statistics-tags",
                            "--edit", "info",
                            "--set", "title="
                        ],
                        check=True
                    )
                except subprocess.CalledProcessError as e:
                    print(f"Error cleaning {file_path}: {e}")

if __name__ == "__main__":
    # Change this to your folder path
    target_directory = r"C:\Users\admin\Desktop\New Folder"
    
    if os.path.exists(target_directory):
        clean_mkv_metadata(target_directory)
    else:
        print(f"Directory does not exist: {target_directory}")

