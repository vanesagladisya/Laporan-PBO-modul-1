class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan_diri
    def perkenalan_diri(self):
        print(f"Nama        : {self.nama}")
        print(f"NIM         : {self.nim}")
        print(f"Jurusan     : {self.jurusan}")
        print(f"Universitas : {Mahasiswa.universitas}")
        print(f"IPK         : {self.ipk}\n")

    # Method update_ipk
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru

    # Method predikat_kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# =======================================
#          INSTANSIASI 3 MAHASISWA
# =======================================

m1 = Mahasiswa("Rose", "240101001", "Bisnis Digital", 3.0)
m2 = Mahasiswa("Lisa", "240101002", "Sistem Informasi", 3.4)
m3 = Mahasiswa("Jennie", "240101003", "Teknik Informatika", 2.2)

# Demonstrasi perkenalan_diri()
m1.perkenalan_diri()
m2.perkenalan_diri()
m3.perkenalan_diri()

# Update IPK
m1.update_ipk(3.4)
m2.update_ipk(3.7)
m3.update_ipk(2.8)

print("Predikat Kelulusan:")
print(f"{m1.nama}: {m1.predikat_kelulusan()}")
print(f"{m2.nama}: {m2.predikat_kelulusan()}")
print(f"{m3.nama}: {m3.predikat_kelulusan()}")
