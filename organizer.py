import os
import shutil

folder_path = "C:/Users/alber/Downloads"

# File type categories
file_types = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_full_path = os.path.join(folder_path, folder)
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(file)

    moved = False

    for folder, extensions in file_types.items():
        if extension.lower() in extensions:
            destination = os.path.join(folder_path, folder, file)
            shutil.move(file_path, destination)
            print(f"Moved {file} → {folder}")
            moved = True
            break

    # If file type not recognized
    if not moved:
        other_folder = os.path.join(folder_path, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        destination = os.path.join(other_folder, file)
        shutil.move(file_path, destination)
        print(f"Moved {file} → Others")