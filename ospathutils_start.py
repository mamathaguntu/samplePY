import os 
from os import path
import datetime
from datetime import date,time,timedelta
import time 

def main():
    # print os name 
    print(os.name)

    # check for item existence in the system
    print("item exist: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str (path.isfile("textfile.txt")))
    print("Item is a directory: " + str (path.isdir("textfile.txt")))

    # work with file paths
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path: " + str(path.split(path.realpath("textfile.txt"))))

    # get modification time 
    t = time.ctime(path.getmtime("textfile.txt"))
    print("modification time of the file textfle.txt", t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate how long ago the item was modified 
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been "+ str(td) +" since the file was modified or " + str(td.total_seconds()) + "seconds")
   
if __name__ == "__main__":
    main()
