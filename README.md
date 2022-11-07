# image-rename
Rename files and move it to a destination

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Cleaning Up](#cleaning-up)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
1. A completed install of `Python 3.x`.
2. Under your `USERPROFILE`, a folder named `Repository` containing all the subfolders with images we want to rename.

**Example**:
```
C:\Users\nso89\Repository\Kirk
    - James_T._Kirk,_alternate_reality.webp
    - star-trek-strange-new-worlds-kirk-paul-wesley.webp

C:\Users\nso89\Repository\Spock
    - 8b10a9280bd46b8874af9b5cadec91d5.webp 
    - Spock_2254.webp
```
#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract the `image-rename-cleanup.zip`.

**Example**:
```batch
C:\Users\nso89\image-rename-cleanup-main
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `image-rename-cleanup-main` folder.

**Example**:
```batch
C:\Users\nso89>cd image-rename-cleanup-main
```

2. Start the `main.py` script.
```batch
C:\Users\nso89\image-rename-cleanup-main>python main.py
```

3. The script creates the necessary destination folders if they don't already exist, renames the images, and moves them to the destination folders.

**Example**:
```
Source : C:\Users\nso89\Repository\Kirk Destination: R:\Pictures\Kirk
Renaming James_T._Kirk,_alternate_reality.webp to 1.webp
Renaming star-trek-strange-new-worlds-kirk-paul-wesley.png to 2.png

Source : C:\Users\nso89\Repository\Spock Destination: R:\Pictures\Spock
Renaming 8b10a9280bd46b8874af9b5cadec91d5.webp to 1.webp
Renaming Spock_2254.webp to 2.webp
```
#### <a name="cleaning-up"></a>Cleaning Up
1. If the subfolders are empty, they will be removed.

**Example**:
```batch
Cleaning Up:
Removing: Kirk
Removing: Spock
```

#### <a name="configuration"></a>Configuration
If you need to change the `source` or `destination` folder:
1. Open the `main.py` script in any text editor.
2. Locate the `SOURCE_REPOSITORY` and `DESTINATION_REPOSITORY` variables.

**Example**:
```python
SOURCE_REPOSITORY = Path.home().joinpath("Repository")
DESTINATION_REPOSITORY = Path("R:\Pictures")
```
3. When you finish changing the variables, save and close the editor.
