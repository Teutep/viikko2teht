userInput = input("Sano luku: ")
maxValue = minValue = int(userInput)

while True
    userInput = input("Sano luku: ")
    if userInput = "":
        break
    if int(userInput) < minValue:
        minValue = int(userInput)
    if int(userInput) > maxValue:
        maxValue = int(userInput)
print(f"Pienin arvo {minValue} ja suurin arvo {maxValue}")