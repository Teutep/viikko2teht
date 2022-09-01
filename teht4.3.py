userInput = input("Sano luku: ")
maxValue = minValue = int(userInput)

while userInput != "":
    if int(userInput) < minValue:
        minValue = int(userInput)
    if int(userInput) > maxValue:
        maxValue = int(userInput)
    userInput = input("Sano luku: ")
print(f"Pienin arvo {minValue} ja suurin arvo {maxValue}")