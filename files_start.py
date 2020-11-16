def main():
    # open a file to create and write content 
    # f = open("textfile.txt","w+") #write permission
    # file is open, write data to it 
    # f = open("textfile.txt", "a") #append the data to the existing file
    # for i in range(10):
        # f.write("This is line "+ str(i) +"\r\n")

    # read the file
   f = open("textfile.txt", "r") #open file in read mode
   if (f.mode == 'r'):
    #    content = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)

    # read file line by line 

    # f.close()

if __name__ == "__main__":
    main()