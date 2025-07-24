import cv2
import numpy as np
import os
from keras.models import load_model
from collections import Counter # Import Counter untuk membantu smoothing

# --- PENTING: Untuk menghilangkan warning oneDNN (Opsional) ---
# Tempatkan baris ini paling atas, sebelum import tensorflow/keras
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# --- 1. Definisikan Path File (SESUAIKAN DENGAN LOKASI FILE ANDA!) ---
# Pastikan nama file dan pathnya benar.
# Jika file berada di folder yang sama dengan script ini, cukup nama filenya saja.
# Jika di subfolder, contoh: "data/haarcascade_frontalface_default.xml"
# Jika path absolut, contoh (Windows): r"C:\Users\YourUser\Documents\my_project\haarcascade_frontalface_default.xml"
# Contoh (Linux/macOS): "/home/youruser/my_project/haarcascade_frontalface_default.xml"

face_cascade_path = "haarcascade_frontalface_default.xml"
# GANTI DENGAN NAMA FILE .h5 ANDA YANG SEBENARNYA!
# Pastikan ini adalah file model yang valid dan sesuai (1 kanal input)
expression_model_path = "emotion.h5" 

# --- 2. Inisialisasi Haar Cascade untuk Deteksi Wajah ---
try:
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    if face_cascade.empty():
        raise IOError(f"ERROR: Face cascade file not loaded from {face_cascade_path}")
    print("SUCCESS: Haar Cascade Loaded Successfully!")
except IOError as e:
    print(e)
    print("FATAL ERROR: Please ensure 'haarcascade_frontalface_default.xml' exists and its path is correct.")
    exit() # Keluar dari program jika file vital tidak ditemukan

# --- 3. Muat Model Ekspresi Keras ---
try:
    model = load_model(expression_model_path)
    print("SUCCESS: Expression Model Loaded Successfully!")
    print(f"DEBUG: Model expected input shape: {model.input_shape}") # Debugging: Bentuk input yang diharapkan model
except Exception as e:
    print(f"FATAL ERROR: Failed to load expression model: {e}")
    print("Please ensure this is a valid Keras model file (.h5) and is compatible with your TensorFlow version.")
    # Kita tidak exit di sini agar jendela kamera tetap bisa tampl
    # dan kita bisa melihat pesan "Model Ekspresi Tidak Ditemukan
    model = None # Set model menjadi None untuk menandakan kegagaan
    print("Model Ekspresi Tidak Ditemukan. Program akan berjalan tanpa prediksi ekspresi.")

# --- 4. Definisikan Label Ekspresi ---
# Urutan label harus sesuai dengan urutan output prediksi dari model Anda.
EMOTIONS = ["Senang", "Netral", "Marah", "Netral", "Senang", "Marah"]

# --- 5. Inisialisasi Kamera Web ---
cap = cv2.VideoCapture(0) # 0 adalah ID default untuk webcam internal

if not cap.isOpened():
    print("FATAL ERROR: Could not open webcam. Please check if camera is connected and not in use.")
    exit()

print("\nCamera initialized. Press 'q' to quit.")

# --- Bagian Baru untuk Smoothing ---
# Dictionary untuk menyimpan riwayat emosi untuk setiap wajah yang terdeteksi
# Key: (x, y) koordinat wajah, Value: list riwayat emosi
face_emotion_history = {}
SMOOTHING_WINDOW_SIZE = 10 # Jumlah frame yang akan digunakan untuk smoothing (bisa disesuaikan)
MAX_FACE_HISTORY = 50 # Batas entri wajah dalam history agar tidak membengkak

# --- 6. Loop Utama untuk Pemrosesan Frame ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("ERROR: Failed to grab frame from camera. Exiting...")
        break

    # Konversi frame ke grayscale untuk deteksi wajah dan preprocessing model
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah dalam frame grayscale
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    current_frame_faces_keys = [] # Untuk melacak wajah yang terdeteksi di frame ini

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Identifikasi unik untuk wajah ini (menggunakan koordinat atas-kiri)
        # Akan ada sedikit pergeseran, jadi ini tidak sempurna untuk melacak satu wajah.
        # Untuk tracking yang lebih robust, butuh algoritma tracking multi-object.
        # Untuk tujuan smoothing sederhana, ini cukup.
        face_key = (x, y) 
        current_frame_faces_keys.append(face_key)

        if model is not None: # Hanya jika model berhasil dimuat
            # --- Preprocessing Wajah untuk Model Ekspresi ---
            roi_gray = gray_frame[y:y + h, x:x + w]
            
            try:
                resized_face = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            except cv2.error as e:
                print(f"ERROR: Failed to resize face ROI. Skipping this face. Detail: {e}")
                cv2.putText(frame, "RESIZE ERROR", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                continue # Lanjutkan ke wajah berikutnya jika ada masalah resize
            
            normalized_face = resized_face / 255.0
            normalized_face = normalized_face.astype(np.float32) 
            
            reshaped_face = np.expand_dims(normalized_face, axis=-1) 
            reshaped_face = np.expand_dims(reshaped_face, axis=0)    

            # --- Prediksi Ekspresi Menggunakan Model ---
            try:
                prediction = model.predict(reshaped_face)[0]
                
                emotion_probability = np.max(prediction)
                emotion_label_arg = np.argmax(prediction)
                current_emotion_text = EMOTIONS[emotion_label_arg]

                # --- Menerapkan Smoothing ---
                # Inisialisasi riwayat untuk wajah ini jika belum ada
                if face_key not in face_emotion_history:
                    face_emotion_history[face_key] = []
                
                # Tambahkan emosi saat ini ke riwayat wajah ini
                face_emotion_history[face_key].append(current_emotion_text)
                
                # Pertahankan ukuran jendela smoothing
                if len(face_emotion_history[face_key]) > SMOOTHING_WINDOW_SIZE:
                    face_emotion_history[face_key].pop(0) # Hapus emosi terlama

                # Dapatkan emosi yang paling sering muncul (modus) dalam riwayat
                smoothed_emotion_text = Counter(face_emotion_history[face_key]).most_common(1)[0][0]

                # --- Tampilkan Hasil di Frame ---
                cv2.putText(frame, smoothed_emotion_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.putText(frame, f"{emotion_probability:.2f}", (x, y + h + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            except Exception as pred_e:
                cv2.putText(frame, "PREDICTION ERROR", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                print(f"ERROR: An error occurred during prediction for a face: {pred_e}")
                print(f"DEBUG: Current reshaped_face shape that caused error: {reshaped_face.shape}")
                # Hapus riwayat wajah ini jika terjadi error agar tidak mengganggu smoothing berikutnya
                if face_key in face_emotion_history:
                    del face_emotion_history[face_key]
                continue # Lanjutkan ke wajah berikutnya jika ada

        else: # Jika model gagal dimuat
            cv2.putText(frame, "Model Ekspresi Tidak Ditemukan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # --- Membersihkan riwayat wajah yang tidak lagi terdeteksi ---
    # Ini penting agar face_emotion_history tidak membengkak
    keys_to_delete = [key for key in face_emotion_history if key not in current_frame_faces_keys]
    for key in keys_to_delete:
        del face_emotion_history[key]
    
    # Batasi ukuran dictionary history untuk mencegah kebocoran memori jika banyak wajah muncul
    if len(face_emotion_history) > MAX_FACE_HISTORY:
        # Hapus entri terlama jika jumlah wajah melebihi batas
        # Ini adalah metode sederhana, untuk produksi mungkin butuh strategi lebih canggih
        oldest_key = next(iter(face_emotion_history)) 
        del face_emotion_history[oldest_key]

    # Tampilkan frame yang telah diproses
    cv2.imshow('Face & Expression Detection (Press Q to Quit)', frame)

    # Tunggu tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- 7. Pembersihan (Release Resources) ---
cap.release() # Lepaskan objek VideoCapture
cv2.destroyAllWindows() # Tutup semua jendela OpenCV
print("\nProgram finished. All resources released.")