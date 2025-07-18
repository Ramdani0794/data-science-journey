# fungsi agresi sum,mean,min,max,std(standar deviasi)
import numpy as np
data_suhu = np.array([ (2,3,4,5,6,7,8,9) ])
rata_suhu = np.mean(data_suhu)
min_suhu = np.min(data_suhu)
max_suhu = np.max(data_suhu)
total_suhu = np.sum(data_suhu)

print(rata_suhu)
print(min_suhu)
print(max_suhu)
print(total_suhu)

matrix = np.array([ (80,90,70),(75,85,95) ]) #disesuaikan dengan index kolom misal 80 + 75 
mean_matrix = np.mean(matrix, axis=0) # axis= 0 artinya operasi dilakukan secara vertikal (perkolom) sedangkan jika axis=1 maka operasi dilakukan dengan secara horizontal (perbaris)
mean_axis1 = np.mean(matrix, axis=1) # axis= 0 artinya operasi dilakukan secara vertikal (perkolom) sedangkan jika axis=1 maka operasi dilakukan dengan secara horizontal (perbaris)
print(f"\nRata-rata per kolom : {mean_matrix}")
print(f"\nRata-rata per kolom : {mean_axis1}")