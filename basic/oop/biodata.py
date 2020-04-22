# """
# 1 class bisa mempunyai banyak objek
# dan setiap objek bisa memanggil semua atribut atau fungsi yang ada di dalam class
# """
# class Oop:
    # 1

    # name = 'Ardi'
    #
    # def getName(self):
    #     return self.name



    # 2
    # """name = ''
    #
    # def getName(self, name):
    #     self.name = name
    #     return self.name"""

# objek
# player = Oop()


# output
# print(player. getName('Ardi'))


"""
instens atribut atau init
otomatis di panggil saat membuat objek dari class/parameter wajib dari class harus menggunakan __namafunction__()
dibawah ini contoh nya dan inheritance
"""
class Biodata:
    def __init__(self, name, kelas):
        self.name  = name
        self.kelas = kelas

    def getName(self):
        return self.name

    def getKelas(self):
        return self.kelas


class siswaBaru(Biodata):
    def getJk(self, Jk):
        self.Jk = Jk
        return self.Jk



biodata1 = siswaBaru('Diaz', 'XI RPL 1')
biodata2 = Biodata('Muhamad Ardi Nur Insan', 'XI RPL 1')
# class gabungan parent dengan child
print("Nama : " + biodata1.getName() + "\nKelas : " +  biodata1.getKelas() + "\nJenis Kelamin : " + biodata1.getJk("L"))
# class parent asli
print("Nama : " + biodata2.getName() + "\nKelas : " +  biodata2.getKelas())







#
