import os
import shutil
def copy_images(backup_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # You can add any type of files you want by editing line number 15
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif','mp4','mp3')):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_file_path, source_folder)
                destination_file_path = os.path.join(destination_folder, relative_path)
                os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
                shutil.copyfile(source_file_path, destination_file_path)
                print(f"Copied: {file}")
if __name__ == "__main__":
    source_folder = input("Folder name : ")
    destination_folder = input('Output Folder name : ')
    copy_images(source_folder, destination_folder)
