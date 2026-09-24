"""
Remove all files in Downloads folder ending with a particular extension type, avoids subfolders.
"""

import sys
from pathlib import Path

def main(ext:str):
    downloads_folder = Path.home() / "Downloads"
    
    for file in downloads_folder.glob(f"*.{ext}"):
        if file.is_file():
            print(f"Deleting file: {file}")
            file.unlink()

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        ext = sys.argv[1].lower()
        
        
        print(f"Using extension: {ext}")    
        main(ext)
        
    else:
        print("Extension type required in first argument") # no args   
        
        
    