# AutoBackup [P164]
# Automatic backup for Book2 and external driver


# Libraries
import os
import sys



# Functions
def read_files(path):
    """
    Create a list with all **files** from given **path**.
    Returns an empty list if the path does not exists.

    """
    # Local path
    path_local = os.getcwd()

    # Read the files
    file_list = list()

    if(os.path.isdir(path) == True):
        os.chdir(path)
        all_items = os.listdir()

        for f in all_items:
            if(os.path.isfile(f) == True):
                file_list.append(f)

        os.chdir(path_local)

    return file_list


def read_folders(path):
    """
    Create a list with all **folders** from given **path**.
    Returns an empty list if the path does not exists.

    """
    # Local path
    path_local = os.getcwd()

    # Read the folders
    folder_list = list()

    if(os.path.isdir(path) == True):
        os.chdir(path)
        all_items = os.listdir()

        for f in all_items:
            if(os.path.isdir(f) == True):
                folder_list.append(f)

        os.chdir(path_local)

    return folder_list


def left_join(left, right):
    """
    Performs **left_join** between two lists.

    """
    l_join = list()

    for i in left:
        if(right.count(i) == 0):
            l_join.append(i)

    return l_join


def inner_join(left, right):
    """
    Performs **inner_join** between two lists.

    """
    i_join = list()

    for i in left:
        if(right.count(i) > 0):
            i_join.append(i)

    return i_join



# Program --------------------------------------------------------------
source = "D:\\"    
destiny = ""  
verbose = True

# end

