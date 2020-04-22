
# BAGIAN 1
import data as d         #-> untuk menimport seluruh data
#from data import nama    #-> untuk mengimport hanya bagian objek tertentu

import data as d


print(d.person)
print(d.nama("Jack"))
print(d.benda)



# data waktu sekarang
import datetime
# now = datetime.datetime.now()
# print(now)

# data waktu bebas
# date = datetime.datetime(2020, 1, 1)
# print(date)

# tampilah tahun, bulan, tgl
now = datetime.datetime.now()
print(now.strftime("%Y, %B, %d"))




# GLOBAL & LOCAL var


Nama = "Ardi"           #variabel ini adalah variabel global

def bunyi():
    #Nama = "Nur"   ->     #variabel ini hanya di miliki di dalam metod bunyi saja atau di sebut juga variabel lokal
    global Nama #untuk bisa mengakses variabel global
    Nama = Nama + " Hydra"  #edit menjadi Ardi Hydra
    print("akses dari dalam metod : ", Nama)

bunyi()
print("akses dari luar metod : ", Nama)



"""
MEMBANTU UNTUK MEN debug
"""
# raise Expection("Stop ada kesalahan") -> berfungsi untuk mematikan kodingan ke bawahnya agar memudahkkan dalam men debug error
"""
try:
    print("test", a) # kesalahan
except:
    print("oow ada yang salah...") #untuk mengeluarkan output kesalahan yg kita inginkan
"""


"""
CEK SISTEM OPERASI
"""
# import sys
# print(sys.platform)




#
