class Mangga:

    def __init__(self,name,jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self): # untuk debugging
        return "repr - Mangga: {} dengan jumlah: {}".format(self.name,self.jumlah)

    def __str__(self): # untuk produuction
        return "Mangga: {} dengan jumlah: {}".format(self.name,self.jumlah)

    def __add__(self,objek):
        return self.jumlah + objek.jumlah

    @property # override __dict__ magic method
    def __dict__(self):
        return "objek ini memiliki nama dan jumlah"

belanja1 = Mangga('arumanis',10)
belanja2 = Mangga('mana lagi',27)
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)
