class Person:
    def __init__(self, name = "Anonymouse", umur = 0):
        self.__umur = umur
        self.__name = name

    def getName(self):
        return self.__name

    def getUmur(self):
        return self.__umur

    def perkenalkan_diri(self):
        return "Saya adalah " + self.__name + ", berumur " + str(self.__umur) + " tahun."

    def __add__(self, other):
        n = Person(self.getName() + other.getName(), self.getUmur()  + other.getUmur())
        return n

    def __str__(self):
        return self.perkenalkan_diri()
def main():
    p = Person("ardi", 17)
    y = Person("nur", 17)
    x = p + y
    print(str(x))

main()