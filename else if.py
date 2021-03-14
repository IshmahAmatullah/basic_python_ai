a = 200
b = 33
if b > a:
    print("b lebih besar dari a")
elif b == a:
    print("a dan b adalah sama")
else: 
    print("b lebih kecil dari a")

c=200
d=100
e=50
if c>d and d>e:
    print("e lebih kecil dari c dan d")
else:
    print("e lebih besar dari c dan d")

print(c>d and d>e)
print(c<d or d>e)
print(not c>d)