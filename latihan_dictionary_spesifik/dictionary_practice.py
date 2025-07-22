profil_pengguna = {
    'nama' : "Muhammad Ramdani",
    'usia' : 21,
    'kota' : "Tangerang",
}
profil_pengguna['usia'] = 25
print(profil_pengguna)

buku_favorit = {
    'Harry Potter' : "J.K. Rowling",
    'Laskar Pelangi' : "Andrea Hirata",
    'Bumi Manusia' : "Pramoedya",
    'Kuala Kumal' : "Raditiya Dika"
}

buku_favorit.pop('Bumi Manusia')
for i in buku_favorit:
    print(i)

     
print(buku_favorit)
print(buku_favorit['Harry Potter'])
print(buku_favorit['Laskar Pelangi'])
