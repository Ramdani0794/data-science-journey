import numpy as np
a = np.floor(np.random.randn(2,3)*10)
print(a)

print(f"nilai max dari a adalah {a.max()}")
print(f"nilai max a ada pada index ke- {a.argmax()}") # args max adalah index dari max
print(f"nilai min dari a adalah {a.min()}")
print(f"nilai min a ada pada index ke- {a.argmin()}") # args max adalah index dari max

print("mengurutkan nilai dari a")
print(np.sort(a))
print(np.argsort(a)) #mengurutkan nilai dari yang terkecil sampai yang terbesar berdasarkan index

# multitype sort

dtipe = [('nama','S10'),('tinggi',int)]
data = [
    ("ucup",150),
    ("nanang",155),
    ("agus",160),
    ("maman",175)
]

b = np.array(data, dtype= dtipe)

print(b)
print(np.sort(b, order= 'nama'))
print(np.sort(b, order= 'tinggi'))