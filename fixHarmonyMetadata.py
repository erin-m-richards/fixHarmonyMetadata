import tkinter as tk
from tkinter import filedialog
import sys
from datetime import datetime
from tifffile import TiffFile
from os import listdir
from os.path import isdir, join, isfile
import xml.etree.ElementTree as ET

def main():
    try:
        # Allow user to specify the folder with the images.
        root = tk.Tk()
        root.withdraw()
        print("\nNote: The selection window may be hidden behind other windows.\n")
        hsFolder = filedialog.askdirectory(title="Select the 'hs' folder that contains your exported images.")

        failedList = []

        # Save stuff to a .txt file for investigation later.
        outputName = "FixHarmonyMetadata_output_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
        sys.stdout = open(join(hsFolder, outputName), "w", encoding="utf-8")

        for guidFolder in listdir(hsFolder): # For each experiment (folder named with GUID) in the export folder
            if isdir(join(hsFolder, guidFolder)): # If it is a folder...
                print(f"\nProcessing folder {guidFolder}.")

                for insideFolder in listdir(join(hsFolder, guidFolder)): # For each folder within the experiment
                    if isdir(join(hsFolder, guidFolder, insideFolder)) and insideFolder == "images": # If it is the images folder...
                        # Find the correct xy pixel resolution in the .xml metadata.
                        xmlFile = join(hsFolder, guidFolder, insideFolder, 'index.xml')
                        if isfile(xmlFile) == True: # If the index.xml file exists...
                            # Open the .xml file.
                            tree = ET.parse(xmlFile) 
                            root = tree.getroot()
                            # Build a format to get rid of the extras on each element name.
                            ns = {"h": root.tag.split("}")[0].strip("{")} 
                            # Find the ImageResolutionX line in the metadata in pixels/m.
                            res = root.find("h:Maps/h:Map/h:Entry/h:ImageResolutionX", ns) 
                            print(f"\tResolution from index.xml file: {res.text} m/pixel")
                            # Convert this value to pixels/cm for TIFF metadata.
                            resTIFF = 1 / (float(res.text)*100) 
                            # Convert to format for TIFF metadata.
                            denom = 10000
                            resTIFF_formatted = (round(resTIFF * denom), denom)

                            # Change the xy pixel resolution in the current TIFF metadata to the correct values that were found in the .xml file.
                            for imageFolder in listdir(join(hsFolder, guidFolder, insideFolder)): # For each item in the images folder
                                if isdir(join(hsFolder, guidFolder, insideFolder, imageFolder)): # If it's a folder...
                                    print(f"\t\tProcessing images in {imageFolder}.")

                                    for image in listdir(join(hsFolder,guidFolder, insideFolder, imageFolder)): # For each image in the folder
                                        if image.endswith(".tiff"): # If it's a .tiff...
                                            # Open the .tiff, grab the old xy resolution, and overwrite it with the new metadata.
                                            with TiffFile(join(hsFolder, guidFolder, insideFolder, imageFolder, image), mode='r+b') as tif:
                                                oldX = tif.pages[0].tags['XResolution'].value
                                                _ = tif.pages[0].tags['XResolution'].overwrite(resTIFF_formatted)
                                                __ = tif.pages[0].tags['YResolution'].overwrite(resTIFF_formatted)

                                            # Re-open the .tiff to confirm the new metadata.
                                            with TiffFile(join(hsFolder, guidFolder, insideFolder, imageFolder, image), mode='r') as tif:
                                                newX = tif.pages[0].tags['XResolution'].value

                            print(f"\tOld XY Resolution: {10000/(oldX[0]/oldX[1])} um/pixel")
                            print(f"\tNew XY Resolution: {10000/(newX[0]/newX[1])} um/pixel")
                        else:
                            print(f"\tNo valid index.xml file found in {guidFolder}.")
                            print(f"\tXY resolution left at {10000/(oldX[0]/oldX[1])} um/pixel.")
                            failedList.append(guidFolder)

                print(f"Finished processing folder {guidFolder}.")

        sys.stdout = sys.__stdout__

        if len(failedList) > 0:
            print(f"\nFailed to update metadata in the following folders:")
            for folder in failedList:
                print(f"\t{folder}")
        else:
            print("\nAll folders processed successfully.")

        print(f"\nDetails saved to {join(hsFolder,outputName)}.\n")

    finally:
        input("Press Enter to close this window...")

if __name__ == "__main__":
    main()