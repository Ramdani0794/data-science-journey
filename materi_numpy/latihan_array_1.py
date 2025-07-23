import numpy as np

array_nilai = np.array([ (85,90,78),
                         (70,75,80),
                         (92,88,95),
                         (65,70,68) ])

print(array_nilai)
#print(f"nilai mahasiswa pertama\n{array_nilai[0]}")
#print(f"nilai mata kuliah kedua\n{array_nilai[:, 1]}")
#print(f"nilai mata kuliah ketiga, mahasiswa kedua\n{array_nilai[1,2]}")   [0:4,0]
#print(f"nilai mahasiswa satu dan dua, semua mata kuliah\n{array_nilai[0:2, :]}")
#
#rata_rata_nilai = np.mean(array_nilai)
#rata_rata_nilai_mahasiswa = np.mean(array_nilai,axis=1)
#rata_rata_nilai_matakuliah = np.mean(array_nilai,axis=0)
#nilai_tertinggi = np.max(array_nilai)
#nilai_terendah = np.min(array_nilai,axis=0)
#
#print(f"rata-rata nilai \n{rata_rata_nilai}")
#print(f"rata-rata nilai mahasiswa \n{rata_rata_nilai_mahasiswa}")
#print(f"rata-rata nilai matakuliah \n{rata_rata_nilai_matakuliah}")
#print(f"nilai tertinggi \n{nilai_tertinggi}")
#print(f"nilai terendah \n{nilai_terendah}")
#
#nilai_bonus = array_nilai + 5
#penyesuaian_nilai = array_nilai * 1.1
# 
#print(f"penambahan bonus nilai absen 5 point \n{nilai_bonus}")
#print(f"nilai yang sudah disesuaikan \n{penyesuaian_nilai}")

total_nilai = np.sum(array_nilai,axis=1)
nilai_matakuliah_pertama = array_nilai[:,0]
nilai_lulus_80_matakuliah = nilai_matakuliah_pertama[nilai_matakuliah_pertama > 80]
print(f"total nilai masing masing mahasiswa \n{total_nilai}")
print(nilai_matakuliah_pertama)
print(nilai_lulus_80_matakuliah)