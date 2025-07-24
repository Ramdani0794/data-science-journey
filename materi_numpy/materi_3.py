import numpy as np
# array 
a = np.arange(10) **2

print(a)

# indexing
print(f"elemen pertama dari a = {a[0]}") # artinya index nol dalam array
print(f"elemen terakhir dari a = {a[-1]}") #artinya index -1 atau dimulai dari paling akhir

#scilling
print(f"elemen dari 5 sampai 7 = {a[4:7]}") # artinya mengambil item array antara dimulai index 4 sampai index 7-1 atau satu angka sebelum index 7 yaitu index 6
print(f"elemen dari pertama sampai 5 = {a[0:5]}")
print(f"elemen dari 5 sampai akhir = {a[4:]}")

#iterasi
for angka in a:
    print(angka)