from pathlib import Path
import shutil
from typing import List

def get_file_count(folder: Path) -> int:
    """
    Using a for loop and Path.is_file(),
    we count all the files in a folder,
    and return it.

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

    SOURCE_REPOSITORY = Path.home().joinpath("Repository")
    DESTINATION_REPOSITORY = Path("R:\Pictures")

    to_delete : List[Path] = []

    try:
        
        # Using filder and is_dir(), we get only the folders as it's being determined.
        for folder in filter(is_dir,SOURCE_REPOSITORY.iterdir()):
            destination_repository_child = DESTINATION_REPOSITORY.joinpath(folder.stem)
            # Create the directory if it doesn't exist, if it does, no exception 
            # will be raised.
            destination_repository_child.mkdir(exist_ok = True)
            # Pick up the count and add 1 to continue.
            number_of_files = get_file_count(destination_repository_child) + 1
            
             # Using filder and is_file(), we get only the files as it's being determined.
            for index, source in enumerate(filter(is_file,folder.iterdir()), start = number_of_files):
                destination = destination_repository_child.joinpath(f"{index}{source.suffix}")
                print(f"Source: {source} Destination: {destination}")
                shutil.move(src = source, dst = destination)
            
            to_delete.append(folder)

        for folder in to_delete:
            folder.rmdir()

    except (FileNotFoundError,OSError) as e:
        print(e)

if __name__ == "__main__":
    main()
