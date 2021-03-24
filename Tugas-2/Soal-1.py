import sys

contacts_name = []
contacts_phone = []

print("Selamat Datang!")

def show_menu():
    print("------Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print("----------------")
    selected_menu = input("Pilih menu: ")
    print("\n")

    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        create_contact()
    elif(selected_menu == "3"):
        print("Program selesai, sampai jumpa!")
        exit()
    else:
        print("Menu tidak tersedia")

def show_contact():
    if(len(contacts_name) <= 0):
        print("Tidak ada data!")
    else:
        print("Daftar Kontak:")
        for indeks in range(len(contacts_name)):
            print("[%d] %s %s" % (indeks+1, "Nama       :", contacts_name[indeks]))
            print("    No Telepon :", contacts_phone[indeks])

def create_contact():
    nama = input("Nama : ")
    contacts_name.append(nama)
    telpon = input("No Telepon : ")
    contacts_phone.append(telpon)
    print("Kontak berhasil ditambahkan")

if __name__ == "__main__":
    while(True):
        show_menu()