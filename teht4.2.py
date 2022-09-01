Tuumat = float(input("Kuinka monta tuumaa? "))
Sentit = Tuumat*2.54 # Tuuma on 2.54cm-
while Tuumat > 0:
    print(f"Tuumat senteissä on {Sentit}")
    Tuumat = float(input("Kuinka monta tuumaa? "))
    Sentit = Tuumat*2.54
else:
    print("Negatiivisilla tuumilla ei voida laskea")