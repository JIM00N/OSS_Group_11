import math
from smbus2 import SMBus

GYRO_ADDR = 0x68
bus = SMBus(1)

def setup_gyro():
    bus.write_byte_data(GYRO_ADDR, 0x6B, 0)

def read_gyro_data():
    acc_x = bus.read_word_data(GYRO_ADDR, 0x3B)
    acc_y = bus.read_word_data(GYRO_ADDR, 0x3D)
    acc_z = bus.read_word_data(GYRO_ADDR, 0x3F)

    acc_x = ((acc_x & 0xFF) << 8) | (acc_x >> 8)
    acc_y = ((acc_y & 0xFF) << 8) | (acc_y >> 8)
    acc_z = ((acc_z & 0xFF) << 8) | (acc_z >> 8)

    roll = math.atan2(acc_y, acc_z) * 180 / math.pi
    pitch = math.atan2(-acc_x, math.sqrt(acc_y**2 + acc_z**2)) * 180 / math.pi
    yaw = math.atan2(acc_x, acc_y) * 180 / math.pi  
    
    return roll, pitch, yaw
