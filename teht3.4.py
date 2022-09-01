Vuosi = int(input("Onko tämä vuosi karkausvuosi?: "))
Jaollinen4 = Vuosi % 4
Jaollinen100 = Vuosi % 100
Jaollinen400 = Vuosi % 400
if Jaollinen4 == 0:
    if Jaollinen100 == 0 and Jaollinen400 == 0:
        print("Kyllä on")
    elif Jaollinen100 == 0 and Jaollinen400 > 0:
        print("Ei ole")
    else:
        print("Kyllä on")
else:
    print("Ei ole")