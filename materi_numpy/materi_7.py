import numpy as np

# cara advance membuat array dalam numpy
a = np.array([(1,2,3),
              (4,5,6)], dtype=float)

b = np.array([0,1,2,3,4,5,6,7,8,9])
print(f"array biasa \n{b**2}")

def kuadrat(baris,kolom):
    return kolom **2

def jumlah(baris,kolom):
    return baris + kolom

b = np.fromfunction(kuadrat, (1,10), dtype=int) # tidak boleh lupa soal ini
# isi dari np.fromfunction(fungsi, ukuran matrix, tipe data)
c = np.fromfunction(jumlah,(6,6), dtype=int)

# menggunakan iterebel
angka = (x*x for x in range(10)) # hasil ini sama dengan array dengan function
d = np.fromiter(angka, dtype=int)

# multitype array 
"""isi dari multitype array bisa berupa stirng,integer,float atau bahkan boolean"""
dtipe = [('nama','S255'), ('tinggi',int)]
data = [
    ("nanang", 160),
    ("maman", 190),
    ("dadang", 175)
]

e = np.array(data,dtype= dtipe)

print(kuadrat(5,5))
print(f"array dengan function\n{b}")
print(f"array baris + kolom \n{c}")
print(f"array dengan iterebel \n{d}")
print(f"multitype array\n{e}")