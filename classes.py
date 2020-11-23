# Classes demo

# int, float, str : basic data types
# Class is also a data type, called Abstract Data type.
# user defined data type.

print('Defining a class')
class myclass:
    def __init__(self):
        self.data = 10
    def display(self):
        print(f"Printing the value of data: {self.data}")
    def cal(self, val):
        print(f"Printing the value of cal: {val * 2}")

m1 = myclass()
m1.display()
m1.cal(3)