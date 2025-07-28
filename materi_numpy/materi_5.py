import numpy as np

#manipulasi matrix 
a = np.array([(1,2,3),
              (4,5,6)])

trnaspose_a = np.transpose(a) # .transpose untuk melakukan transpose matrix
ravel_a = a.ravel()  # .ravel untuk menjadikan bentuk 1 baris
reshape_a = a.reshape(3,2) # merubah bentuk a tanpa merubah data a, maksudnya adalah bentuk a 2x3 akan tetap dipertahankan
resize_a = a.resize(3,2) # ini merubah nilai a yang tadinya 2,3 menjadi sesuai kemauan kita dicontoh diubah ke 3,2 maka tidak perlu memanggil resize_a cukup a saja karena nilainya sudah diubah

print(f"ini adalah matrix {a.shape} :\n{a}")  #.shape untuk melihat bentuk dari matrix
print(f"ini adalah matrix {trnaspose_a.shape} :\n{trnaspose_a}")
print(a.T) # bisa seperti ini untuk melakukan transpose hanya saja berlaku hanya untuk dibagian print
print(a.transpose()) # atau bisa melakukan seperti ini

print(f"ini adalah matrix {ravel_a.shape} :\n{ravel_a}")
print(f"ini adalah matrix {reshape_a.shape} :\n{reshape_a}")
print(f"ini adalah matrix {a.shape} :\n{a}") # ini tida perlu memanggil resize a karena akan menghasilkan none 


# latihan
b = np.array([(4,5),
              (7,8),
              (1,2)])

print(f"ini adalah matrix dengan bentuk {b.shape}\n{b}")
print(f"ini adalah ubah bentuk dari matrix b dengan bentuk {b.shape}\n{b.reshape(2,3)}")

b.resize(1,6) # jika melebihi dari nilai awal maka sisa akan di isi oleh nilai nol 0
print(b)