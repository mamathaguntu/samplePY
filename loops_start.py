def main():
    x = 0
    # define a while loop
    while (x<5):
        print(x)
        x = x+1

    # for loop
    # for x in range(5, 10):
    #     print(x)

    # use a loop over a collection
    days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print(i,d) #print index and value 

    # break and continue
    # for x in range(5,10):
    #     # if (x==7):
    #     #     break
    #     if (x%2==0):
    #         continue
    #     print(x)


main()