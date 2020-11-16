# declare f as int 
f = 0
print(f)

# redeclare f
f = "abc"
print(f)

# print combined string
print("hello world", 124)
print("this is a string "+ str(123))

# Global as local
def someFunction():
    global f
    f = "def"
    print("inside function", f)

someFunction() #prints def
print(f) #with global word, it prints the value inside function , else without global word it prints the last assigned value - abc

del f
print(f)