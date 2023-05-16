class Hero:

    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property # membuat info dengan property akan menghasilkan output yang tepat dibanding info sebagai object instance
    def info(self):
        return "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None

sniper = Hero('sniper',100,10)

print('merubah info')
print(sniper.__dict__)
print(sniper.info)
sniper.armor = 69
print(sniper.armor)
print(sniper.__dict__)
del sniper.armor
print(sniper.armor)
print(sniper.__dict__)
