
# BERMAIN DENGAN FILE 


#      nama file->mode build in function ada di web resmi python

file = open('data.txt', 'a+') #r+dari awal dan a+ mulai dari akhir atau menambahkan filenya


def add_to_list(newtext):
    file.write('\n' + newtext)
    ask_user()

def ask_user():
    add_to_list(input("Tuliskan list anda : "))

ask_user()