nilai = []
jumlahSiswa = int(input("Masukkan jumlah siswa : "))
for x in range(jumlahSiswa):
    nilai.append(int(input()))
counter = 0
for index in range(len(nilai)):
    if (nilai[index] >= 60):
        counter += 1
print("jumlah nilai bagusnya : ", counter)
