teori = int(input("skor normatif :"))
praktek = int(input("skor adaptif :"))
if teori>=70 and praktek>=70:
    print("Selamat, Anda lulus!")
elif teori>=70 and praktek<70:
    print("Anda harus mengulang ujian praktek")
elif teori<70 and praktek>=70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")