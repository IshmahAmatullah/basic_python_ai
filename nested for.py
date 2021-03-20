"""i = 0-1
j = 0-2
k = 0-2

i = 0:
    j = 0:
        k = 0
        k = 1
        k = 2
    j = 1:
        k = 0
        k = 1
        k = 2
    j = 2
        k = 0
        k = 1
        k = 2
i = 1:
    j = 0
    j = 1
    j = 2
i = 2:
    j = 0
    j = 1
    j = 2"""

for i in range(2):
    for j in range(3):
        for k in range (2):
            print("{}:{}:{}".format(i,j,k), end=" ")
        print()
print("Hello", end = " ")
print("World")

nama = []
matkul = []
z = 0

n = int(input("Jumlah Mahasiswa : "))
m = int(input("Jumlah Matkul : "))
for x in range(n):
    name = str(input("Nama : "))
    nama.append(name)
    for y in range (m):
        matakuliah = str(input("Matakuliah : "))
        matkul.append(matakuliah)

for x in range (n):
    print(x+1, nama[x] )
    for y in range (m):
        print("--->", matkul[z])
        z += 1

matkul = [[1,2,3,],[4,5,6]]
print(matkul[1][2])

for x in range(1,15):
    for y in range(1,x+1):
        print(y, end=",")
    print()

"""x = 3
y = 1
1
12"""