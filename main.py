from math import pi
AmountOfNumbersToPrint = input("How many numbers do you want to print: ")
arrToPrint = ["Bizz buzz sequence: "]
try:
    AmountOfNumbersToPrint = int(AmountOfNumbersToPrint)
except:
    print("Amount of numbers to print is invalid")
    exit()
# i is a counter variable
for i in range(AmountOfNumbersToPrint):
    if(i % 3 == 0 and i % 5 == 0):
        arrToPrint.append("bizz buzz, ")
    elif(i % 3 == 0):
        arrToPrint.append("bizz, ")
    elif(i % 5 == 0):
        arrToPrint.append("buzz, ")
    else:
        arrToPrint.append((str(i) + ", "))
output = str(arrToPrint).replace("'",'',100000000)
output = output.replace("[]",'',1000000000)
print(output)