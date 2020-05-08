# class parent
class Person:
    # constructor
    def __init__(self, name = "Anonymouse", umur = 0):
        self.__umur = umur
        self.__name = name
    # ambil nama
    def getName(self):
        return self.__name
    # ambil umur
    def getUmur(self):
        return self.__umur

    def perkenalkan_diri(self):
        return "Saya adalah " + self.__name + ", berumur " + str(self.__umur) + " tahun"
# class child 1
class Student(Person):
    # constructor parent
    def __init__(self, name = "Anonymouse", umur = 0, jk = "parameter kosong"):
        super().__init__(name=name, umur=umur)
        self.__jk = jk
    def perkenalkan_diri(self):
        return super().perkenalkan_diri() + " jenis kelamin " + self.__jk
# class child 2
class Teacher(Person):
    def __init__(self, name = "Anonymouse", umur = 0):
        super().__init__(name=name, umur=umur)

def main():
    c = Student("Ardi", 17, "Laki laki")
    print(c.perkenalkan_diri())
    t = Teacher("Bu Ibu", 27)
    print(t.perkenalkan_diri())
main()