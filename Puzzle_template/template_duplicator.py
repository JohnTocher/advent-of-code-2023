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

    # Copy source code and markdown
    source_ext = [".py", ".md", ".txt"]
    source_files = (
        f_name
        for f_name in Path(source_folder).iterdir()
        if f_name.suffix in source_ext
    )
    # This format was the result of black auto-linting, I think this actually works
    # quite well for a moderately complex list comprehension, but it might be one
    # worth breaking out into it's own functoin for future use

    for source_file in source_files:
        # print(f"Testing: {source_file}")
        if "NN" in source_file.name:
            new_name = source_file.name.replace("NN", f"{folder_number:02}")
            dest_file = target_folder / new_name
            print(f"Going to re-create: {source_file}")
            print(f"Output name will be: {dest_file}")
            with open(source_file, "r") as input_file:
                with open(dest_file, "w") as output_file:
                    for each_line in input_file:
                        if "NN" in each_line:
                            if "adventofcode.com" in each_line:
                                new_line = each_line.replace("NN", f"{folder_number}")
                            else:
                                new_line = each_line.replace(
                                    "NN", f"{folder_number:02}"
                                )
                        else:
                            new_line = each_line
                        output_file.write(new_line)

    return False


if __name__ == "__main__":
    create_ok = create_puzzle_folders(folder_number=5)
