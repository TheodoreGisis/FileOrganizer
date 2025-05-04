import os
import shutil
import sys

class OrganizeDirectory:
    def __init__(self):
        self.path = sys.argv[1]
        self.files = os.listdir(self.path)
        self.folders = []

    def CreateFolders(self) -> None:
        for f in self.files:
            full_path = os.path.join(self.path, f)
            if os.path.isfile(full_path) and '.' in f:
                ext = f.split('.')[-1]
                folder_path = os.path.join(self.path, ext)
                try:
                    os.makedirs(folder_path, exist_ok=True)
                    print(f"Directory '{ext}' created or already exists.")
                except Exception as e:
                    print(f"Failed to create directory '{ext}': {e}")

    def OrganizeFiles(self) -> None:
        for f in self.files:
            full_path = os.path.join(self.path, f)
            if os.path.isfile(full_path) and '.' in f:
                ext = f.split('.')[-1]
                dest_folder = os.path.join(self.path, ext)
                try:
                    shutil.move(full_path, os.path.join(dest_folder, f))
                    print(f"Moved '{f}' to '{ext}/'")
                except Exception as e:
                    print(f"Failed to move '{f}': {e}")

    def __str__(self) -> str:
        return f"The directory path is: {self.path}"

if __name__ == "__main__":
    organizer = OrganizeDirectory()
    organizer.CreateFolders()
    organizer.OrganizeFiles()
