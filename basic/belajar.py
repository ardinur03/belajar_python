print("\t WELCOME TO LEARN PYTHON")

# identitas about me
Nama  = "Muhamad Ardi Nur Insan"
Kelas = "11 RPL 1"
print("Nama  :", Nama +"\nKelas :", Kelas)
print("----------------\"-----\"-----------------")


# aplikasi sederhana penanyaan Nama
# concatinetion (penggabungan string)
"""
nama = input("\nSiapa nama anda bosqu?? ")
umur = input("\nUmur berapa anda?? ")
print("Wihh..salam kenal! boss " + nama + " Umur anda  " + umur + " Tahun")
"""


# boolean
"""
x = "ardi"
print(x.isalnum()) #mengecek apakah ini nomber atau bukan
"""


#if else
"""
angka1 = 90
angka2 = 100
if angka1 > angka2:
    print("Horee benar!!!")
else:
    print("Oow! salah!")
"""

# aplikasi sederhana hitung hutang if-elif-else
"""
uang = input("Uang anda berapa? ")
hutang = 10000

if int(uang) < hutang:
    print("Hutang anda : ", hutang)
    print("Uangnya kurang bos!!!:)")
elif int(uang) == hutang:
    print("Hutang anda : ", hutang)
    print("Terimakasih sudah membayar :)")
else:
    hasil = int(uang)-hutang
    print("Hutang anda : ", hutang)
    print("Uang lebih bos!!! Kembaliannya : ", hasil)
"""


# contoh if else bercabang
"""
Putri raja ingin menikah dengan syarat baik dan rajin

tamu  = "cwe"
baik  = True
rajin = True

if baik & rajin:
    if tamu == "cwo":
        print("Nikah yuk!!!")
    else:
        print('kita sodaraan saja!!!')
else:
    print("hush! sana!!!")
"""


#perulangan while
"""
hitung = 0
while hitung < 5:
    print("Halloo Ardi!!!")
    hitung = hitung+1
"""

# for in
"""
orang = ['Ardi', 'Ahmad', 'Bujank', 'Naufal', 'Diaz']
#judul = "YT Ardi Hydra"
for nama in orang:
    print("Nama orangnya adalah : ", nama)
"""

# loop bercabang while
"""
a = 1
while a < 5:
    b = 0
    while b < a:
        print("*", end="")
        b += 1
    print()
    a += 1
"""
# loop bercabang while
"""
for a in range(1,5):
    for b in range(1,5):
        c = a*b
        print(c, end="  ")
    print()
"""



# list
"""
orang  = ['Ardi', 'Ahmad', 'Diaz', 'Naufal']
umur   = [18, 17, 17, 19, 36]
mixed  = ['text', 78, 9.7]

# menampilkan semua dalam lis->var
# print(orang)

# mengedit list
# orang[0]= "Muhamad Ardi Nur Insan"

# tambah data list
# orang.append('nur insan')

# hapus data list
# del orang [4]
print(orang)
"""


"""
# dictionary
orang = {'Nama' : 'Muhamad Ardi Nur Insan',
        'kelas' : 'XI RPL 1',
        'Umur' : '17 Tahun',
        'Jenis Kelamin' : 'Laki-laki'
}

# memanggil hasil
print("Namanya adalah : ", orang['Nama'])
print("Umurnya adalah : ", orang['Umur'])

# menambah data
orang['Sekolah'] = 'SMK Negeri 11 Bandung'

# mengedit data
orang['Nama'] = 'Ardi Hydra'

# menghapus data
del orang['Umur']


print("Sekolahnya adalah : ", orang)

# mengeluarkan sesuai data dictionary
for key, value in orang.items():
    print(key + " - " + value)
"""


# list = [] - dictionary {} - tuples ()


# nested dictionary
data = { 1:{'nama':'ardi', 'kelas':'XI RPL 1', 'sekolah':'SMK Negeri 11 Bandung'},
         2:{'nama':'mad', 'kelas':'XI MM 1', 'sekolah':'SMK Negeri 11 Bandung'}
}

# print(data[1]['nama']) = untuk memanggil sallah satu key awal
"""
for key, value in data.items():
    print("\nKeynya : ", key)
    for key2 in value:
        print(key2 + "-", value[key2])
"""




"""
#FUNCTION = PARAMETER, RETURN, KEYWORD ARGUMEN
 1. tanpa berparameter
 2. ada parameter
 3. parameter default
 parameter = argumen
"""
# 1 parameter
"""
def printArdi(teks = 'Parameter belum di isi'):
    print("----------")
    print(teks)
    print("----------")

printArdi("Muhamad Ardi Nur Insan")
printArdi("XI RPL 1")
"""
# 2 parameter
"""
def printTeks(nama = 'Parameter nama kosong!!!', kelas = 'Parameter kelas kosong!!!'):
    print("----------------------")
    print(nama)
    print(kelas)
    print("----------------------")

printTeks("Muhamad Ardi Nur Insan", "XI RPL 1")
"""
# fungsi menggunakan return
"""
def hitung(a,b,c):
    return (a*b)+c

print("Hasil perkalian : ", hitung(4,5,1))
"""
# fungsi menggunakan keyword argumen
"""
def data(nama, kelas):
    print("Nama "+nama + "  Kelas  "+ kelas)

data(kelas = "XI RPL 1", nama = "Muhamad Ardi Nur Insan")
"""
# percobaan
"""def coba(nama, kelas, sekolah, noHp = "nope kosong"):
    print("Nama     : "+nama)
    print("Kelas    : "+kelas)
    print("Sekolah  : "+sekolah)
    print("No Hp    : "+noHp)
coba("Muhamad Ardi Nur insan", "XI RPL 1", "SMK Negeri 11 Kota Bandung", "08953288984")
"""
# *args
"""def benda(*args):
    for nama in args:
        print(nama)
benda("pulpen", "pensil", "penggaris", "penghapus")"""
# **kwargs
def jurusan(**jrs):
    for nama, nilai in jrs.items():
        print(nama, " - ", nilai)
jurusan(MM = "Multimedia", RPL = "Rekayasa Perangkat Lunak", TKJ = "Teknik Komputer dan Jaringan")







print(" ")
