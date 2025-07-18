import pandas as pd
s =pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s)
print(s['b'])

data = {
    'nama' : ["andi","budi","maman","nanang"],
    'usia' : [25,30,22,35],
    'kota' : ["jakarta","bandung","surabaya","medan"]
}

df = pd.DataFrame(data)
print(df)