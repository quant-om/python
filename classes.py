# Classes demo

# int, float, str : basic data types
# Class is also a data type, called Abstract Data type.
# user defined data type.

print('Defining a class')
class myclass:
    def __init__(self):
        self.data = 10
        self.st = "myclass function"
        self.dec = 13.6
        self.myl = []
        self.myd = {"1": 1, "2": 2}
    def display(self):
        print(f"Printing the value of data: {self.data}")
    def cal(self, val):
        print(f"Printing the value of cal: {val * 2}")

m1 = myclass()
m1.display()
m1.cal(3)

class animal:
    # This the constructor method and will be called
    # during a instance creation.
    def __init__(self, carn, tail, legs, wild):
        self.carnivorous = carn
        self.tail = tail
        self.legs = legs
        self.wild = wild
        self.name = None
        self.set_animal()

    def set_animal(self):
        if self.carnivorous == True and self.wild == True:
            self.name = "Tiger"

    def print_name(self):
        print(f"The animal is {self.name}")


tiger = animal(True, True, 4, True)
tiger.print_name()

class cat(animal):
    def __init__(self, carn, tail, legs, wild):
        super().__init__(carn, tail, legs, wild)
        self.canswim = False
        self.pet = None
    def print(self):
        pass


mycat = cat(True, True, 4, False)
print(mycat.wild)
