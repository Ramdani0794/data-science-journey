import numpy as np
# membuat array dasar

deret_ganjil = np.arange(1,20,2)
print(deret_ganjil)

matriks_identitas = np.eye(3)
print(matriks_identitas)

np.random.seed(5)
data_acak = np.random.randint(1,100,size=(4,5))
print(data_acak)

#mengakses dan merubah bentuk array
print(data_acak[1][2])
print(data_acak[-1])
print(data_acak[0:4,0]) # [0:4,0] artinya mengambil seluruh kolom index nol didalam baris index nol sampai 4
print(data_acak[1:3,2:5]) #[1:3,2:5] artinya mengambil baris 1 sampai 2, dan mengambil kolom 2 sampai 4

array_deret = deret_ganjil.reshape(5,2)
print(array_deret)

#operasi matematika
array_a = np.array([(1,2),(3,4)])
array_b = np.array([(5,6),(7,8)])

hasil = array_a + array_b
kali = array_a * array_b
kali_10 = array_a *10

print(hasil)
print(kali)
print(kali_10)

#fungsi agresi
data_penjualan_kota = np.array([(120,150,130),(200,180,220),(90,110,100)]) #baris = kota, kolom = penjualan
print(np.sum(data_penjualan_kota))
print(np.mean(data_penjualan_kota,axis=0))
print(np.sum(data_penjualan_kota,axis=1))
print(np.min(data_penjualan_kota))
print(np.max(data_penjualan_kota))