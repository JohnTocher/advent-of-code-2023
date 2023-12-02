""" Puzzle template duplicator

    This code is meant to be run on my local repository, where it copies
    template files from my templete directory to a folder for a specific
    days puzzle, and renames everything appropriately,as well as editng
    each file to replace the internal references to the puzzle numbers.

    It's just to reduce the effort in setting up a puzzle subfolder, it
    has no bearing on any solutions otherwise

    Assumes that it will be run from the template folder, and that the 
    daily puzzle folders are one folder up, and then named after the day
    number
"""

from pathlib import Path

INPUT_FOLDER = "Puzzle_template"


def create_puzzle_folders(folder_number=1):
    """Main working function"""

    # Check if target folder exists
    source_folder = Path(__file__).parent
    target_folder = Path(__file__).parent.parent / f"Puzzle_{folder_number:02}"

    if target_folder.is_dir():
        print(f"Folder: {target_folder} already exists!")
        return False

    print(f"Source folder to be copied is {source_folder}")
    print(f"Target folder to be created is {target_folder}")
    target_folder.mkdir(exist_ok=False)

    return False


if __name__ == "__main__":
    create_ok = create_puzzle_folders(folder_number=3)
