import numpy as np

#perkalian matrix 
"""perkalian matrix adalah operasi biner yang menghasilkan matrix dari dua matrix.
   untuk bisa mengalikan dua matrix, jumlah kolom pada matrix harus sama dengan matrix satu dan yang lain
   dalam python maka digunakan rumus ndarray atau numerical dimension array contoh: np.dot dan np.matmul """
# penggunaan
a = np.array([(11,20),
              (2,5)])

b = np.array([(5,2),
              (3,2)])

""" ini link dari gambaran tentang perkalian matrix
https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtLzdkNWUxOTY4NzI5NTQ1ODBiNzJhNDA4YmNkYTI1ZDg5X0JCQTcxNzYyLTEyRTAtNDJFMS1CMzI0LTVCMTMxRjQyNEUzRF9hMzBjNmQ4MS0zYjRjLTRlOGEtOTkwNC0zYzcxMDdhMDA3Zjg="""

print(f"{a}\n{b}")
print(np.dot(a,b))
print(np.matmul(a,b))


# biar gk pusing arti kolom harus sama
c = np.array([(3,5,6),
              (5,6,4)])

d = np.array([(2,3),
              (1,1),
              (4,2)])

e = c.dot(d)

print(c)
print(d)
print(e)