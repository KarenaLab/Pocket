# GitHub Organizer (P249) ----------------------------------------------

# Upgrades
# Read an external .json/.txt/.csv with folders data - v04 [Dec 30th, 2022]
# Automatic remove of files at github that are not at folder
# Add an option to consider folders, or a list of folders (bigger projects) [Apr 19th, 2025]
# Remove single files in GitHub.



# Libraries
import os
import shutil

import socket
from time import sleep


# Setup/Config
path_script = os.getcwd()
path_projects = r"D:\01 - Projects Binder"


# Functions
def pc_choose():
    """
    Read PC and returns the folder to append to GitHub folder path.

    """
    pc_name = socket.gethostname()

    if(pc_name == "EKC-Zen14"):
        github_prefix = r"D:\02a - GIT EKC-Zen14"

    elif(pc_name == "EKC-Book2"):
        github_prefix = r"D:\02b - GIT EKC-Book2"

    else:
        github_prefix = None
        print(f" *** Error: PC not registered for github sync {pc_name} ***")


    return github_prefix
    

def read_txt(filename, lines=5, verbose=False):
    """
    Extracts information from a .txt.
    Returns information as a list and the number of steps to process.

    """
    # Read information from .txt
    file = open(filename, mode="r")
    buffer = file.readlines()
    file.close()

    # Prepare information as a list
    for i in range(0, len(buffer)):
        buffer[i] = buffer[i].replace("\n", "")

    blocks = len(buffer) // (lines + 1)

    # Group information
    info_list = []
    for i in range(0, blocks):
        info_dict = {}
        for j in range(0, lines+1):
            data = buffer.pop(0)
            if(data != ""):
                field, value = data.split(": ")
                info_dict[field] = value

        info_list.append(info_dict)


    if(verbose == True):
        print(f" > Number of folders to compare and transfer: {steps}")


    return info_list    
    

def files_list(path=None):
    """
    Returns a list with only file(s) (remove folder(s)) from given path
    or the current path.
    
    """
    # Path preparation
    path_comeback = os.getcwd()
    if(path != None):        
        os.chdir(path)

    # Files searcher
    f_list = list()
    for f in os.listdir():
        if(os.path.isfile(f) == True):
            f_list.append(f)


    os.chdir(path_comeback)
        
    return f_list


def folders_list(path=None):
    """
    Returns a list with only folder(s) (remove file(s)) from given path
    or the current path.
    
    """
    # Path preparation
    path_comeback = os.getcwd()
    if(path != None):        
        os.chdir(path)

    # Files searcher
    f_list = list()
    for f in os.listdir():
        if(os.path.isdir(f) == True):
            f_list.append(f)


    os.chdir(path_comeback)
        
    return f_list


def transfer_files(file_list, enable_types):
    """
    Receives a **list with file(s)** from project source
    and a **list with extension(s)** allowed to copy for github destiny.
    Returns a list with files to copy/compare between project source and
    github destiny.

    enable_types is a string with the extensions, need to handle it.

    """
    # Select file extensions to keep (enable_types)
    types_to_handle = enable_types.split(",")

    enable_types = []
    for i in types_to_handle:
        ext = i.strip()
        ext = ext.replace(".", "")
        
        enable_types.append(ext)


    # Select files with extensions enabled
    new_list = []
    for f in file_list:
        name, extension = f.split(".")
        if(enable_types.count(extension) == 1):
            new_list.append(f)


    # Remove Tester files
    file_list = new_list[:]
    remove_list = ["tester", "test"]
    
    new_list = []
    for f in file_list:
        name, extension = f.split(".")
        prefix = name.split("_")[0]
        prefix = prefix.lower()

        if(remove_list.count(prefix) == 0):
            new_list.append(f)

    
    return new_list


def remove_index(filename):
    """
    file "_vxx" extension analysis and decison to remove for github
    folder, not preserving version control but keeping it always the
    last version.
    
    """
    _name, extension = filename.split(".")
    _name = _name.split("_")

    if(len(_name) > 1):
        version = _name[-1]

        if(version[0] == "v" and version[1: ].isdigit() == True):
            name = "_".join(_name[0:-1])
            version = _name[-1]

        else:
            name = "_".join(_name)
            version = ""
                
    else:
        name = _name[0]
        version = ""

    filename = name + "." + extension

    return filename


def inner_join(left, right):
    """
    Performs **inner join** between **left** list and **right** list.
    """
    i_join = []
    for i in right:
        if(left.count(i) > 0):
            i_join.append(i)

    return i_join


def left_join(left, right):
    """
    Performs **left join** between **left** list and **right** list.
    Attention: Take care with left and right position.
    """
    l_join = []
    for i in left:
        if(right.count(i) == 0):
            l_join.append(i)

    return l_join


def outter_join(left, right):
    """
    Performs **outter join** between **left** list and **right** list.
    """
    join = left + right
    o_join = []

    for i in join:
        if(o_join.count(i) == 0):
            o_join.append(i)

    return o_join


def remove_temp_folders(path):
    """
    Removes python (__pychache__) and Jupyter (.ipnb_checkpoints)
    temporary folders

    """
    os.chdir(path)
    temp_folder = ["__pycache__", ".ipnb_checkpoints"]

    projects_list = folders_list()
    for folder in projects_list:
        os.chdir(os.path.join(path, folder))
        internal_folders = folders_list()

        for temp in temp_folder:
            if(internal_folders.count(temp) == 1):
                folder_remove = os.path.join(os.getcwd(), temp)
                shutil.rmtree(folder_remove)
                text = f"> Removing {folder_remove}"
                print_info(text)

    return None


def print_info(text, cut=12, connector="... ", limit=70):
    """
    Adjusting printing long chain of chars (paths, for example and/or long
    filenames for a single line in HALF window screen, using **limit** as
    delimiter and selecting the place to **cut**.

    """
    if(len(text) > limit):
        leftover = (-1) * (limit - cut - len(connector))
        text = text[0:cut] + "... " + text[leftover: ]

    print(text)
    
    return None


def prepare_none(string):
    if(string == "None"):
        string = None

    return string


def prepare_folders(path, folders):
    f_list = [path]

    if(folders != None):
        folders = folders.split(",")
        temp = list()
        for i in folders:
            i = i.strip()
            i = i.replace(",", "")
            i = i.replace(".", "")
            temp.append(i)
            
        folders = temp[:]       
        for f in folders:
            f_list.append(os.path.join(path, f))


    return f_list


# Main program ---------------------------------------------------------
print("\n ****  Auto Github 2 | Sync project and github folders  ****")
print(" ****              Samsung Galaxy Book 2 360            ****\n")           

# Folders to sync (External info from .txt.
#    name: Name of the folder, suggestion: Folder path,
#   types: String with the types (extensions) that will be sync,
#    root: Folder from Project (Source),
# folders: Sub folders to be included in export,
#  github: Folder from github (Destiny),


# External information
filename = "paths_for_sync.txt"
buffer = read_txt(filename)
github_prefix = pc_choose()


# Inputation and modification indexes
new_github, mod_github = 0, 0


for i in range(0, len(buffer)):
    # Upload data slice from buffer (dict)
    data = buffer[i]

    types = data["types"]
    path_root = data["root"]
    path_github = os.path.join(github_prefix, data["github"])
    folders = prepare_none(data["folders"])
    
    path_root = prepare_folders(path_root, folders)
    path_github = prepare_folders(path_github, folders)

    for p_root, p_github in zip(path_root, path_github):
        print(f'> Folder {data["name"]}')
        update = False

        os.chdir(p_root)
        
        root_files = transfer_files(files_list(), types)        
        github_files = transfer_files(files_list(p_github), types)

        # From project to GitHub    
        for filename in root_files:
            filename_noindex = remove_index(filename)

            if(github_files.count(filename_noindex) == 0):
                # File does not exists in github = Add file          
                update = True
                source = os.path.join(p_root, filename)
                destiny = os.path.join(p_github, filename_noindex)
                shutil.copyfile(source, destiny)
                print_info(f'  >>> New file at github: "{filename_noindex}"')
                new_github = new_github + 1

            else:
                # File exists in github = Check if need to update
                os.chdir(p_root)
                project_epoch = int(os.path.getmtime(filename))

                os.chdir(p_github)
                github_epoch = int(os.path.getmtime(filename_noindex))

                if(project_epoch > github_epoch):
                    update = True
                    source = os.path.join(p_root, filename)
                    destiny = os.path.join(p_github, filename_noindex)
                    shutil.copyfile(source, destiny)
                    print_info(f'  >>> Updated file at github: "{filename_noindex}"')
                    mod_github = mod_github + 1


    if(update == True):
        print("")
    
  
# Print sum up of actions ----------------------------------------------
print("")
print(f">  New files added to GitHub: {new_github}")
print(f">    Files updated at GitHub: {mod_github}")


# Cleaning Project Folder ----------------------------------------------
print("")
remove_temp_folders(path_projects)

# end
