from pathlib import Path
import shutil
from typing import List

def get_file_count(folder: Path) -> int:
    file_count : int = 0
    for file in folder.iterdir():
        if file.is_file():
            file_count += 1
    return file_count

def is_dir(item: Path) -> bool:
    return item.is_dir()

def is_file(item: Path) -> bool:
    return item.is_file()

def main():

    SOURCE_REPOSITORY = Path.home().joinpath("Repository")
    DESTINATION_REPOSITORY = Path("R:\Pictures")

    to_delete : List[Path] = []

    try:
        
        for folder in filter(is_dir,SOURCE_REPOSITORY.iterdir()):
            destination_repository_child = DESTINATION_REPOSITORY.joinpath(folder.stem)
            destination_repository_child.mkdir(exist_ok=True)
            number_of_files = get_file_count(destination_repository_child) + 1
            
            for index, source in enumerate(filter(is_file,folder.iterdir()), start=number_of_files):
                destination = destination_repository_child.joinpath(f"{index}{source.suffix}")
                print(f"Source: {source} Destination: {destination}")
                shutil.move(src=source,dst=destination)
            
            to_delete.append(folder)

        for folder in to_delete:
            folder.rmdir()

    except (FileNotFoundError,OSError) as e:
        print(e)

if __name__ == "__main__":
    main()
