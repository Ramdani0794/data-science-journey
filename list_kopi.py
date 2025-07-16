daftar_nama_kopi = ["Gula Aren", "Latte", "Matcha", "Americano", "Espresso"]
detail_espresso = {
    'nama' : "Espresso",
    'harga' : 28000,
    'kategori' : "Kopi Hitam",
    'stok' : 15
}

cek_list = daftar_nama_kopi[2]
print(cek_list)
harga = detail_espresso["harga"]
print(harga)
stok = detail_espresso["stok"]
print(stok)
stok = detail_espresso["stok"] = 12
print(stok)

daftar_nama_kopi.append("Flat White")
print(daftar_nama_kopi)