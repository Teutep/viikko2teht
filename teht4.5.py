username = "python"
password = "rules"
yritys = input(f"Syötä Käyttäjätunnus: ")
yritys2 = input("Syötä Salasana: ")
i = 1
while i < 5:
    if yritys == username and yritys2 == password:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
        i += 1
        yritys = input(f"Syötä Käyttäjätunnus: ")
        yritys2 = input("Syötä Salasana: ")
if i == 5:
    print("Pääsy evätty")