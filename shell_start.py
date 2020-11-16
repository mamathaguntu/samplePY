import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    #duplicate an existing file
    filename = "textfile.txt"
    if (path.exists(filename)):
        src = path.realpath(filename) 
        dest = src + ".bak"
        # shutil.copy(src,dest) # copies only the contents of the file

        # # copy the metadata(modification time , permissions, and other info) along with the file
        # shutil.copystat(src,dest)

        # rename the original file 
        # os.rename("newfile.txt",filename)

     
        # root_dir, tail = path.split(src)

        # archive entire directory
        # shutil.make_archive("archive", "zip", root_dir)
        
        # create custom zip file with required files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

        
if __name__ == "__main__":
    main()