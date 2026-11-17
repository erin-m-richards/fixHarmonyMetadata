# fixHarmonyMetadata
When using 'Write Archive' to export images from the Revvity Opera Phenix and Harmony 5.2/5.3, TIFs export with incorrect XY pixel size metadata. This issue is not seen in the Harmony 5.2/5.3 software, but it can be seen in other image analysis programs like ImageJ/FIJI, Imaris, and Aivia.

<img width="5100" height="3965" alt="261116_Harmony_metadata_issues" src="https://github.com/user-attachments/assets/cae4bc5d-7dfa-417c-9a12-228205897430" />

The correct metadata is in the associated index.xml file for each Measurement.

  hs\ → folder named for GUID\ → images\ → index.xml with metadata

This package is a Python script to fix the internal metadata for each exported TIF to match that of the index.xml file. Correcting the internal metadata does not impact the ability to use 'Read Archive' in Harmony 5.2/5.3 and still keep the correct XY pixel size. Correcting the internal metadata allows ImageJ/FIJI, Imaris, and Aivia to now properly read in XY pixel size.

______________________________________________________________________________

## Inputs:
  - Pop-up window that asks the user to select the 'hs' Archive file that was created using 'Write Archive' to export data from Harmony 5.2/5.3.

## Outputs:
  - _In place_ correction of TIF metadata (XY pixel size) for each TIF image file in each Measurement that was selected for export during the 'Write Archive' step
  - output.txt file (with the date and time in the name) with details for metadata corrections

______________________________________________________________________________

## Required packages (may work with lower, but has not been tested)
  - python 3.13 and dependencies
  - tifffile 2026.10.15 and dependencies

All packages are contained in the env.yml file.

______________________________________________________________________________

## Installation and Running instructions (.exe application)
1. (Install) Download fixHarmonyMetadata.exe or install Release App_v01 to your computer.
2. (Run) Double-click the fixHarmonyMetadata.exe application. A Terminal will open.
  - Note: It may take up to 20 seconds between the Terminal opening and the application running.
3. (Run) A pop-up window will appear asking you to select the 'hs' archive folder that contains your exported images.
4. (Run) Any issues with folders will appear in the Terminal as a printed message. Otherwise, a printed message in the Terminal will tell you that all images were processed successfully.
5. (Run) A .txt output file is generated with the details of the run (including XY pixel size before and after the fix). The location and name of the output file is given in the Terminal as a printed message.
6. (Run) Close the Terminal by clicking on the Terminal and pressing Enter.

______________________________________________________________________________

## Installation instructions (conda environment and python script)
1. (Install) Download env.yml and fixHarmonyMetadata.py or install Release Script_v01 to your computer.
2. (Install) In Terminal, create necessary conda environment with "conda env create -f full\path\to\env.yml".
3. (Run) Activate conda environment with "conda activate fixMetadata".
4. (Run) Run python script with "python full\path\to\fixHarmonyMetadata.py".
5. (Run) A pop-up window will appear asking you to select the 'hs' archive folder that contains your exported images.
6. (Run) Any issues with folders will appear in the Terminal as a printed message. Otherwise, a printed message in the Terminal will tell you that all images were processed successfully.
7. (Run) A .txt output file is generated with the details of the run (including XY pixel size before and after the fix). The location and name of the output file is given in the Terminal as a printed message.
8. (Run) Close the Terminal by clicking on the Terminal and pressing Enter.

_After you run Steps 1-3 above_, you can also turn this script into its own .exe application on your own computer with:
1. Download the PyInstaller [https://pyinstaller.org/en/stable/] package with "pip install PyInstaller".
2. Then run "pyinstaller --clean --one-file --name fixHarmonyMetadata path\to\fixHarmonyMetadata.py". It may take a while to compile.
3. After it is complete, you can simply double-click the fixHarmonyMetadata.exe file to run the program.
