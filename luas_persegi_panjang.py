# aplikasi sederhana persegi panjang
print("Masukkan panjang : ")
panjang = float(input())
if (panjang < 0):
    panjang = panjang * -1
lebar   = float(input("Masukkan lebar : "))
if (lebar  < 0):
    lebar = lebar * -1
luas = panjang * lebar
print("Luas segiempat : ", luas)
