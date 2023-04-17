from math import pi
AmountOfNumbersToPrint = input("How many numbers do you want to print: ")
try:
    AmountOfNumbersToPrint = int(AmountOfNumbersToPrint)
except:
    print("Amount of numbers to print is invalid")
    exit()
# i is a counter variable
for i in range(AmountOfNumbersToPrint):
    print("loop ran")