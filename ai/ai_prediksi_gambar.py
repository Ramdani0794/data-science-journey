import cv2 # OpenCV
import numpy as np
import tensorflow as tf
from keras.models import load_model
import os # Untuk memeriksa file

print("--- Program Deteksi Wajah & Prediksi Ekspresi Sederhana ---")
print("Akan menggunakan kamera laptop Anda.")

# --- Bagian 1: Deteksi Wajah ---
# Pastikan Anda memiliki file haarcascade_frontalface_default.xml
# Anda bisa mengunduhnya dari: https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_frontalface_default.xml
# Letakkan di direktori yang sama dengan script Python ini.
face_cascade_path = 'haarcascade_frontalface_default.xml'

if not os.path.exists(face_cascade_path):
    print(f"ERROR: File '{face_cascade_path}' tidak ditemukan.")
    print("Silakan unduh dari https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_frontalface_default.xml")
    print("Dan letakkan di direktori yang sama dengan script ini, lalu jalankan lagi.")
    exit()

face_cascade = cv2.CascadeClassifier(face_cascade_path)
print(f"Berhasil memuat Haar Cascade untuk deteksi wajah dari '{face_cascade_path}'.")

# --- Bagian 2: Prediksi Ekspresi (Menggunakan Model Pra-terlatih) ---
# CATATAN: Anda perlu mengunduh model ekspresi Keras (.h5 atau saved_model) secara terpisah!
# Model yang direkomendasikan dan diasumsikan di sini adalah dari FER2013, dengan input 64x64 grayscale:
# Link: https://github.com/justinsy/fer2013/raw/master/emotion_model.h5
# Unduh model tersebut dan letakkan di folder yang sama dengan script ini.

emotion_model_path = 'emotion_model.h5' # Pastikan nama ini sesuai dengan file yang Anda simpan!
# Urutan label ini HARUS SESUAI dengan urutan output dari model yang Anda unduh.
# Untuk model FER2013 (justinsy), urutan umumnya adalah:
emotion_labels = ['Marah', 'Jijik', 'Takut', 'Senang', 'Sedih', 'Terkejut', 'Netral']

emotion_model = None # Inisialisasi model ekspresi sebagai None

if os.path.exists(emotion_model_path):
    try:
        emotion_model = tf.keras.models.load_model(emotion_model_path)
        print(f"Berhasil memuat model ekspresi dari '{emotion_model_path}'.")
        # Optional: Print model summary to verify input shape expectations
        # emotion_model.summary()
    except Exception as e:
        print(f"ERROR: Gagal memuat model ekspresi. Pastikan ini adalah file model Keras yang valid (.h5).")
        print(f"Detail error: {e}")
        emotion_model = None
else:
    print(f"PERINGATAN: Model ekspresi '{emotion_model_path}' tidak ditemukan.")
    print("Prediksi ekspresi tidak akan berfungsi tanpa model yang diunduh.")
    print("Silakan unduh model pra-terlatih (misalnya .h5) dan letakkan di sini.")

# Inisialisasi kamera
print("\nMenginisialisasi kamera laptop...")
cap = cv2.VideoCapture(0) # 0 berarti kamera default laptop Anda

if not cap.isOpened():
    print("ERROR: Tidak dapat membuka kamera. Pastikan kamera terhubung dan tidak digunakan oleh aplikasi lain.")
    exit()

print("Kamera berhasil diinisialisasi. Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read() # Membaca satu frame dari kamera
    if not ret:
        print("Gagal mengambil frame dari kamera. Keluar...")
        break

    # Balik gambar secara horizontal (opsional, agar terlihat seperti cermin)
    frame = cv2.flip(frame, 1)

    # Ubah frame menjadi grayscale (diperlukan untuk deteksi wajah Haar Cascade)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah dalam frame
    # scaleFactor: Seberapa banyak ukuran gambar dikurangi pada setiap skala gambar.
    # minNeighbors: Berapa banyak tetangga yang harus dimiliki kandidat persegi panjang untuk mempertahankannya.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Proses setiap wajah yang terdeteksi
    for (x, y, w, h) in faces:
        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Warna biru, tebal 2 piksel

        # Ekstrak ROI (Region of Interest) wajah untuk prediksi ekspresi
        roi_gray = gray[y:y+h, x:x+w]
        # roi_color = frame[y:y+h, x:x+w] # Tidak digunakan untuk model grayscale

        # --- Prediksi Ekspresi ---
        if emotion_model is not None:
            try:
                # Ubah ukuran ROI wajah menjadi ukuran input yang diharapkan oleh model ekspresi (64x64 piksel)
                # Ini adalah perubahan krusial dari masalah 'shape' sebelumnya!
                resized_face_for_emotion = cv2.resize(roi_gray, (64, 64), interpolation = cv2.INTER_AREA)

                # Normalisasi piksel ke rentang 0-1
                resized_face_for_emotion = resized_face_for_emotion.astype('float32') / 255.0

                # Tambahkan dimensi batch dan channel (karena grayscale, channel = 1)
                # Bentuk input yang diharapkan Keras untuk gambar tunggal grayscale adalah (1, height, width, 1)
                processed_face = np.expand_dims(resized_face_for_emotion, axis=0) # Bentuk menjadi (1, 64, 64)
                processed_face = np.expand_dims(processed_face, axis=-1) # Bentuk menjadi (1, 64, 64, 1)

                # Optional: Print processed_face shape for debugging
                # print(f"Processed face shape before prediction: {processed_face.shape}")

                emotion_prediction = emotion_model.predict(processed_face, verbose=0)[0] # verbose=0 agar tidak print progress bar
                # Ambil indeks emosi dengan probabilitas tertinggi
                emotion_label_index = np.argmax(emotion_prediction)
                predicted_emotion = emotion_labels[emotion_label_index]

                # Tampilkan teks ekspresi di atas wajah
                cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)
            except Exception as e:
                # Ini akan menampilkan error spesifik di konsol, membantu debugging
                print(f"Error prediksi ekspresi (di dalam loop): {e}")
                cv2.putText(frame, "Error Prediksi Ekspresi", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Model Ekspresi Tdk Ada", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 165, 255), 1, cv2.LINE_AA)


    # Tampilkan frame di jendela
    cv2.imshow('Deteksi Wajah & Ekspresi (Tekan Q untuk keluar)', frame)

    # Tunggu tombol 'q' ditekan untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup semua jendela OpenCV
cap.release()
cv2.destroyAllWindows()
print("\nProgram selesai. Kamera dimatikan.")