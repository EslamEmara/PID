import time
from mpu6050 import mpu6050

#imu = mpu6050(0x68)

kd = 0.5
kp = 70 
ki = 0.001

sent = False
def server_recieve():
    global sent
    if sent == False:
        sent = True
        return True
    else:
        return False

def get_data_test():
    roll = int(input('current imu roll reading='))
    rotate =int(input('current imu rotate reading='))
    pitch = int(input('current imu pitch reading='))
    return roll,pitch,rotate


def imu_current_reading():
    #roll,pitch,rotate = imu.get_gyro_data()
    roll,pitch,rotate = get_data_test()

    return roll,pitch,rotate

def get_desired_location():
    if (server_recieve()):
        return imu_current_reading()
    else:
        return False 
        


desired_roll,desired_pitch,desired_rotate = get_desired_location()  

roll_new_time = time.time()
pitch_new_time = time.time()
rotate_new_time = time.time()

roll_old_time = 0
pitch_old_time = 0
rotate_old_time = 0

roll_error =0
roll_old_error=0
roll_error_sum = 0

pitch_error =0
pitch_old_error=0
pitch_error_sum = 0

rotate_error =0
rotate_old_error =0
rotate_error_sum =0

def calc_pid(desired,actual,new_time,old_time,error,error_sum):
    global kd,kp,ki
    old_time = new_time 
    new_time = time.time()
    time_diff = new_time - old_time
    old_error = error 
    error = desired-actual 
    error_diff = error-old_error
    error_slope = error_diff / time_diff
    error_sum += (error *time_diff)
    return (kd * error + kp * error_slope + ki*error_sum),old_time,old_error,error_sum


while True:

    current_roll ,current_pitch,current_rotate = imu_current_reading()

    roll_pid ,roll_old_time , roll_old_error , roll_error_sum = \
    calc_pid(desired_roll,current_roll,roll_new_time,roll_old_time,roll_error,roll_error_sum)

    pitch_pid ,pitch_old_time , pitch_old_error , pitch_error_sum = \
    calc_pid(desired_pitch,current_pitch,pitch_new_time,pitch_old_time,pitch_error,pitch_error_sum)
    
    rotate_pid ,rotate_old_time , rotate_old_error , rotate_error_sum = \
    calc_pid(desired_rotate,current_rotate,rotate_new_time,rotate_old_time,rotate_error,rotate_error_sum)

    if roll_pid >0:
        print ('roll up with speed ',roll_pid)
    else:
        print ('roll down with speed ',roll_pid)
    if rotate_pid >0:
        print ('rotate left with speed ',rotate_pid)
    else:
        print ('rotate right with speed ',rotate_pid)
    if pitch_pid >0:
        print ('pitch up with speed ',pitch_pid)
    else:
        print ('pitch down with speed ',pitch_pid)
    print('###############################################')