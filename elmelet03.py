# Ezzel a programmal egy jegyvásárlási rendszert szimulálunk
print("Jegyvásárlás".center(50,"_"))
kupon = input("\nVan kuponod?")
if kupon == "igen" or kupon == "Igen" or kupon == "i" or kupon == "I":
    print("ingyenes belépő")
else:
    print("Ez sok pénzbe fog kerülni!")
    kor = int(input("Hány éves vagy?"))
    if kor < 8:
        print("1.000 Ft")
    elif kor < 18:
        print("2.000 Ft")
    elif kor < 65:
        print("3.000 Ft")
    else:
        print("100 Ft")
print("Jó szórakozást!")
