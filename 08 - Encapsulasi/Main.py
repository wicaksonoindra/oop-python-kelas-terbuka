class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attpower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getAttPower(self):
        return self.__attpower

    # setter
    def diserang(self,serangPower):
        self.__health -= serangPower

    def addAttPower(self,nilaitambah):
        self.__attpower += nilaitambah

# awal dari game
earthshaker = Hero("earthshaker",50,5)

# game berjalan
print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())
print(earthshaker.getAttPower())
earthshaker.addAttPower(5)
print(earthshaker.getAttPower())
