def luasSegiempat(panjang, lebar):
    return panjang*lebar

def main():
    p   = int(input("Masukkan panjang : "))
    l   = int(input("Masukkan lebar   : "))
    luas1   = luasSegiempat(p, l) #variabel dalam parameter bisa beda

    panjang = int(input("Masukkan panjang : "))
    lebar   = int(input("Masukkan lebar   : "))
    luas2   = luasSegiempat(panjang, lebar) #variabel dalam parameter bisa sama
    print ("Luas keduanya yaitu : ", luas1 + luas2)
main()
