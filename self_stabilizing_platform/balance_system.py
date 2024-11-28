from servo_control import set_servo_angle

def balance_system(roll, pitch, yaw):
    if abs(roll) > 5:  
        set_servo_angle(0, 90 - roll if roll > 0 else 90 + abs(roll))

    if abs(pitch) > 5:
        set_servo_angle(1, 90 - pitch if pitch > 0 else 90 + abs(pitch))

    if abs(yaw) > 5:
        set_servo_angle(2, 90 - yaw if yaw > 0 else 90 + abs(yaw))
