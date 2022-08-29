kuha_pituus = float(input("Kuinka pitkä kuha on (cm)? "))
pyyntimitta = 37 #cm

if kuha_pituus < pyyntimitta:
    pyyntimitta = pyyntimitta - kuha_pituus
    print(f"Kuha on alamittainen, pyyntimitasta puuttuu {pyyntimitta}")
else:
    print("Kuha on tarpeeksi pitkä")