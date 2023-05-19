class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.showInfo()

    def showInfo(self,tipe):
        print(f"{self.name}\n\tTipe: {tipe}\n\thealth: {self.health}")

class Hero_intelligent(Hero):
    def __init__(self,name):
        super().__init__(name, 100)
        # super().showInfo()

    def showInfo(self):
        # super().showInfo('intelligent')
        # override
        print(f"{self.name}\n\tTipe: intelligent\n\thealth: {self.health}") # override showinfo pada Hero class

class Hero_strenght(Hero):
    def __init__(self,name):
        super().__init__(name, 200)
        # super().showInfo()

    def showInfo(self):
        # super().showInfo('strength')
        # override
        print(f"{self.name}\n\tTipe: strength\n\thealth: {self.health}") # override showinfo pada Hero class

lina = Hero_intelligent('lina')
axe = Hero_strenght('axe')
