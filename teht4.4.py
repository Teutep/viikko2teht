import random
Vastaus = random.randint(1, 10)
Ehdotus = int(input("Arvaa numero 1-10?: "))
while Ehdotus != Vastaus:
    if Ehdotus < Vastaus:
        print(f"Liian pieni arvaus")
    elif Ehdotus > Vastaus:
        print(f"Liian suuri arvaus")
    Ehdotus = int(input("Arvaa numero 1-10?: "))
else:
    print(f"Oikein")