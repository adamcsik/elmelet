def beker(min, max, uzenet, maxProba):
    proba = 1
    szam = int(input(uzenet))
    while szam < min or szam > max:
        print("Roosz értéket adott meg!")
        szam = int(input(uzenet))
        proba += 1
        if proba > maxProba:
            exit()
    return szam, proba

# innen indul
if __name__ == "__main__":
   print(beker(18, 65, "Kérem az életkorát: ", 3))
   print(__name__)
