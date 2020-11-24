# functions
print("Demonstrating functions....")


def fun():
    print("Printing my function: fun")


def fun1():
    print("Printing my function: fun1")

def multiply(x, y):
    z = x * y
    return z

mulnum = multiply(150, 160)
print(f"The return value is {mulnum}")

# Demonstrating lambda functions
# Lambda functions are anonymous functions
x = lambda a: a + 10
print(f'The value of x is {x}')
y = x(5)
print(f'The value of y is {y}')
