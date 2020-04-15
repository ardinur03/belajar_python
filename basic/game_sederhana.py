# serang menyerang
player1 = {'nama':'Lesley', 'damage': 1000}
player2 = {'nama':'Bruno', 'damage': 1000}

def farming(player):
    player['damage'] += 200

def by1(serang, defender):
    if (serang['damage'] > defender['damage']):
        print('Serangan berhasil!!! selamat untuk : ', serang['nama'])
    elif (serang['damage'] == defender['damage']):
        print('Kekuatan kedua hero seimbang')
    else:
        print('Serangan gagal!! damage kamu lemah : ', serang['nama'])

farming(player1)
by1(player2, player1)
