
# Chris Nyland
# 2023-07-14

# Install settings into notepadpp

import os
import shutil
import xml.etree.ElementTree as ET

here = os.path.dirname(__file__) if os.path.dirname(__file__) else os.getcwd()

# Define on all the source and destination files in a system and 
# location agnostic way
notepadpp_folder = os.path.expandvars(r"%APPDATA%\notepad++")
shortcuts_xml = os.path.join(notepadpp_folder, "shortcuts.xml")
shortcut_folder = os.path.join(notepadpp_folder, "shortcut_batchfiles")
batchfile_name = 'RunPythonFull.bat'

# Create a shortcuts folder if it doesn't exist
if not os.path.isdir(shortcut_folder):
    os.mkdir(shortcut_folder)

# Copy the batch script into the Notepad++ APPDATA folder
# This will overwrite the file if it exists
src = os.path.join(here, batchfile_name)
dst = os.path.join(shortcut_folder, batchfile_name)
shutil.copyfile(src, dst)

# Parse the current shortcuts.xml from the APPDATA folder and get the
# UserDefinedCommands element.
tree = ET.parse(shortcuts_xml)
root = tree.getroot()
udc = root.find('UserDefinedCommands')

# Add the our user defined commands match the current padding in a 
# sort of hacky way. We also redefine the tail of the last element 
# before we start to add our elements so the spacing looks right.
udc[-1].tail = '\n' + 8 * ' '
with open('userdefinedcommands.xml') as fid:
    for line in fid:
        element = ET.fromstring(line)
        element.tail = '\n' + 8 * ' '
        udc.append(element)

# Write the changes back to the APPDATA folder
tree.write(shortcuts_xml)    
