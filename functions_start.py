# basic function
def func1():
    print("I am a function")

# func1()
# print("func1()", func1()) 
#prints 'None: string representation of 
# return value' since there is no return value
# # print(func1) gives error <function func1 at 0x0000022C0EF581F0>

# function with parameters 
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# func2(10,20)
# print(func2(10,20)) # prints none , since there is no return value


# function that returns a value
def cube(x):
    return x*x*x

# print(cube(3))

# function with default value
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result

# print(power(2)) # takes x =1 , default value
# print(power(2,3))
# print (power(x=3,num=2)) # can change the order of the parameters by specifying the parameter names 

# function with args 
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(2,3,4))

# make sure args is the last parameter when combined with the formal parameters


