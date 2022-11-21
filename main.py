from pathlib import Path
import shutil
from typing import List


SOURCE_REPOSITORY = Path.home().joinpath("Repository")
DESTINATION_REPOSITORY = Path("R:\Pictures")


def get_file_count(folder: Path) -> int:
    """
    Returns the number of files in a 
    folder.

    Args:
        folder: Path - the folder 
        we're looping over.

    Return:
        file_count: the number of files 
        in the folder.
    """
    file_count : int = 0
    for file in folder.iterdir():
        if file.is_file():
            file_count += 1
    return file_count


def is_dir(item: Path) -> bool:
    """
    Determine if the item is
    in fact a folder.

    Args:
        item: Path - The item 
        we're checking.

    Returns:
        bool - true if item is 
        a folder, false if it's 
        a file. 
    """
    return item.is_dir()


def is_file(item: Path) -> bool:
    """
    Determine if the item is
    in fact a file.

    Args:
        item: Path - The item 
        we're checking.

    Returns:
        bool - true if item 
        is a file, false if 
        it's a folder.
    """
    return item.is_file()
    

def main():

    to_delete : List[Path] = []

    try:
        
        for folder in filter(is_dir,SOURCE_REPOSITORY.iterdir()):
            destination_repository_child = DESTINATION_REPOSITORY.joinpath(folder.stem)
            destination_repository_child.mkdir(exist_ok = True)
            number_of_files = get_file_count(destination_repository_child) + 1
            
            print(f"\nSource: {folder} Destination: {destination_repository_child}")

            for index, source in enumerate(filter(is_file,folder.iterdir()), start = number_of_files):
                destination = destination_repository_child.joinpath(f"{index}{source.suffix}")
                print(f"Renaming {source.name} to {destination.name}")
                shutil.move(src = source, dst = destination)
            
            to_delete.append(folder)

        print("\nCleaning Up:")
        for folder in to_delete:
            print(f"Removing: {folder.stem}")
            folder.rmdir()

    except (FileNotFoundError, OSError) as e:
        print(e)

if __name__ == "__main__":
    main()
