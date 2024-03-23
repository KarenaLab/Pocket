# AutoBackup [P164]
# Automatic backup for Book2 and external driver


# Libraries
import os
import shutil



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


def create_folder(destiny, list_folders, verbose=False):
    """
    Given **destiny** and a list of names, cretes that folders.
    (( Does not returns any value ))

    """
    for i in list_folders:
        os.makedirs(os.path.join(destiny, i))

        if(verbose == True):
            printline(f" > created folder: {os.path.join(destiny, i)}")


    return None

def delete_folder(destiny, list_folders, verbose=True):
    """
    Given **destiny** and a list of names, delete that folders.
    (( Does not returns any value ))

    """
    for i in list_folders:
        shutil.rmtree(os.path.join(destiny, i))

        if(verbose == True):
            printline(f" < deleted folder: {os.path.join(destiny, i)}")


    return None


def create_file(destiny, list_files, verbose=True):
    """
    Given **destiny** and a list os files, creates a copy.
    (( Does not return any value ))

    """
    for i in list_files:
        src = os.path.join(os.getcwd(), i)
        dst = os.path.join(os.path.join(destiny, i))
        shutil.copyfile(src, dst)

        if(verbose == True):
            printline(f" -> created file: {dst}")


    return None

def delete_file(destiny, list_files, verbose=True):
    """
    Given **destiny** and a list os files, delete that files.
    (( Does not return any value ))

    """
    for i in list_files:
        os.remove(os.path.join(destiny, i))

        if(verbose == True):
            printline(f" <- deleted file: {os.path.join(destiny, i)}")


    return None


def update_file(destiny, list_files, verbose=True):
    """
    Given **destiny** and a list os files, creates a copy.
    (( Does not return any value ))

    """
    for i in list_files:
        time_src = os.path.getmtime(os.path.join(os.getcwd(), i))
        time_dst = os.path.getmtime(os.path.join(destiny, i))

        if(time_src > time_dst):
            src = os.path.join(os.getcwd(), i)
            dst = os.path.join(destiny, i)
            shutil.copyfile(src, dst)

            if(verbose == True):
                printline(f" --> updated file: {dst}")


    return None


def printline(text, first=30, last=35):
    """
    Keep each verbose line as a single line.
    Splits and contracts as two parts, controled by **first** and
    **last**.
    
    """
    if(len(text) > (first + last - (4+1))):
        text = text[0:first] + " ..." + text[-last: ]

    print(text)

    return None


def backup(path_source, path_destiny, verbose=True):
    """
    Backups data from **path_source** to **path_destiny**
    

    """
    for (src_path, src_folders, src_files) in os.walk(path_source):
        # Move for source path
        os.chdir(src_path)

        # Create the "shadow" path for destiny
        dst_path = path_destiny + src_path.replace(path_source, "")

        # 1a- Read files and folders from source (nade by the function os.walk)

        # 1b - Read files and folders from source
        dst_folders = read_folders(dst_path)
        dst_files = read_files(dst_path)


        # 2a - Folders: Create folders that does not exists in destiny
        list2create = left_join(left=src_folders, right=dst_folders)
        if(len(list2create) > 0):
            create_folder(dst_path, list2create, verbose=verbose)

        # 2b - Folders: delete folders that exists in destiny but does not
        #      exist anymore.
        list2delete = left_join(left=dst_folders, right=src_folders)
        if(len(list2delete) > 0):
            delete_folder(dst_path, list2delete, verbose=verbose)


        # 3a - Files: Create files that does not exists in destiny
        list2create = left_join(left=src_files, right=dst_files)
        if(len(list2create) > 0):
            create_file(dst_path, list2create, verbose=verbose)

        # 3b - Files: Delete files that exists in destiny but does not exist
        #      anymore.
        list2delete = left_join(left=dst_files, right=src_files)
        if(len(list2delete) > 0):
            delete_file(dst_path, list2delete, verbose=verbose)

        # 3c - Files: Update files
        list2update = inner_join(left=src_files, right=dst_files)
        if(len(list2update) > 0):
            update_file(dst_path, list2update, verbose=verbose)


    return None


# Program --------------------------------------------------------------

path_source = [r"D:\01 - Projects Binder",
               r"D:\04 - Data Science",
               r"D:\05 - DataDNA",
               r"D:\06 - Samsung SRBR",
               r"D:\09 - Documents",
               r"D:\10 - Images",
               r"D:\99 - INBOX"]

path_destiny = [r"E:\Book2\01 - Projects Binder",
                r"E:\Book2\04 - Data Science",
                r"E:\Book2\05 - DataDNA",
                r"E:\Book2\06 - Samsung SRBR",
                r"E:\Book2\09 - Documents",
                r"E:\Book2\10 - Images",
                r"E:\Book2\99 - INBOX"]


for source, destiny in zip(path_source, path_destiny):
    backup(source, destiny)
    #_ = input()


# end
