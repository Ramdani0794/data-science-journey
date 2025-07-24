import numpy as np
# array biasa
a = np.array([1,2,3,4,5,6,7,8,9])

# Array dengan range (arange)
b = np.arange(1,9,2) # 3s (start,stop,step)

# array dengan linspace(linspace) atau rentang jarak yang sesuai input
c = np.linspace(2,10,5) #(start,stop,rentang jarak antar angka yang sama)

# array multidimensi ([()()])
d = np.array([(1,2,3,4,5),(6,7,8,9,10)])

# array matrixs 0
e = np.zeros([2,2])

# array matrixs 1 
f = np.ones([2,2])

#matrix identits
g = np.identity(4)
h = np.eye(4)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
