import cv2
import mediapipe as mp
import numpy as np
from flask import Flask, render_template, Response

# Inisialisasi Flask
app = Flask(__name__)

# Inisialisasi face detection dan face mesh dari MediaPipe
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk mengecek apakah rambut memenuhi dahi
def cek_rambut(frame, face_landmarks, detection):
    h, w, _ = frame.shape
    bbox = detection.location_data.relative_bounding_box
    x_min = int(bbox.xmin * w)
    y_min = int(bbox.ymin * h)
    box_width = int(bbox.width * w)
    box_height = int(bbox.height * h)

    # Perluas area untuk rambut
    hair_y_min = max(y_min - int(0.5 * box_height), 0)  # Perluas ke atas
    cv2.rectangle(frame, (x_min, hair_y_min), (x_min + box_width, y_min), (128, 128, 128), 2)

    # Ambil area rambut dari frame
    hair_region = frame[hair_y_min:y_min, x_min:x_min + box_width]

    # Pastikan area rambut tidak kosong sebelum konversi warna
    if hair_region.size > 0:
        hsv = cv2.cvtColor(hair_region, cv2.COLOR_BGR2HSV)

        # Dapatkan landmark untuk dahi
        forehead_landmark = face_landmarks.landmark[10]  # Landmark di bagian dahi

        # Konversi ke koordinat piksel
        forehead_y = int(forehead_landmark.y * h)

        # Deteksi rambut panjang berdasarkan area di dahi
        if hair_y_min < forehead_y:
            forehead_to_chin_dist = forehead_y - y_min
            if forehead_to_chin_dist != 0:
                covered_dahi_ratio = (forehead_y - hair_y_min) / forehead_to_chin_dist
                if covered_dahi_ratio > 0.6:  # Ubah threshold ke nilai yang lebih tinggi
                    cv2.putText(frame, 'Rambut Panjang', (x_min, hair_y_min - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    cv2.rectangle(frame, (x_min, hair_y_min), (x_min + box_width, y_min), (0, 0, 255), 2)
                elif covered_dahi_ratio < 0.3:  # Ubah threshold untuk rambut pendek ke nilai yang lebih rendah
                    cv2.putText(frame, 'Rambut Pendek', (x_min, hair_y_min - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x_min, hair_y_min), (x_min + box_width, y_min), (0, 255, 0), 2)
                else:
                    cv2.putText(frame, 'Deteksi Tidak Pasti', (x_min, hair_y_min - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    else:
        cv2.putText(frame, 'Tidak Ada Deteksi Rambut', (x_min, hair_y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Fungsi streaming frame video
def generate_frames():
    cap = cv2.VideoCapture(0)

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection, \
            mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:

        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                break

            # Konversi warna BGR ke RGB
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Deteksi wajah
            face_detection_results = face_detection.process(image_rgb)
            face_mesh_results = face_mesh.process(image_rgb)

            # Jika wajah terdeteksi, lakukan analisis rambut
            if face_detection_results.detections and face_mesh_results.multi_face_landmarks:
                for detection, face_landmarks in zip(face_detection_results.detections, face_mesh_results.multi_face_landmarks):
                    # Mendeteksi dan menganalisis rambut berdasarkan wajah yang terdeteksi
                    cek_rambut(frame, face_landmarks, detection)

            # Encode frame ke JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Kirim frame melalui stream HTTP
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Rute untuk halaman utama (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk halaman demo (demo.html)
@app.route('/demo')
def demo():
    return render_template('demo.html')

# Rute untuk stream video
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Jalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
