import time

kd = 0.5
kp = 70 
ki = 0.001

def imu_current_roll():
   return int(input("imu reading:"))

desired_roll = imu_current_roll()               

new_time = time.time()
roll_error =0
roll_error_integral = 0

while True:
    actual_roll = imu_current_roll()
    old_time = new_time
    new_time = time.time()
    roll_error_diff = new_time-old_time
    roll_old_error = roll_error
    roll_error = desired_roll - actual_roll
    roll_error_change = roll_error - roll_old_error
    roll_error_slope = roll_error_change / roll_error_diff

    roll_error_integral += (roll_error*roll_error_diff)

    pid = kd * roll_error + kp * roll_error_slope + ki*roll_error_integral

    if pid >0:
        print ('pitch up with speed ',pid)
    else:
        print ('pitch down with speed ',pid)