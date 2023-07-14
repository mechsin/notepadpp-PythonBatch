# notepadpp-PythonBatch
Batch files to allow a user to run Python from Notepad++.

## Installation

There is a simple install script that will copy the neccessary files to the
APPDATA directory. It will also update the shortcuts.xml. Since the entire 
point of these commands are to run Python the install script is written in 
Python because it is assumed that will be installed. Run the install command
like below:

`py install.py`

**Note:**Notepad++ overwrites the shortcuts.xml everytime it is closed so 
you need to run the install.py while Notepad++ is closed.

The install script is basic and doesn't check to see if the commands it is 
addinger are there so if you run the install script multiple times you wil
get duplicate commands.
