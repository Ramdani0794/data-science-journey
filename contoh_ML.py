import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Program Klasifikasi Bunga Iris Sederhana ---")
print("Belajar Machine Learning dengan Scikit-learn")

# 1. Memuat Dataset Iris
print("\n1. Memuat Dataset Iris...")
iris = load_iris()
X = iris.data  # Fitur (panjang kelopak, lebar kelopak, dll.)
y = iris.target # Target (spesies bunga Iris)
feature_names = iris.feature_names
target_names = iris.target_names

# Tampilkan beberapa baris data pertama dan informasi dasar
df_iris = pd.DataFrame(X, columns=feature_names)
df_iris['species'] = y
print("5 baris pertama dari dataset Iris:")
print(df_iris.head())
print("\nNama fitur:", feature_names)
print("Nama spesies (target):", target_names)
print(f"Jumlah sampel: {X.shape[0]}, Jumlah fitur: {X.shape[1]}")

# 2. Memisahkan Data Latih dan Data Uji
# Data akan dibagi secara acak 80% untuk pelatihan dan 20% untuk pengujian
print("\n2. Memisahkan Data Latih (80%) dan Data Uji (20%)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Jumlah data latih: {X_train.shape[0]} sampel")
print(f"Jumlah data uji: {X_test.shape[0]} sampel")

# 3. Memilih dan Melatih Model Machine Learning (K-Nearest Neighbors)
print("\n3. Memilih dan Melatih Model K-Nearest Neighbors (KNN)...")
# KNN adalah algoritma klasifikasi sederhana yang efektif.
# 'n_neighbors' adalah parameter penting, bisa diubah-ubah!
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

print("Model KNN berhasil dilatih!")

# 4. Membuat Prediksi
print("\n4. Membuat Prediksi pada Data Uji...")
y_pred = knn_model.predict(X_test)
print("Prediksi berhasil dibuat.")

# 5. Evaluasi Model
print("\n5. Evaluasi Kinerja Model...")

# Akurasi: Persentase prediksi yang benar
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi Model: {accuracy:.2f}") # Tampilkan dalam 2 angka desimal

# Laporan Klasifikasi: Menunjukkan presisi, recall, f1-score untuk setiap kelas
print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Matriks Konfusi: Menunjukkan jumlah prediksi benar dan salah untuk setiap kelas
print("\nMatriks Konfusi:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualisasi Matriks Konfusi (lebih mudah dibaca)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=target_names, yticklabels=target_names)
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.title('Matriks Konfusi')
plt.show()

print("\n--- Program Selesai ---")

print("\nSelamat! Anda telah menjalankan program Machine Learning sederhana!")
print("Sekarang, mari kita pelajari lebih lanjut dan Anda bisa mulai mengulik program ini.")