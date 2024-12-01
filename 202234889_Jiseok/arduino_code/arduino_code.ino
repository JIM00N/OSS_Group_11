#include <Servo.h>

Servo tailServo; // 꼬리 모터
int leftMotor = 3;  // 왼쪽 DC 모터 (PWM 핀)
int rightMotor = 5; // 오른쪽 DC 모터 (PWM 핀)
int piezo = 9;      // 스피커 핀

void setup() {
  Serial.begin(9600);  // 시리얼 통신 초기화
  tailServo.attach(6); // 서보 모터 연결
  pinMode(leftMotor, OUTPUT);
  pinMode(rightMotor, OUTPUT);
  pinMode(piezo, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readString();

    if (command == "owner") {
      // 주인 인식 시: 꼬리 흔들기
      for (int angle = 0; angle <= 90; angle += 10) {
        tailServo.write(angle);
        delay(50);
      }
      for (int angle = 90; angle >= 0; angle -= 10) {
        tailServo.write(angle);
        delay(50);
      }
    }
    
    else if (command == "stranger") {
      // 낯선 사람 인식 시: 짖기
      for (int i = 0; i < 3; i++) {
        tone(piezo, 1000, 200);  // 1000Hz 톤을 200ms 동안 재생
        delay(300);
      }

    }
    
    else if (command.startsWith("rotate")) {

      // 주인을 바라보기 위해 회전
      char direction[2];
      command.substring(6, 7).toCharArray(direction, 2);
      int speed = command.substring(8).toInt();  // Python에서 전송한 속도 값 읽기
      if (direction[0] == 'L'){
        analogWrite(leftMotor, -1 * speed);
        analogWrite(rightMotor, speed);
      }
      else if (direction[0] == 'R'){
        analogWrite(leftMotor, 0);
        analogWrite(rightMotor, 0);
      }
      delay(500); // 0.5초 동안 회전
    }
  }
}
