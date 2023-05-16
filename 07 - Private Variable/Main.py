class Hero:

    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable instance private, tidak bisa di akses dan tidak bisa di ubah
        self.__private = "private"

        # variable instance protected, bisa di akses dan dirubah, namun tidak boleh dirubah
        self._protected = "protected"


lina = Hero('lina',100)

print(lina.__dict__)
print(Hero.__dict__)
