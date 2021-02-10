class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(objek, nama, gaji):
        objek.nama = nama
        objek.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(objek):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(objek):
        print("Nama :", objek.nama)
        print("Gaji :", objek.gaji)

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)
