x1 = int(input("masukkan koordinat x1: "))
y1 = int(input("masukkan koordinat y1: "))
x2 = int(input("masukkan koordinat x2: "))
y2 = int(input("masukkan koordinat y2: "))
jarak1 = (x1-x2) + (y1-y2)
if jarak1 > 0:
    print("jarak Manhattan: ", jarak1)
else:
    jarak1 *= -1
    print("jarak Manhattan: ", jarak1)