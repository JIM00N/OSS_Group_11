import cv2
import serial
import time

# 아두이노와 시리얼 통신 설정 (포트 이름은 본인 아두이노 프로그램에서 설정한 포트)
arduino = serial.Serial("/dev/cu.usbmodem101", 9600, timeout=1)
time.sleep(2)  # 아두이노 초기화 대기

owner_faces = cv2.face.LBPHFaceRecognizer_create()
owner_faces.read('trainer.yml')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 카메라 열기

cap = cv2.VideoCapture(0)  # Laptop 카메라


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 탐지
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=8)

    for (x, y, w, h) in faces:
        # 얼굴 영역 가져오기
        face_region = gray[y:y+h, x:x+w]
        face_region = cv2.resize(face_region, (100, 100))

        # 주인과 비교
        label, confidence = owner_faces.predict(face_region)
        if label == 1 and confidence < 100:  # 레이블 1 = 주인, confidence가 낮을수록 매칭 정확
            cv2.putText(frame, "Owner Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            arduino.write(b'owner\n')  # 주인을 인식했음을 아두이노에 전송
        else:
            cv2.putText(frame, "Stranger", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            arduino.write(b'stranger\n')  # 낯선 사람을 아두이노에 전송

        # 얼굴 영역 박스 그리기
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 카메라 출력
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q'를 눌러 종료
        break

cap.release()
cv2.destroyAllWindows()
