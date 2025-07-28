import numpy as np

#stacking matrix hstack untuk horizontal dan vstack untuk vertikal
a = np.array([(1,2,3)])
b = np.array([(4,5,6)])

hstack = np.hstack((a,b))
vstack = np.vstack((a,b))

print(hstack)
print(vstack)

# stacking dalam matrix 
c = np.array([(1,2,3),
              (4,5,6)])

d = np.array([(7,8,9),
              (1,2,3)])

cmat = np.hstack((c,d))
dmat = np.vstack((c,d))

print(c)
print(d)
print(cmat)
print(dmat)