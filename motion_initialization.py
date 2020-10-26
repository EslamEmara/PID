#import pigpio
#pi = pigpio.pi()

# this is a module in which the intializations of the motor and its direction of motion


class addmotor:
    def __init__ (self ,gpiopin) :
        self.pin = gpiopin
        #pi.set_servo_pulsewidth(self.pin,1500)     #intializing the motor to stop signal to triger the esc
        print("motor is intailised with speed zero at pin :",self.pin)
   
    def stop(self) :                                #stopping the motor
        #pi.set_servo_pulsewidth(self.pin,1500)
        print("motor at pin :",self.pin,"is stopped ")
    def cw (self,addition_speed):                        #launching the motor in clock wise rotation
        self.speed = 1590+addition_speed                  #1590 is the minimum applied speed to launch the motor 
        if self.speed <1740:                              #1740 is set to be the maximum speed applied on motor to work with forward thrust
            pass
            #pi.set_servo_pulsewidth(self.pin,self.speed)
        elif self.speed>1740:
            self.speed = 1740
            #pi.set_servo_pulsewidth(self.pin,self.speed)
        print("motor at pin :",self.pin," is moving clockwise with speed:",self.speed )
    def ccw (self,addition_speed):                        #launching the motor in counter clock wise rotation
        self.speed =1410-addition_speed                    #1410 is the minimum applied speed to launch the motor 
        if self.speed >1260 :                              #1260 is set to be the maximum speed applied on motor to work with backward thrust
            pass
            #pi.set_servo_pulsewidth(self.pin,self.speed)
        elif (self.speed <1260) :
            self.speed = 1260
            #pi.set_servo_pulsewidth(self.pin,self.speed)
        print("motor at pin :",self.pin," is moving counter clockwise with speed:",self.speed )
