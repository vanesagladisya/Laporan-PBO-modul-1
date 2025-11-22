class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"
    

# pembuatan objek
mhs1 = Mahasiswa("Budi Santoso", "TI001")
mhs2 = Mahasiswa("Siti Aminah", "TI1002")


print(mhs1.perkenalan())
print(mhs2.perkenalan())