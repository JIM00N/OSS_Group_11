import cv2
import os

# 얼굴 검출 모델 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 저장 경로
data_dir = "face_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # 얼굴 영역 추출
        face_region = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face_region, (100, 100))

        # 히스토그램 균일화 적용
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        face_resized = clahe.apply(face_resized)

        # 얼굴 저장
        count += 1
        file_path = os.path.join(data_dir, f"owner_{count}.jpg")
        cv2.imwrite(file_path, face_resized)
        print(f"Saved {file_path}")

        # 얼굴 감지 영역 표시
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Face Registration", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 300:
        break

cap.release()
cv2.destroyAllWindows()
