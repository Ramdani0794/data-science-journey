# List
daftar_belanja = ["Mie","Terigu","Gula","Garam","Roti"]
print(daftar_belanja[0])
print(daftar_belanja[-1])

daftar_belanja.append("Minyak")
daftar_belanja.append("Kecap")
daftar_belanja.insert(1,"Susu")
daftar_belanja.remove("Roti")
daftar_belanja.sort()

for item in daftar_belanja:
    print(item)

# Tuple
koordinat_gps = (850,9.60)
print(koordinat_gps[0])
print(koordinat_gps[1])

# Set
angka_acuan = [1,2,2,3,4,5,1]
angka_unik = angka_acuan.copy()
angka_unik = set(angka_unik)

set_a = {1,2,3}
set_b = {3,4,5}
union = set_a.union(set_b)
intersection = set_a.intersection(set_b)

print(angka_acuan)
print(angka_unik)
print(union)
print(intersection)

# Dictionary
profil_teman = {
    'nama' : "maman",
    'usia' : 20,
    'pekerjaan' : "Programmer",
    'hobi' : "Futsal"
}

print(profil_teman["nama"])
profil_teman["pekerjaan"] = "Wiraswasta"
print(profil_teman['pekerjaan'])
profil_teman['email'] = "mmn4445@gmail.com"
del profil_teman['hobi']

for key in profil_teman.keys():
    print(key)

for value in profil_teman.values():
    print(value)

for item in profil_teman.items():
    print(item)

# Dictionary tugas
data_mahasiswa = {
    "MHS001" : {'nama' : "Adi", 'jurusan' : "Teknik Informatika", 'nilai_mtk' : 85, 'nilai_fisika' : 78},
    "MHS002" : {'nama' : "Bella", 'jurusan' : "Sistem Informasi", 'nilai_mtk' : 90, 'nilai_fisika' : 88},
}

data_mahasiswa['MHS003'] = {'nama' : "Adit", 'jurusan' : "Teknik Mesin", 'nilai_mtk' : 82, 'nilai_fisika' : 90}
print(data_mahasiswa["MHS002"]['jurusan'])
print(data_mahasiswa["MHS001"]['nilai_fisika'])

data_mahasiswa["MHS003"]['nilai_mtk'] = 95
print(data_mahasiswa["MHS003"]['nilai_mtk'])

for mahasiswa in data_mahasiswa.values():
    print(mahasiswa['nama'], mahasiswa['jurusan'])

print(len({"a":1, "b":2, "c":3}))