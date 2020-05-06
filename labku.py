# laboraturiumku percobaan program pyton yang sementara
"""class Person():
    name = "anonymouse"


def myFunction(person, bilangan):
    person = Person()
    person.name = "ardi" #dikarenakan immutable yang asalnya anonymouse menjadi ardi jika di outputkan
    bilangan = 3         #karena integer ini immutable maka variabel 14 menjadi 3
    print(person.name)
    print(bilangan)

def main():
    p = Person()
    p.name = "ahmad" #dikarenakan immutable dan program di jalankan di dalam def main maka variabel p berisi kan ahmad
    b = 14          #di dikarenakan integer immutable maka variabel b pindah objeknya yang asalnya 3 menjadi 14
    myFunction(p, b)
    print(p.name)
    print(b)
main()"""

"""l = [11,12,13,14]
x = iter(l)

print (next(x))
print (next(x))
print (next(x))
print (next(x))"""

"""for x in l:
    print(x)"""

"""l = []
for i in range(11):
    if i % 2 != 0:
        l.append(i)
print(l)

l2 = [bilangan for bilangan in range(11) if bilangan %2 != 0]
print(l2)

x = {bilangan : bilangan + 1 for bilangan in range(11) if bilangan %2 == 0}
print (x)"""

"""def tambah(bil1, bil2):
    return bil1 + bil2

def kali(bil1, bil2):
    return bil1*bil2

def operatorMtk(bil1, bil2, operator):
    return operator(bil1, bil2)

def kurang():
    def kurangDlm(bil1, bil2):
        return bil1 - bil2
    return kurangDlm

def main():
    myFunction = kurang()
    hasil = operatorMtk(7, 5, myFunction)
    print(hasil)

main()"""



"""def bilanganku(a):
    return a

def main():
    x = bilanganku(2)
    print(x)

main()"""

"""def main():
    coordinates = [(2,3), (4,6), (7,8)]
    for x, y in coordinates:
        print ("x : ", x, "| y : ", y)

main()"""

"""def main():
    a, b, c = 11, 12, 13
    print(a, b, c)

main()"""

"""def fungsi(bilangan):
    if bilangan < 0:
        raise ValueError("Harus positif")
    return bilangan + 1

def main():
    x = int(input("Masukkan bilangan : "))
    try:
        hasil = fungsi(x)
        print(hasil)
    finally:
        print("akhir !!!")
main()"""

"""class Person:
    def __init__(self, name, umur):
        self.__name = name
        self.__setUmur(umur)


    #method akses name
    def getName(self):
        return self.__name

    #method akses umur
    def getUmur(self):
        return self.__umur

    #method ubah umur
    def __setUmur(self, umur):
        self.__umur = umur if umur >= 0 else 0

def main():
    p = Person("Muhamad Ardi Nur Insan", 17)
    print(p.getName())
    print(p.getUmur())



main()"""






l = []
for i in range(11):
    if i % 2 != 0:
        l.append(i)
print(l)

l2 = [bilangan for bilangan in range(11) if bilangan %2 != 0]
print(l2)

x = {bilangan : bilangan + 1 for bilangan in range(11) if bilangan %2 == 0}
print (x)























#
