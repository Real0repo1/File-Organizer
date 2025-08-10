import os
import shutil

def check_files(DOWNLOAD_PATH: str):
    for f in os.listdir(DOWNLOAD_PATH):
        file_path = os.path.join(DOWNLOAD_PATH, f)

        # Skip if it's already a folder
        if os.path.isdir(file_path):
            continue

        nm, ext = os.path.splitext(f)
        
        if ext:  # Only process files with extensions
            ext_clean = ext.lstrip(".").lower()  # Remove . and make lowercase
            folder_path = os.path.join(DOWNLOAD_PATH, ext_clean)

            # Create folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Move file to that folder
            shutil.move(file_path, os.path.join(folder_path, f))