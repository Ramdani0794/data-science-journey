import numpy as np
# array berulang
array_1d = np.array([1,5,9,13,17])
array_2d = np.array([ (15,20,25,30),(10,15,20,25) ])
arange_1d = np.arange(5,16,1)

print(array_1d)
print(array_2d)
print(arange_1d)

#indexing dan slicing berulang
data_sensor = np.array([15,18,12,20,14,25,17])
print("\n")
print(data_sensor[0])
print(data_sensor[-1])
print(data_sensor[0:3])
print(data_sensor[2:5])

matrix_data = np.array([ (10,20,30),(40,50,60),(70,80,90) ])
print("\n")
print(matrix_data[2][0])
print(matrix_data[0][0:3])
print(matrix_data[0][1])
print(matrix_data[0:2,1:3])

#latihan operasi matematika berulang
array_penjualan = np.array([100,150,200])
array_biaya = np.array([70,100,120])

tambah = array_penjualan + array_biaya
kurang = array_penjualan - array_biaya
diskon = array_penjualan * 1.1
kuadrat = array_biaya **3

print("\n")
print(tambah)
print(kurang)
print(diskon)
print(kuadrat)

#latihan fungsi agresi
data_uji = np.array([ (5,8,2),(9,1,7),(3,6,4)])
max_data = np.max(data_uji)
mean_data = np.mean(data_uji,axis=1)
sum_data = np.sum(data_uji,axis=0)
min_data = np.min(data_uji)

print("\n")
print(max_data)
print(mean_data)
print(sum_data)
print(min_data)