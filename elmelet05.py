# modulok
'''import random
print((random.randint(1, 90)))
from random import randint
print(randint(1, 90))
print(random.choice(["egy", "kettő", "három"]))

from random import *
print(choice(["egy", "kettő", "három"]))
import random as r
print(r.choice(["egy", "kettő", "három"]))

import random


def kor():
    import random, math
    r = random.randint(1, 10)
    k = 2 * r * math.pi
    return r, k


sugar, kerulet = kor()
print("sugár:", sugar)
print("kerület:", kerulet)
'''

szamsor = range(5)
print(list(szamsor))

lista = ["-", "első", "második", "harmadik", "negyedik"]
print(lista)
print(lista[0])

for c in range(5):
    print(c)

for c in lista:
    print(c)

szoveg = "délelőtt"

for c in range(len(szoveg)):
    print(c, szoveg[c])
