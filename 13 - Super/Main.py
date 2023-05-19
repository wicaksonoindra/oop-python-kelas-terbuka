class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} dengan health: {self.health}")

class Hero_intelligent(Hero):
    def __init__(self,name):
        # Hero.__init__(self, name ,100)
        super().__init__(name,100)
        # Hero.showInfo(self)
        super().showInfo()

class Hero_strenght(Hero):
    def __init__(self,name):
        # Hero.__init__(self, name, 200)
        super().__init__(name,200)
        # Hero.showInfo(self)
        super().showInfo()

lina = Hero_intelligent('lina')
axe = Hero_strenght('axe')
