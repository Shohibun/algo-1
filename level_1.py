angka_desimal = float(input("masukkan angka desimal (dua digit dibelakang koma): "))
Bilangan1 =(angka_desimal * 10) - ((angka_desimal * 10) // 1)

if Bilangan1 < 0.5:
    pembulatan = (((angka_desimal * 10)//1)/10)
    print(pembulatan)
else:
    pembulatan = ((((angka_desimal * 10)//1)+1)/10)
    print(pembulatan)
