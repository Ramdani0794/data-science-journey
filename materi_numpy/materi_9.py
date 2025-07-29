import numpy as np

# perkalian vektor dot dan cross
a = np.array([1,3])
b = np.array([2,1])

c = a.dot(b) # perkalian vektor serupa dengan matriks
print(c)

# perkalian cross
a2 = np.array([1,2,0])
b2 = np.array([2,1,0])

c2 = np.cross(a2,b2)
c3 = np.cross(b2,a2)

print(c2)
print(c3)