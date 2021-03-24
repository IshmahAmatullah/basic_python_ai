# nama = []
# nomor = []
# z = 0

# n = int(input("Jumlah Kontak :"))
# for x in range (n):

# def show_menu():
#     print(" Menu ")
#     print("1. Daftar Kontak")
#     print("2. Tambah Kontak")
#     print("3. Keluar")
    
#     menu = input("Pilih menu :")
#     print("\n")
    
#     if menu == 1:
#         show_data()
#     elif menu == 2:
#         insert_data()
#     elif menu == 3:
#         print("Program selesai, sampai jumpa!")
#     else:
#         print("Menu tidak tersedia")
#     return show_menu()

#     def show_data():

import csv
import os

csv_filename = 'contacts.csv'

def show_menu():
    print("------Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print("----------------")
    selected_menu = input("Pilih menu: ")

    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        create_contact()
    elif(selected_menu == "3"):
        print("Program selesai, sampai jumpa!")
        exit()
    else:
        print("Menu tidak tersedia")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def show_contact():
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)
        
    if(len(contacts) > 0):
        labels = contacts.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in contacts:
            print(f'{data[0]} \t {data[1]} \t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()

def create_contact():
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['Nama', 'Telepon']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        nama = input("Nama : ")
        telepon = input("No. Telepon : ")

        writer.writerow({'Nama' : nama, 'Telepon' : telepon})
        print("Kontak berhasil ditambahkan")
        
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()