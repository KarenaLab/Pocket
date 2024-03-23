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




# Program --------------------------------------------------------------




# end

