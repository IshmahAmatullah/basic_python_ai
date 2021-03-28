class karyawan:

    jumlah_karyawan = 0

    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji
        karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total Karyawan :", karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        print("Gaji : ", self.gaji)
        print()

karyawan1 = karyawan("Budi", 20, 5)
karyawan2 = karyawan("Hana", 25, 4)
karyawan3 = karyawan("Raisa", 25, 4)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
karyawan2.tampilkan_jumlah()