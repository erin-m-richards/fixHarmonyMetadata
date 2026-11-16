# fixHarmonyMetadata
When using 'Write Archive' to export images from the Revvity Opera Phenix and Harmony 5.2/5.3, TIFs export with incorrect XY pixel size metadata. This issue is not seen in the Harmony 5.2/5.3 software, but it can be seen in other image analysis programs like ImageJ/FIJI, Imaris, and Aivia.

<img width="5100" height="3965" alt="261116_Harmony_metadata_issues" src="https://github.com/user-attachments/assets/cae4bc5d-7dfa-417c-9a12-228205897430" />

The correct metadata is in the associated index.xml file for each Measurement. 

  ⌊__ hs\
    ⌊__ folder named with GUID\
      ⌊__ images\
        ⌊__ folder for each well\
        ⌊__ image.index
        ⌊__ index.xml (which includes the correct metadata)
      ⌊__ index\
      ⌊__ ...

This package is a Python script to fix the internal metadata for each exported TIF to match that of the index.xml file. Correcting the internal metadata does not impact the ability to use 'Read Archive' in Harmony 5.2/5.3 and still keep the correct XY pixel size. Correcting the internal metadata allows ImageJ/FIJI, Imaris, and Aivia to now properly read in XY pixel size.

______________________________________________________________________________

**Inputs:**
  - Pop-up window that asks the user to select the 'hs' Archive file that was created using 'Write Archive' to export data from Harmony 5.2/5.3.

**Outputs:**
  - _In place_ correction of TIF metadata (XY pixel size) for each TIF image file in each Measurement that was selected for export during the 'Write Archive' step
  - output.txt file (with the date and time in the name) with details for metadata corrections
