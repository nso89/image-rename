# image-rename
Cleanup image filenames and move it to a destination

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Cleaning Up](#cleaning-up)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
1. A complete install of `Tcl` 8.6.
2. A folder labelled `Work` under your `Documents` folder.
3. A copy of your base cover letter and resume in one file, saved as a `.odt` file in your `Work` folder.
#### <a name="setup"></a>Setup
1. Download and extract the contents of `job-workflow.zip` into your `Work` folder.

**Example**:
```
C:\Users\nso89\Documents\Work\run.bat
C:\Users\nso89\Documents\Work\automate-workflow.tcl
C:\Users\nso89\Documents\Work\cover_letter_resume_base.odt
```
#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to your `Work` folder.

**Example**:
```batch
C:\Users\nso89>cd Documents\Work
```

2. Run the `run.bat` script.

**Example**:
```batch
C:\Users\nso89\Documents\Work>start run.bat
```

3. The `run.bat` script starts the `automate-workflow.tcl` script, and asks you for the `Company Name` and `Position`.

**Example**:
```batch
Running C:\Users\nso89\Documents\Work\automate-workflow.tcl
Company Name: Microsoft
Position: Software Engineer
```

4. The script creates 3 folders, the `Company Name` as the parent, the `Position` as the subfolder, and another subfolder labelled with current date and time. It copies the base cover letter and resume to the new folder, and exits. 

```batch
Creating Microsoft/Software Engineer/20201118-124252 folder.
Copying cover_letter_resume.odt to Microsoft/Software Engineer/20201118-124252
C:\Users\nso89\Documents\Work\automate-workflow.tcl exiting.
Press any key to continue . . .
```
5. Pushing any key to continue will open the file in your default word processor. 

**Example**:
```batch
Starting Microsoft/Software Engineer/20201118-124252/cover_letter_resume.odt
```

#### <a name="cleaning-up"></a>Cleaning Up
1. You'll notice that in your `Work` folder, a `job.txt` appeared. The `automate-workflow.tcl` script wrote the file path to your newly created folders to a text file so the `run.bat` can open your cover letter ane resume. You don't have to delete this file manually, the `run.bat` can do it for you.

**Example**:
```batch
C:\Users\nso89\Documents\Work\job.txt, Delete (Y/N)? y
```
#### <a name="configuration"></a>Configuration

**Changing the filename**
1. Open the `automate-workflow.tcl` in any text editor, locate the `coverletterresume` variable, and change the filename. **Do not** change anything else.

**Example**:
```Tcl
# Path to our cover letter and resume.
set coverletterresume "cover_letter_resume.odt" # < -- Change this, but leave the quotes.
```
2. Save and close the editor.
