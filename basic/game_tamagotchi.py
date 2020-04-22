print("\tWelcome to game tamagotchi !!!")
name = input("Nama Monsternya apa ??? ")
monster = {'name' : name, 'power' : 400}
boss1 = {'name' : 'Kera', 'power' : 500}
def startGame():
    print ("1. Makan\n2. Lihat Status\n3. lawan dengan boss ke 1\n4. keluar")
    choice = input("Anda mau apa")
    if choice == "1":
        goEat()
    elif choice == "2":
        goStatus()
    elif choice == "3":
        goFight(monster, boss1)
    else:
        goOut()

def goEat():
    print("Amm...ammm.ammm")
    monster['power'] += 100
    startGame()

def goStatus():
    print("Nama Monster : ", monster['name'], "\nPower        : ", monster['power'])
    startGame()

def goFight(power, defender):
    if power['power'] > defender['power']:
         print("Anda Kuat sekali !!! anda behasil mengalahkan Boss ke 1", defender['name'])
    elif power['power'] == defender['power']:
        print("Kekuatan anda seimbang !!!")
    else:
        print("Anda terlalu lemah", power['name'])
    startGame()




def goOut():
    print("Bye..bye sampai jumpa kembali yaaa......")



startGame()
