import numpy as np

# perbandingan atau perbedaan antara array list dan list biasa
a = np.array([1,2,3,4,5,6]) # array tidak akan mengeluarkan pembatas koma(,) nya
b = [1,2,3,4,5,6] # sedangkan list biasa akan membawa koma pada hasil akhir

a += 1
b += [1]
print(f"\n{a}")
print(f"\n{b}")