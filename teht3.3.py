Sukupuoli = input("Kumpi sukupuoli olet? Mies vai nainen?: ")
Hemoglobiiniarvo = int(input("Paljonko hemoglobiini tasosi on (g/l)?: "))
if Sukupuoli == "mies":
    if Hemoglobiiniarvo < 134:
        print(f"Hemoglobiiniarvosi on liian matala")
    elif Hemoglobiiniarvo > 195:
        print(f"Hemoglobiiniarvosi on liian korkea")
    else:
        print("Hemoglobiiniarvosi on normaali")
else:
    if Hemoglobiiniarvo < 117:
        print(f"Hemoglobiiniarvosi on liian matala")
    elif Hemoglobiiniarvo > 175:
        print(f"Hemoglobiiniarvosi on liian korkea")
    else:
        print("Hemoglobiiniarvosi on normaali")