try:
    print(8/0)
except NameError:
    print("névhivatkozás hiba")
except ZeroDivisionError:
    print("osztás nullával")

"""fajl = open('holnap.txt', "r", encoding='utf-8')

for sor in fajl:
    sor = fajl.readline()
    print(sor.strip())

teljes = fajl.read()
print(teljes)
fajl.close()"""

with open('holnap.txt', "r", encoding='utf-8') as fajl:
    for sor in fajl:
        print(sor.strip())


