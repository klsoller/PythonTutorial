"""
learn_os.py
SUMMARY DOCS
LICENSE: ALL RIGHTS RESERVED.
"""

import os
import sys
from icecream import ic


sys.path.append("../PythonTutorial")
sys.path.append("../PythonTutorial/tests")


import tests.calc as calc
from test import test_calc


os.system("cls")


# test 1
ic(dir(os))


# test 2
os.getcwd()
os.chdir(r"C:\Users\kaleb\source\repos\klsoller\PythonTutorial")  # Change Directory


# test 3
ic(os.listdir())


# TODO test 4 - os.mkdir()
# ! os.mkdir will not make multiple directories. You have to use os.makedirs(). See 'test 5'
#  ** It's probably best practice to just use os.makedirs().
# // useless comment
new_directory = "folder_name"
# param os.mkdir(new_directory)  # Comment out so it doesn't print every test.


# TODO test 5 - os.makedirs()
# ** It's probably best practice to just use os.makedirs().
multiple_directories = "year/month/day/folder_name"
# os.makedirs(multiple_directories)  # Comment out so it doesn't print every test.


# TODO test 5 - os.rmdir()
# This will not remove multiple directories.
# os.rmdir("/path/to/file/file_name.py")


# TODO test 6 - os.removedirs()
# ! More dangerous than os.rmdir()
# This *WILL* not remove multiple directories.
# os.removedirs("/path/to/file/file_name.py")


# TODO test 7 - os.rename()
# Rename the file.
# This can also pass a directory. See documentation.
os.rename("test.txt", "demo.txt")


# TODO test 8 - os.stat()
# Get the information about the file.
print(os.stat("demo.txt"))
print(os.stat("demo.txt").st_size)  # .DOT notation from returns, below. etc.
"""
 RETURN:    
            st_mode
            st_ino
            st_dev
            st_nlink
            st_uid
            st_gid
            st_size 'in BYTES' = '20 BYTES'
            st_atime    
            st_mtime    'modification time' in timestamp (import datetime)
            st_ctime    
"""

# TODO test 9 - os.walk()
# Gets current directory items. Walks the directories down in BWF soft pattern.
# Does the entire root path on the passed directory.
# This is the search feature on Windows File Explorer.
"""

"""
for dirpath, dirnames, filenames in os.walk("/directory/name/"):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()


# TODO test 10 - os.enrion()
#
print(os.environ.get("HOME"))


class os_path:

    def __init__(self) -> None:
        pass

    def first(self):
        pass

    print(dir(os.path))

    # ** TOP os.path functions to use in your projects.

    # TODO test 11 - os.path.join('/user/downloads/test.txt')
    # os.path.join()
    # os.path.join("path/location", "test.txt")

    # TODO test 12 - os.path.basename('/user/downloads/test.txt')
    # Get the filename only of the file you are working on.
    # /user/downloads/test.txt -> 'test.txt'

    # TODO test 13 - os.path.dirname('/user/downloads/test.txt')
    # Get the directory only of the file you are working on.
    # /user/downloads/test.txt -> '/user/downloads'

    # TODO test 14 - os.path.split('/user/downloads/test.txt')
    # Get the filename, & directory  of the file you are working on.
    # /user/downloads/test.txt -> ('/user/downloads', 'text.txt') as a tuple

    # TODO test 15 - os.path.exists('/user/downloads/test.txt')
    # Checks if the filename exists.
    # /user/downloads/test.txt -> True | False

    # TODO test 16 - os.path.isdir('/user/downloads/test.txt')
    # Returns boolean if it is a directory.
    # /user/downloads/test.txt -> True | False

    # TODO test 17 - os.path.isfile('/user/downloads/test.txt')
    # Returns boolean if it is a file.
    # /user/downloads/test.txt -> True | False

    # TODO test 18 - os.path.splitext('/user/downloads/test.txt')
    # Get the directory/filename, & extension  of the file you are working on.
    # /user/downloads/test.txt -> ('/user/downloads/test', '.txt') as a tuple


class os_system:

    def __init__(self) -> None:
        pass

    def os_system(self):
        pass
        # Executes the file passed, or runs the file.
        os.system("test.txt")

    def os_getcwd(self):
        pass
        # Return the Current Working Directory (cwd).
        os.getcwd()

    def os_listdir(self):
        pass
        # returns the
        # os.listdir() == os.listdir(os.getcwd())
        os.listdir("/path/to/directory/")
        # RETURNS: file filenames and directories as str.

    def os_mkdir(self):
        pass
