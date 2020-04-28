class Segiempat:
    """docstring for Segiempat."""
    """
    TIDAK MENDEKLARASIKAN JUGA TIDAK APA-APA
    panjang = 0
    lebar   = 0
    """
    def luasSegiempat(self):
        return self.panjang * self.lebar


def main():
    s = Segiempat()
    s.panjang = int(input("Masukkan panjang : "))
    s.lebar   = int(input("Masukkan lebar   : "))
    luas = s.luasSegiempat()
    print("luasnya adalah : ", luas)

main()

"""
MENGGUNAKAN __INIT__
class Segiempat:
    docstring for Segiempat.

    # method __init__ ini akan di jalan kan secara otomatis
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar  = lebar


    def luasSegiempat(self):
        return self.panjang * self.lebar


def main():
    s = Segiempat(int(input("Masukkan panjang : ")), int(input("Masukkan lebar   : ")))
    luas = s.luasSegiempat()
    print("luasnya adalah : ", luas)

main()
"""
