class myClass():
    def method1(self):
        print("method1")

    def method2(self,something):
        print("myclass method2",something)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("another class method1")

    def method2(self,something):
        print("another class method2")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")

# Python interpretor check if the name is main, if yes, it executes its own program 
if __name__ == "__main__":
    main()