bilangan_numerik = int(input("masukkan angka (hanya untuk 1-10): "))

if bilangan_numerik > 0 and bilangan_numerik < 4:
    romawi = "I" * bilangan_numerik
    print(romawi)
elif bilangan_numerik == 4:
    print("IV")
elif bilangan_numerik > 4 and bilangan_numerik < 9:
    romawi = "V" + ("I" * (bilangan_numerik - 5))
    print(romawi)
elif bilangan_numerik > 8 and bilangan_numerik < 11:
    romawi = "I" * (10 - bilangan_numerik) + "X"
    print(romawi)
else:
    print("melebihi kapasitas maksimum")