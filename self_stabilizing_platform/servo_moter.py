import RPi.GPIO as GPIO

SERVO_PINS = [17, 27, 22]
servo_pwm = []

def setup_servos():
    GPIO.setmode(GPIO.BCM)
    for pin in SERVO_PINS:
        GPIO.setup(pin, GPIO.OUT)
        pwm = GPIO.PWM(pin, 50) 
        pwm.start(7.5) 
        servo_pwm.append(pwm)

def set_servo_angle(servo_index, angle):
    duty_cycle = 2.5 + (angle / 18)  
    servo_pwm[servo_index].ChangeDutyCycle(duty_cycle)

def cleanup_servos():
    for pwm in servo_pwm:
        pwm.stop()
    GPIO.cleanup()
