
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# Complex : can ignore for now

# Integer
x = 5
print(x)
print(type(x))

# String
x = "quantom"
print(x)
print(type(x))

# Float
x = 5.2
print(x)
print(type(x))

# Basic arithmetic operation.
a = 5.4
b = 2.8
print(a/b)
print(a//b)
print(a*b)
print(a+b)
print(a-b)
print(a%b)

# Basic string operations
# Declaring a new variable
myVar1 = None
myVar2 = None

myVar1 = "quantom"
myVar2 = 5

myVar3 = myVar1 + str(myVar2)
print("myVar3 value is", myVar3)

myVar3 = myVar1 * myVar2
print("myVar3 value is", myVar3)

# Subtraction and Division are not valid operations on strings
# myVar3 = myVar1 - str(myVar2)
# myVar3 = myVar1 / str(myVar2)
print("myVar3 value is", myVar3)

# here x is called a 'variable', assigned to 3 with assignment operator '='
x = None       # Null value
x = 3          # Integer value
x = "quantom"  # String value
x = 4.5        # Float value

# We use type function to know the type of a variable
type(x)

# To print any value, we use print function.
print(type(x))


# What is a function in Python
# Every function creation should start with keyword 'def'
# myfunction is the function name, you can have any function name
# except the pre-defined python keywords
def myfunction(data, data1):
    print("This is my function and data is ", data)
myfunction(67, "quantom")


# In python coding is done by indenting the code blocks
# Instead of using parenthesis in other languages
def anotherfunc():
    print("This is another function to demonstrate code block")
    print("This belongs to this function, because it indented with 4 spaces.")

anotherfunc()

