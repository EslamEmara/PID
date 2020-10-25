import time
import busio
from Adafruit_BNO055 import BNO055

# pid constants
kd = 0.5
kp = 70
ki = 0.001

# time variables
old_time=0
new_time=time.time()

# roll variables
roll_current_error =0
roll_old_error=0
roll_error_integral = 0
roll_desired_value = 0

# pitch variables
pitch_current_error =0
pitch_old_error=0
pitch_error_integral = 0
pitch_desired_value = 0

# rotate variables
rotate_current_error = 0
rotate_old_error=0
rotate_error_integral = 0
rotate_desired_value = 0

# depth variables
depth_desired_value = 0         # change its value when the rov goes up or down
depth_old_error = 0
depth_current_error = 0
depth_error_integral = 0

# speeds list of motors to change their speed
def calculate_pid_error(speeds,current_error,old_error,current_integral):
    global old_time, new_time
    old_time = new_time
    new_time = time.time()
    deltaT = new_time-old_time
    derivative = (current_error-old_error)/deltaT
    current_integral += current_error*deltaT
    pid_error = kp*current_error + ki*current_integral + kd*derivative
    print("the pid error : ",pid_error)

    # change the speed during to the pid_error

    return current_integral

def calculate_roll_error(roll_actual_value):
    global roll_old_error,roll_current_error,roll_error_integral
    # put the motors speed to change the roll
    speeds = []
    roll_old_error = roll_current_error
    roll_current_error = roll_desired_value - roll_actual_value
    print("the roll current error : ", roll_current_error)
    roll_error_integral = calculate_pid_error(speeds, roll_current_error, roll_old_error, roll_error_integral)


def calculate_pitch_error(pitch_actual_value):
    global pitch_old_error,pitch_current_error,pitch_error_integral
    # put the motors speed to change the pitch
    speeds = []
    pitch_old_error = pitch_current_error
    pitch_current_error = pitch_desired_value - pitch_actual_value
    print("the pitch current error : ", pitch_current_error)
    pitch_error_integral = calculate_pid_error(speeds, pitch_current_error, pitch_old_error, pitch_error_integral)

def calculate_rotate_error(rotate_actual_value):
    global rotate_old_error,rotate_current_error,rotate_error_integral
    # put the motors speed to change the rotate
    speeds = []
    rotate_old_error = rotate_current_error
    rotate_current_error = rotate_desired_value - rotate_actual_value
    print("the rotate current error : ", rotate_current_error)
    rotate_error_integral = calculate_pid_error(speeds, rotate_current_error, rotate_old_error, rotate_error_integral)

def calculate_depth_error(self):
    global depth_old_error,depth_current_error,depth_error_integral
    # put the motors speed to move up and down
    speeds = []
    depth_old_error = depth_current_error
    # read depth_actual_value from pressure sensor
    # depth_current_error = depth_desired_value - depth_actual_value
    print("the depth current error : ", depth_current_error)
    depth_error_integral = calculate_pid_error(speeds, depth_current_error, depth_old_error, depth_error_integral)


# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:
# imu = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
# BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
# and RST connected to pin P9_12:
# imu= BNO055.BNO055(rst='P9_12')



while True:
    # Read the Euler angles for heading, roll, pitch (all in degrees).
    # heading, roll, pitch = imu.read_euler()
    # Print everything out.
    # print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(heading, roll, pitch, sys, gyro, accel, mag))
    # Other values you can optionally read:
    # Orientation as a quaternion:
    # x,y,z,w = imu.read_quaterion()
    # Sensor temperature in degrees Celsius:
    # temp_c = imu.read_temp()
    # Magnetometer data (in micro-Teslas):
    # x,y,z = imu.read_magnetometer()
    # Gyroscope data (in degrees per second):
    # x,y,z = imu.read_gyroscope()
    # Accelerometer data (in meters per second squared):
    # x,y,z = imu.read_accelerometer()
    # Linear acceleration data (i.e. acceleration from movement, not gravity--
    # returned in meters per second squared):
    # x,y,z = imu.read_linear_acceleration()
    # Gravity acceleration data (i.e. acceleration just from gravity--returned
    # in meters per second squared):
    # x,y,z = imu.read_gravity()
    # Sleep for a second until the next reading.
    # time.sleep(1)

    roll_desired_value,pitch_desired_value,rotate_desired_value=get_desired_location()

    # roll ,pitch ,rotate = imu.read_euler()
    roll = int(input('actual roll position = '))
    pitch = int(input('actual pitch position = '))
    rotate = int(input('actual rotate position = '))
    calculate_roll_error(roll)
    calculate_pitch_error(pitch)
    calculate_rotate_error(rotate)
    calculate_depth_error()

