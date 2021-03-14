import math as m
r = float(input("jari-jari lingkaran "))
L = r**(2)*m.pi
Luas = "%.2f" % L

prompt = "Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r, "%.2f" % L)
print(prompt)
call = "Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r, Luas)
print(call)

a = "Luas lingkaran dengan jari-jari"
b = "adalah"
print(a, r, "cm", b, Luas, "cm\u00b2")
print(a, r, "cm", b, "%.2f" % L, "cm\u00b2")