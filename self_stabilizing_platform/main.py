import time
from gyro_sensor import setup_gyro, read_gyro_data
from servo_moter import setup_servos, cleanup_servos
from balance_system import balance_system

if __name__ == "__main__":
    try:
        setup_gyro()
        setup_servos()

        while True:
            roll, pitch, yaw = read_gyro_data()
            print(f"Roll: {roll:.2f}, Pitch: {pitch:.2f}, Yaw: {yaw:.2f}")

            balance_system(roll, pitch, yaw)
            time.sleep(0.1)  

    except KeyboardInterrupt:
        print("Exiting...")
        
    finally:
        cleanup_servos()
