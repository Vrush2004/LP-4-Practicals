# Write a computer forensic application program for Recovering permanent Deleted Files and Deleted Partitions

import pytsk3
import sys

def recover_files(img_path):
    # Open the image file
    img = pytsk3.Img_Info(img_path)
    
    # Open the filesystem from the image
    fs = pytsk3.FS_Info(img)
    
    # Traverse through the filesystem to find deleted files
    recover_deleted_files(fs)

def recover_deleted_files(fs):
    # Iterate over the root directory
    root_dir = fs.open_dir(path="/")
    
    # Recursively search for deleted files
    for entry in root_dir:
        if entry.info.name.name in (b'.', b'..'):
            continue

        # Check if the entry is deleted
        if entry.info.meta and entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_REG and entry.info.meta.flags == pytsk3.TSK_FS_META_FLAG_UNALLOC:
            print(f"Recovered Deleted File: {entry.info.name.name.decode('utf-8')}")

        # If the entry is a directory, recurse into it
        if entry.info.meta and entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_DIR:
            recover_deleted_files(fs.open_dir(entry.info.name.name.decode('utf-8')))

if __name__ == "__main__":
    # Provide the path to the disk image (e.g., dd image file)
    if len(sys.argv) != 2:
        print("Usage: python recover_files.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    recover_files(image_path)