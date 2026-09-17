angka1_3015 = int(input("Input angka-1: "))
angka2_3015 = int(input("Input angka-2: "))

print("\nNilai awal angka1_3015 =", angka1_3015)
print("Nilai angka2_3015 =", angka2_3015)

#Assignment biasa
hasil_3015 = angka1_3015
print("\nOperator Assignment Biasa (=)")
print("Hasil =", hasil_3015)

#Assignment penjumlahan
hasil_3015 = angka1_3015
hasil_3015 += angka2_3015
print("\nOperator Assignment Penjumlahan (+=)")
print("Hasil =", hasil_3015)

#Assignment pengurangan
hasil_3015 = angka1_3015
hasil_3015 -= angka2_3015
print("\nOperator Assignment Pengurangan (-=)")
print("Hasil =", hasil_3015)

#Assignment perkalian
hasil_3015 = angka1_3015
hasil_3015 *= angka2_3015
print("\nOperator Assignment Perkalian (*=)")
print("Hasil =", hasil_3015)

#Assignment pembagian, pembagian bulat, sisa bagi
if angka2_3015 !=0:
    hasil_3015 = angka1_3015
    hasil_3015 /= angka2_3015
    print("\nOperator Assignment Pembagian (/=)")
    print("Hasil =", hasil_3015)
    #Operator tambahan
    hasil_3015 = angka1_3015
    hasil_3015 //= angka2_3015
    print("\nOperator Assignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_3015)

    hasil_3015 = angka1_3015
    hasil_3015 %= angka2_3015
    print("\nOperator Assignment Sisa Bagi (%=)")
    print("Hasil =", hasil_3015)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

#Operator tambahan: Assignment perpangkatan
hasil_3015 = angka1_3015
hasil_3015 **= angka2_3015
print("\nOperator Assignment Perpangkatan (**=)")
print("Hasil =", hasil_3015)