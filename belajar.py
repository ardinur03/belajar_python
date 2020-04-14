print("\t WELCOME TO LEARN PYTHON")

# identitas about me
"""
Nama  = "Muhamad Ardi Nur Insan"
Kelas = "11 RPL 1"
print("Nama  :", Nama +"\nKelas :", Kelas)
print("----------------\"-----\"-----------------")
"""


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
