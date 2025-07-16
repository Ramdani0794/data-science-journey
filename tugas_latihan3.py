daftar_buku = ["menanam","memakan","menghias","mengambil"]

print(daftar_buku[0])
print(daftar_buku[-1])

daftar_buku.append("memasak")
daftar_buku.append("melihat")

print(daftar_buku)


data_produk = {
    'laptop' : {"harga" : 1200000, "stok" : 10},
    'mouse' : {"harga" : 100000, "stok" : 5},
    'keyboard' : {"harga" : 500000, "stok" : 20}
}

print(data_produk["mouse"]["harga"])
data_produk["keyboard"]["stok"] = 15
print(data_produk["keyboard"]["stok"])