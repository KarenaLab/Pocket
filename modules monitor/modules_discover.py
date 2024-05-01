# Modules monitor (P337) -----------------------------------------------

# Libraries
import os
import sys

# Personal modules
sys.path.append(r"C:\python_modules")


# Setup/Config
path = r"C:\python_modules"


# Program --------------------------------------------------------------
os.chdir(path)

files_list = os.listdir()
new_list = []

# Remove folders
for f in files_list:
    if(os.path.isfile(f) == True):
        new_list.append(f)


# Remove not python (.py) files
if(len(new_list) > 0):
    print(f'\n Personal modules at "{path}"') 

    # Updating database
    files_list = new_list[:]
    new_list = []

    for f in files_list:
        name, extension = f.split(".")
        if(extension == "py"):
            new_list.append(f)
            print(f" > {name}")

print("")

# end

