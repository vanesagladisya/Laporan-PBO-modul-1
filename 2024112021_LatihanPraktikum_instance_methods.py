class ManajerInventori:
    def __init__(self):
        self.inventori = {}  # Menyimpan data barang: {nama: stok}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah > 0:
            if nama_barang in self.inventori:
                self.inventori[nama_barang] += jumlah
            else:
                self.inventori[nama_barang] = jumlah
            return f"Berhasil menambah {jumlah} {nama_barang}. Total stok: {self.inventori[nama_barang]}"
        return "Jumlah harus positif"

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang not in self.inventori:
            return "Barang tidak ditemukan"
        
        if 0 < jumlah <= self.inventori[nama_barang]:
            self.inventori[nama_barang] -= jumlah
            if self.inventori[nama_barang] == 0:
                del self.inventori[nama_barang]
            return f"Berhasil mengurangi {jumlah} {nama_barang}"
        
        return "Jumlah tidak valid atau stok tidak mencukupi"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        
        daftar = "=== Daftar Inventori ===\n"
        for barang, stok in self.inventori.items():
            daftar += f"{barang}: {stok}\n"
        return daftar.rstrip()
    

# Demonstrasi Method
inv = ManajerInventori()

print(inv.tambah_barang("Laptop", 5))
print(inv.tambah_barang("Mouse", 10))
print(inv.tambah_barang("Laptop", 3))

print(inv.hapus_barang("Mouse", 4))
print(inv.hapus_barang("Laptop", 2))

print(inv.lihat_inventori())
