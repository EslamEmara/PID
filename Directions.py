#import pigpio
#pi = pigio.pi()
import time
from motion_initialization import addmotor
pins = [3,5,7,11,13,15,8,10,11]   #the pin 11 for servo for clapper
class Direction :
    def __init__(self):
        for i in range(9) :
          # pi.set_mode(pins[i], pigpio.INPUT)
          print("set the mode of pins",pins[i])
        self.motor1 = addmotor(pins[0])
        self.motor2 = addmotor(pins[1])
        self.motor3 = addmotor(pins[2])
        self.motor4 = addmotor(pins[3])
        self.motor5 = addmotor(pins[4])
        self.motor6 = addmotor(pins[5])
        self.motor7 = addmotor(pins[6])
        self.motor8 = addmotor(pins[7])
        time.sleep(7)
        print("motors are ready >>>")
        return

    # Forward:
    # 1&2 (-)
    # 3&4 (-)
    def forward(self,addition_speed):
        print("forward direction")
        self.motor1.ccw(addition_speed)
        self.motor2.ccw(addition_speed)
        self.motor3.ccw(addition_speed)
        self.motor4.ccw(addition_speed)
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()
        return

    # Backward:
    # 1&2 (+)
    # 3&4 (+)
    def Backward(self,addition_speed):
        print("Backward direction")
        self.motor1.cw(addition_speed)
        self.motor2.cw(addition_speed)
        self.motor3.cw(addition_speed)
        self.motor4.cw(addition_speed)
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()
        return

    # Right:
    # 2&3 (-)
    # 1&4 (+)
    def Right(self, addition_speed):
        print("Right direction")
        self.motor1.cw(addition_speed)
        self.motor2.ccw(addition_speed)
        self.motor3.ccw(addition_speed)
        self.motor4.cw(addition_speed)
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()
        return

# Left:
# 2&3 (+)
# 1&4 (-)
    def Left(self, addition_speed):
        print("Left direction")
        self.motor1.ccw(addition_speed)
        self.motor2.cw(addition_speed)
        self.motor3.cw(addition_speed)
        self.motor4.ccw(addition_speed)
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()
        return

# Up:
# 5&8 (-)
# 6&7 (+)
    def Up(self, addition_speed):
        print("Up direction")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.ccw(addition_speed)
        self.motor6.cw(addition_speed)
        self.motor7.cw(addition_speed)
        self.motor8.ccw(addition_speed)
        return

# Down:
# 5&8 (+)
# 6&7 (-)
    def Down(self, addition_speed):
        print("Down direction")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.cw(addition_speed)
        self.motor6.ccw(addition_speed)
        self.motor7.ccw(addition_speed)
        self.motor8.cw(addition_speed)
        return

# Roll to right (x):
# 7&8 (-)
# 5&6 (+)
    def RollToRight(self, addition_speed):
        print("RollToRight direction")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.cw(addition_speed)
        self.motor6.cw(addition_speed)
        self.motor7.ccw(addition_speed)
        self.motor8.ccw(addition_speed)
        return

# Roll to left (x):
# 7&8 (+)
# 5&6 (-)
    def RollToLeft(self, addition_speed):
        print("RollToLeft direction")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.ccw(addition_speed)
        self.motor6.ccw(addition_speed)
        self.motor7.cw(addition_speed)
        self.motor8.cw(addition_speed)
        return

# Pitch up (y):
# 5&7 (-)
# 6&8 (+)
    def PitchUp(self, addition_speed):
        print("PitchUp direction")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.ccw(addition_speed)
        self.motor6.cw(addition_speed)
        self.motor7.ccw(addition_speed)
        self.motor8.cw(addition_speed)
        return

# Pitch down (y):
# 5&7 (+)
# 6&8 (-)
    def PitchDown(self, addition_speed):
        print("PitchDown direction")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.cw(addition_speed)
        self.motor6.ccw(addition_speed)
        self.motor7.cw(addition_speed)
        self.motor8.ccw(addition_speed)
        return

# Yaw cw (z):
# 2&4 (-)
# 1&3 (+)
    def YawCw(self, addition_speed):
        print("YawCw direction")
        self.motor1.cw(addition_speed)
        self.motor2.ccw(addition_speed)
        self.motor3.cw(addition_speed)
        self.motor4.ccw(addition_speed)
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()
        return

# Yaw ccw (z):
# 2&4 (+)
# 1&3 (-)
    def YawCCw(self, addition_speed):
        print("YawCCw direction")
        self.motor1.ccw(addition_speed)
        self.motor2.cw(addition_speed)
        self.motor3.ccw(addition_speed)
        self.motor4.cw(addition_speed)
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()
        return
    def Stop(self):
        print("motors are stopped")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()

        return
#clapper motion ...
