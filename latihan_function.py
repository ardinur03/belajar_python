def luasSegiempat(panjang, lebar):
    return panjang*lebar

def main():
    panjang = int(input())
    lebar   = int(input())
    luas1   = luasSegiempat(panjang, lebar)

    panjang = int(input())
    lebar   = int(input())
    luas2   = luasSegiempat(panjang, lebar)
    print (luas1 + luas2)
main()
