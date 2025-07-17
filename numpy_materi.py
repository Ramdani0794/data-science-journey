import numpy as np

list = [1,2,3,4,5,6,7,8,9] # list biasa
array_list = np.array(list) #array dari list hasil print array tidak akan menggunakan , (koma)
array_nol = np.zeros((2,2)) #array zeros adalah kumpulan array dengan bilangan nol ((2,2)) ini artinya array memiliki 2 baris dan dua kolom 2 di depan artinya baris dan 2 dibelakang artinya kolom
array_satu = np.ones((4,4)) #array ones adalah array dengan angka 1 sama hal dangan array zeros
array_dua = np.full((2,2),4) #array full berisi nilai array yang mau kita input ((2,2),4) 2,2 disini adalah kolom dan baris dan 4 adalah angka yang akan dibuat array
array_range = np.arange(0,9,3) #arange adalah array range konsep nya sama yaitu 3s (start,stop,step)
linspacce = np.linspace(1,10,4) # linspace menciptakan kondisi dimana jumlah array memiliki jarak yang sama dari satu bilangan ke bilangan lainnya



print(list)
print(array_list)
print(array_nol)
print(array_satu)
print(array_dua)
print(array_range)
print(linspacce)
print(type(array_list))