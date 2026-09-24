"""
Sorts all files inside Downloads folder into subfolders for related filetypes.
No arguments needed, assumes Windows Host.
"""

import shutil
from pathlib import Path

extension_type_mappings = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".pdf": "PDF Files",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".xls": "Excel Files",
    ".xlsx": "Excel Files",
    ".ppt": "PowerPoint Files",
    ".pptx": "PowerPoint Files",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".exe": "Executables",
    ".msi": "Executables",
    ".txt": "Text Files",
    ".csv": "CSV Files",
    ".py": "Scripts",
    ".js": "Scripts",
}

# maps which file to sort to based on extension type
def folder_to_map_to(extension:str) -> str:
    if extension.lower() in extension_type_mappings:
        return extension_type_mappings[extension]

    return "No Extension"

# If dest_folder/filename already exists, append (1), (2), etc.
#    until a free filename is found
def get_unique_destination(dest_folder: Path, filename: str) -> Path:
    dest_path = dest_folder / filename
    if not dest_path.exists():
        return dest_path

    stem = dest_path.stem
    suffix = dest_path.suffix
    counter = 1
    while True:
        candidate = dest_folder / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize(downloads_folder: Path) -> None:
    if not downloads_folder.exists:
        print(f"Error: folder not found for {downloads_folder}")
        return
    
    for file in list(downloads_folder.iterdir()):
        if file.is_dir(): 
            # ignore directories, we only want to organize the files
            continue
        
        if file.suffix.lower() in (".crdownload", ".tmp", ".part"):
            # ignore partials
            continue 
            
        extension_str = file.suffix.lower()
        folder_to_sort_to = folder_to_map_to(extension_str)
        
        destination = downloads_folder / folder_to_sort_to
        destination.mkdir(exist_ok=True)
        
        dest_path = get_unique_destination(destination, file.name)
        
        try:
            shutil.move(str(file), str(dest_path))
            print(f"Moved {file.name}")
        except (PermissionError, OSError) as e:
            print(f"Skipped (in use or inaccessible): {file.name}, ({e})")
            
        
    print("Script Terminated")
    return


def main():
    print("Organizing...")
    downloads_path = Path.home() / "Downloads"
    
    organize(downloads_path)


if __name__ == "__main__":
    main()
    





