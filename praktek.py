# manajemen kontak telepon
daftar_kontak = {}

def tambah_kontak():
    nama = input("Masukan nama kontak: ")
    nomor = input("Masukan nomor kontak: ")
    daftar_kontak[nama] = nomor
    print(f"Kontak '{nama} berhasil ditambahkan")

def lihat_semua_kontak():
    print(5*"-"+"Daftar Kontak"+"-"*5)
    if not daftar_kontak:
        print("Tidak ada kontak tertera")
    else:
        for nama, nomor in daftar_kontak.items():
            print(f"Nama : {nama}, Nomor : {nomor}")

def cari_kontak():
    nama_dicari = input("Masukan nama kontak: ")
    if nama_dicari in daftar_kontak:
        nomor_ditemukan = daftar_kontak[nama_dicari]
        print(f"nomor telepon '{nama_dicari}' : {nomor_ditemukan}")
    else:
        print("nomor tidak ditemukan")

def hapus_kontak():
    nama_hapus = input("masukan nama kontak yang ingin dihapus: ")
    if nama_hapus in daftar_kontak:
        del daftar_kontak[nama_hapus]
        print(f"kontak '{nama_hapus}' berhasil dihapus")
    else:
        print(f"kontak '{nama_hapus}' tidak ditemukan")

def menu_program():
    while True:
        print("\n--- Menu Kontak ---")
        print("1. Tambah kontak")
        print("2. Lihat Daftar Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Exit")

        pilihan = input("Pilih Menu: ")
        if pilihan == "1":
            tambah_kontak()
        elif pilihan == "2":
            lihat_semua_kontak()
        elif pilihan == "3":
            cari_kontak()
        elif pilihan == "4":
            hapus_kontak()
        elif pilihan == "5":
            print("Terimakasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid silahkan pilih menu lagi")

if __name__ == "__main__":
    menu_program()