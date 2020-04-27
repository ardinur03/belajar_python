# for
total= 0
for x in range(1, 6): # 5 juga bisa
    print ("Masukkan bilangan ke", x)
    total = total + int(input())
total = total / 5
print("Rata-rata : ", total)


# while
n = int(input("Anda ingin menghitung berapa bilangan? "))
total = 0
counter =1
while(counter <= n):
    print("Masukkan bilangan ke", counter)
    total = total + int(input())
    counter = counter+1
total = total / n
print("Rata-rata : ", total)
