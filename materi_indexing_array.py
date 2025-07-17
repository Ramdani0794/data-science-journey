import numpy as np
array_1d = np.array([10,20,30,40,50])

print(array_1d[0]) # mengeksekusi nilai array index 0 yaitu 10 (indexing)
print(array_1d[0:5]) #mengeksekusi nilai array dari index 0 sampai 5 (slicing)

array_2d = np.array([ [10,20,30],[40,50,60],[70,80,90] ]) #array du dimensi ([ [baru diisi angka],[lanjut baris kedua],[lanjut baris ketiga] ])
print(array_2d)

print(array_2d[0][0]) #mengeksekusi baris nol kolom nol
print(array_2d[1][2]) #mengeksekusi baris satu kolom kedua
print(array_2d[0,0:3]) #mengeksekusi baris nol kolom nol sampai tiga

array_sebelum = np.arange(1,10)
array_sesudah = array_sebelum.reshape((3,3)) # reshape merubah bentuk array dari yang hanya satu range menjadi bentuk matrix 3x3
print(array_sebelum)
print(array_sesudah)