class Teglalap:
    alap = 8
    def __init__(self, a_oldal=2, b_oldal=3):
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def kerulet(self):
        return self.a_oldal * 2 + self.b_oldal * 2

    def terulet(self):
        return self.a_oldal * self.b_oldal

class Negyzet(Teglalap):
    def __init__(self, a_oldal, b_oldal=0):
        super().__init__(a_oldal, b_oldal)
        self.a_oldal = a_oldal
        self.b_oldal = a_oldal

class Haromszog(Teglalap):
    pass

class Trapez(Teglalap):
    pass

tegla = Teglalap(8,3)

print("a = ", tegla.a_oldal)
print("b = ", tegla.b_oldal)
print("kerület = ", tegla.kerulet())
print("terület = ", tegla.terulet())

negy = Negyzet(5)
print("a = ", negy.a_oldal)
print("b = ", negy.b_oldal)
print("kerület = ", negy.kerulet())
print("terület = ", negy.terulet())

