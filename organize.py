import os
from pathlib import Path

# Change working directly (temporary)
os.chdir('C:\\Users\\RAM\\Desktop\\Python\\Organize\\Ex_Files_Python_Automation\\Exercise Files\\OrganizeMe')

# Directory Dictionary
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# Test an example
def pickdirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'
#print(pickdirectory('.mp3'))

# Organize each file in a directory
def organizedirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filepath = Path(item)
        filetype = filepath.suffix.lower()
        directory = pickdirectory(filetype)
        dirpath = Path(directory)
        if dirpath.is_dir() != True:
            dirpath.mkdir()
        filepath.rename(dirpath.joinpath(filepath))

organizedirectory()