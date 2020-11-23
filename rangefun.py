# Loops

# for loop
for val in range(1, 10):
    # do something
    print(f"value: {val}")

# for loop
for val in range(1, 10):
    # do something
    print(f"value: {val}")
    if val == 6:
        break

for val in range(0, 20, 2):
    # do something
    print(f"value: {val}")
    if val == 18:
        break

for val in range(1, 4):
    # do something
    print(f"value: {val}")

# while loop
print("Demonstrating while loop.")
val = 0
while val < 10:
    print(f"val = {val}")
    val = val + 1

mlist1 = [1, 2, 3, "quantom", 'dictionary', 5, 6.9]
mtup1 = (1, 2, 3, "quantom", 'dictionary', 5, 6.9)
print(f"mlist1 is {mlist1}")
for val in mlist1:
    print(f"list val = {val}, type={type(val)}")
    if val == 5:
        print("FIVE.....")

for val in mtup1:
    print(f"Tuple val = {val}")
print("End of program.")


for val in mlist1:
    if isinstance(val, int):
        print(f"val+100 = {val+100}")


# Write a program to print tables
tableno = 1524567
for val in range(1, 11):
    print(f"{tableno} X {val} = {tableno * val}")
