Valinta = input("Minkälaisen hytin haluaisit vaihtoehdoista LUX, A, B tai C? ")
if Valinta == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif Valinta == "A":
        print("A on ikkunallinen hytti ulkokannen yläpuolella")
elif Valinta == "B":
        print("B on ikkunaton hytti autokannen yläpuolella")
elif Valinta == "C":
        print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")