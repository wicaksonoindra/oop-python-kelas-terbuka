class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_Strenght(Hero):
    pass

lina = Hero('lina',100)
techies = Hero_intelligent('techies',50)
axe = Hero_Strenght('axe',200)

print(lina.name)
print(techies.name)
print(axe.name)
