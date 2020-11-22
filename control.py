# Let us learn control structures

x = 7
# if else
if x == 5:
    print("Yes : true")
else:
    print("No, its not true: It is false")

# if else
if x != 5:
    print("Yes : true")
else:
    print("No, its not true: It is false")

if x == 5:
    print("The value is correct.")

print("Comparing string with integer")
# Comparing strings with integers, always false
x = '5'
if x == 5:
    print("The value is correct.")
else:
    print("Unexpected value.")

print("Testing if else with strings")
x = 'Quantom'
if x == 'quantom':
    print("The value is correct.")
else:
    print("Unexpected value.")


print("Testing the 'is' operator.")
x = "quantom"
if 'quantom' is x:          # same as if 'quantom' == x:
    print("Value found..")
else:
    print("Value not found..")

x = 5
if 5 is x:          # same as if 'quantom' == x:
    print("Value found..", x)
else:
    print("Value not found..", x)

print("Demonstrating elif")
# if x is 1, print (GET)
# if x is 2, print (PUT)
# if x is 3, print (DELETE)
# if x > 5 and < 10, print (Not Defined)
# else any other value, print (None)
x = 11
if x == 1:
    print("GET.....")
elif x == 2:
    print("PUT.....")
elif x == 3:
    print("DELETE.....")
elif x > 5 and x < 10:   # same as 5 < x < 10:
    print("Not defined.")
else:
    print('None')

# testing 'or' operator
# if x is 5 or 10, print True else false
print('Testing 'or' operator.')
x = 1
if x == 5 or x == 10:
    print("True....")
else:
    print("False...")

print("Demonstrating not operator.")
# if x is not 10, print(Not 10) else print 10
x = 20
#if x != 10:
#if not x == 10:
if x is not 10:
    print("Not 10")
else:
    print("10")

print('Demonstrating in operator.')
x = 'b'
y = 'quantom'
# check if a is present in another value.
if x in y:
    print("Found the keyword.")
else:
    print("Keyword not found.")

print("End of program.")


# More basic data types in Python.
# List
# Tuple
# Dictionary

# list is a Python mutable data structure that can hold values of any type.
# It holds data in continuous memory locations like array
# List is represented by []
mylist = list()   # create an empty list
mylist = []       # create an empty list
mylist = [1, 2, 3, "quantom"]
print(f"Printing mylist: {mylist}")
print(f"Printing mylist: {mylist[3]}")
mylist[2] = "vj"
print(f"Printing mylist: {mylist}")
mylist.append(80)
print(f"Printing mylist: {mylist}")

# Tuple is immutable.
mytuple = ()         # create an emtpy tuple
mytuple = tuple()    # create an emtpy tuple
mytuple = (1, 2, 3, "quantom",)
print(f"Printing mytuple: {mytuple}")
# mytuple[0] = '45'   # Will throw an error
print(f"Printing mytuple: {mytuple[0]}")
print(f"Printing mytuple: {mytuple[3]}")

# Dictionary is a key/value based data structure.
mydictionary = dict()    # create an empty dictionary
mydictionary = {}        # create an empty dictionary
print(f"Printing mydictionary: {mydictionary}")
mydictionary["1"] = "One"
mydictionary["10thValue"] = "Quant-OM"
print(f"Printing mydictionary: {mydictionary}")
print(f"Printing mydictionary: {mydictionary['1']}")
print(f"Printing mydictionary: {mydictionary['10thValue']}")

mydictionary = {'one': 1, 'two': 2.0, "three": 3, "zero": 0}
print(f"Printing mydictionary: {mydictionary}")
print(f"Printing mydictionary: {mydictionary['three']}")

