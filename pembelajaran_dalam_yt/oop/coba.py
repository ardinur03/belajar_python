class Manusia:
    nama = "anonymouse"
    def Copy(self):
        manusiaBaru = Manusia()
        manusiaBaru.nama = self.nama + " copy"
        return manusiaBaru

def main():
    bilangan = 12
    m = Manusia()
    m2 = m.Copy()
    print(m2.nama)

main()
