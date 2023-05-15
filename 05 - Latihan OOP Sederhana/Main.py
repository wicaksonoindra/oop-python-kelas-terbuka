class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = attackPower_lawan/self.armorNumber
        print(f'serangan terasa: {attack_diterima}')
        self.health -= attack_diterima
        print(f'darah {self.name} tersisa {self.health}')

sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
