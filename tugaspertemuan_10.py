# Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi"). 

Mahasiswa = ("Ardian Maulana Hasyim", 2605060065, "Teknologi Informasi")
print (Mahasiswa)
print ("\n")

# Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya.
 
print (f"NIM    : " , Mahasiswa [1])
print (f"Prodi  : " , Mahasiswa [2])
print ("\n")

# Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi.

print ("Error tersebut terjadi karena Tuple bersifat immutable (tidak dapat diubah setelah dibuat).\n Begitu sebuah tuple dideklarasikan dan diisi, isi dari tuple tersebut bersifat permanen (read-only).\n Anda tidak bisa mengubah, menambah, atau menghapus elemen individu di dalamnya menggunakan penugasan indeks")
print ("\n")
# Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5.Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!

nilai_angka = {10,4,3,2,4,10,7,5} 
print (nilai_angka)
print ("Angka 10 dan 4 yang ditulis dua kali hanya muncul sekali karena Set secara otomatis menghapus nilai duplikat\n (hanya menyimpan nilai unik) dan elemen di dalamnya bersifat tidak berurutan (unordered).")
print ("\n")

# Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut: - "nim": "240101" - "nama": "Budi Santoso" - "prodi": "Teknologi Informasi"

data_mahasiswa = {
    "nim"  : "240101",
    "nama" : "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print (data_mahasiswa)
print ("\n")

# Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026. 

data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = "2026"
print (data_mahasiswa)
print ("\n")

# Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar. 

del data_mahasiswa["nim"]
print (data_mahasiswa)
print ("\n")

# Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000} 

data_buah = {
    "apel"   : 5000,
    "pisang" : 3000,
    "jeruk"  : 7000,
    "anggur" : 15000
}

print (data_buah)
print ("\n")

# Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000" 

# Tampilkan total belanja 

total_belanja = 0

for barang, harga in data_buah.items():
    print(f"harga {barang}\t : Rp.{harga}")
    total_belanja = total_belanja + harga

print (f" Total Belanja : Rp {total_belanja}")