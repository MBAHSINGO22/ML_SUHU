
Celcius = float(input('Masukkan suhu dalam Celcius: '))

print("Pilih jenis konversi:")
print("1. Konversi ke Fahrenheit")
print("2. Konversi ke Reamur")
print("3. Konversi ke Kelvin")
pilihan = int(input("Masukkan pilihan (1/2/3): "))

if pilihan == 1:
    Fahrenheit = (Celcius * 9/5) + 32
    print(Celcius, "Celcius adalah", Fahrenheit, "Fahrenheit")
elif pilihan == 2:
    Reamur = Celcius * 4/5
    print(Celcius, "Celcius adalah", Reamur, "Reamur")
elif pilihan == 3:
    Kelvin = Celcius + 273
    print(Celcius, "Celcius adalah", Kelvin, "Kelvin")
else:
    print("Pilihan tidak valid.")