# Rekap minggu pertama (variable dan tipe data, operasi aritmatika, perbandingan logika, input dari pengguna)
# 1. variable dan tipe data
nama_depan = "Muhammad"
nama_belakang = "Ramdani"
tahun_lahir = 2004
tinggi_badan_cm = 169.05
sudah_makan = True

print(nama_depan,type(nama_depan))
print(nama_belakang,type(nama_belakang))
print(tahun_lahir,type(tahun_lahir))
print(tinggi_badan_cm,type(tinggi_badan_cm))
print(sudah_makan,type(sudah_makan))

print("\n")
# operasi matematika
uang = 20000
apel = 5
jeruk = 3
harga_apel = 2500
harga_jeruk = 3000

total_buah = apel + jeruk
total_harga_apel = apel * harga_apel
total_harga_jeruk = jeruk * harga_jeruk
total_harga_buah = total_harga_apel + total_harga_jeruk
kembalian = uang - total_harga_buah

print(f"Total buah = {total_buah}")
print(f"Total harga apel = {total_harga_apel}")
print(f"Total harga jeruk = {total_harga_jeruk}")
print(f"Total harga buah = {total_harga_buah}")
print(f"Sisa kembalian = {kembalian}")

print("\n")
#perbandingan dan logika
print(10 > 7)
print("apel" == "Apel")
print(5 > 3 and 10 < 8)
print(2 == 2 or 7 != 7)
print(not 100 > 50)

print("\n")
#input dari pengguna
nama_pengguna = input("Masukan nama: ")
usia_pengguna = int(input("Masukan usia: "))

print(f"Halo {nama_pengguna}! kamu berusia {usia_pengguna} tahun.")