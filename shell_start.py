import os
from os import path
import shutil

def main():
    #duplicate an existing file
    filename = "textfile.txt"
    if (path.exists(filename)):
        src = path.realpath(filename) 
        dest = src + ".bak"
        shutil.copy(src,dest) # copies only the contents of the file

        # copy the metadata(modification time , permissions, and other info) along with the file
        shutil.copystat(src,dest)
if __name__ == "__main__":
    main()