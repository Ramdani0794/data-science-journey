inventaris = [
   {'nama_produk' : "Buku", 'harga' : 5000, 'stok' : 100},
   {'nama_produk' : "Pulpen", 'harga' : 2500, 'stok' : 200},
   {'nama_produk' : "Pensil", 'harga' : 2000, 'stok' : 150}
]

def tampilan_inventaris(data_inventaris):
    if not data_inventaris:
        print("Inventaris kosong.")

    print("{:<20} {:<15} {:<10}".format("Nama Barang", "Harga Barang", "Stok Barang"))
    print("-"*50)
    
    for item in data_inventaris:
        print("{:<20} {:<15} {:<10}".format(item['nama_produk'], item['harga'], item['stok']))
tampilan_inventaris(inventaris)

def tambah_produk(data_inventaris,nama,harga,stok):
    