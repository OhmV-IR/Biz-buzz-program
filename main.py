#ask for user input
invalidinput = True
while(invalidinput):
    AmountOfNumbersToPrint = input("How many numbers do you want to print: ")
    #initialize array
    # error catching(if try fails run except)
    invalidinput = False
    try:
        AmountOfNumbersToPrint = int(AmountOfNumbersToPrint)
    except:
        print("Amount of numbers to print is invalid")
        invalidinput = True
arrToPrint = ["Bizz buzz sequence: "]
# i is a counter variable
for i in range(1, AmountOfNumbersToPrint + 1):
    #if the current number is not divisible by 5 and 3 then check if divisible by 3
    # then check if it is divisible by 5
    if(i % 3 == 0 and i % 5 == 0):
        #if divisible by 5 and 3
        # Add this to the end of the array
        arrToPrint.append("bizz buzz, ")
    elif(i % 3 == 0):
        #if divisible by 3 then add this to end of arr
        arrToPrint.append("bizz, ")
    elif(i % 5 == 0):
        #if divisible by 5 then add this to the end of arr
        arrToPrint.append("buzz, ")
    else:
        #if none is true add the number to the end of arr
        arrToPrint.append((str(i) + ", "))
# remove all quotation marks and brackets from string
output = str(arrToPrint).replace("'",'',100000000)
output = output.replace("[]",'',1000000000)
output = output.replace(",","", 1000000000)
#print final string
print(output)