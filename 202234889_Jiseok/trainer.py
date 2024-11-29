import cv2
import numpy as np
import os

# 얼굴 데이터 폴더 경로
data_dir = "face_data"

# LBPH 얼굴 인식기 초기화
recognizer = cv2.face.LBPHFaceRecognizer_create()

# 얼굴 검출 모델 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 학습 데이터와 라벨 초기화
faces = []
labels = []

# 얼굴 데이터 로드
label_map = {}  # 레이블과 이름 매핑
current_label = 0

for filename in os.listdir(data_dir):
    if filename.endswith(".jpg"):
        img_path = os.path.join(data_dir, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # 얼굴 검출 및 검증
        detected_faces = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5)
        for (x, y, w, h) in detected_faces:
            face_region = img[y:y+h, x:x+w]
            faces.append(face_region)
            labels.append(current_label)

        # 파일 이름에서 라벨 추출 (예: owner_1.jpg -> "owner")
        label_name = filename.split("_")[0]
        if label_name not in label_map:
            label_map[label_name] = current_label
            current_label += 1

# 학습 데이터와 라벨 넘파이 배열로 변환
faces = np.array([cv2.resize(face, (100, 100)) for face in faces])
labels = np.array(labels)

# LBPH 모델 학습
recognizer.train(faces, labels)

# 모델 저장
recognizer.save("trainer.yml")
print(f"Model trained and saved as 'trainer.yml'")
print(f"Label Map: {label_map}")
