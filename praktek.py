# manajemen kontak telepon
daftar_kontak = []
id_kontak = 1

while True:
    kontak_baru = input("Masukan nama kontak: ")
    nomor_baru = input("Masukan nomor kontak: ")

    kontak_telepon = {
        'id' : id_kontak, 'nama' : kontak_baru, 'nomor' : nomor_baru       
    }

    daftar_kontak.append(kontak_telepon)
    id_kontak += 1

    islanjut = input("apakah anda ingin memasukan nomor lagi (y/n)? ")
    if islanjut.lower() == "n":
        print("Program berakhir")
        break

print(5*"-"+"Daftar Kontak"+"-"*5)
if not daftar_kontak:
    print("Tidak ada kontak tertera")
else:
    for item in daftar_kontak:
        print(f"ID: {item['id']}, Nama: {item['nama']}, Nomor: {item['nomor']} ")

#for item in kontak_telepon.values():
#        print(item)