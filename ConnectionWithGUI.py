from Directions import Direction
import time
CurrentDirection=""
class ControlMotion:
    def __init__(self):
       self.rov=Direction()                        #object from the directions class
       return
    def DirectionofTravel(self,msg):
        array = msg.split()
        global CurrentDirection
##############################################################################################################
######## as no speed is given (addition speed =0) the rov motors will operate with its mininmum speed#########
##############################################################################################################
        if(array[0]=="move"):
            if(array[1]=="forward"):                   #forward
               self.rov.forward(0)
               CurrentDirection="forward"
            
            elif(array[1]=="backward"):                #backward
                self.rov.Backward(0)
                CurrentDirection = "backward"
            
            elif(array[1]=="right"):                   #slide right
                self.rov.Right(0)
                CurrentDirection = "right"
           
            elif(array[1]=="left"):                    #slide left
                self.rov.Left(0)
                CurrentDirection = "left"
            
            elif(array[1]=="up"):                      #upward
                self.rov.Up(0)
                CurrentDirection = "up"
            
            elif(array[1]=="down"):                    #downward
                self.rov.Down(0)
                CurrentDirection = "down"

            elif(array[1]=="rolltoright"):             #rolling clockwise
                self.rov.RollToRight(0)
                CurrentDirection = "rolltoright"

            elif(array[1]=="rolltoleft"):              #rolling counterclockwise
                self.rov.RollToLeft(0)
                CurrentDirection = "rolltoleft"    
            
            elif(array[1]=="pitchup"):                 #pitching up
                self.rov.PitchUp(0)
                CurrentDirection = "pitchup"

            elif(array[1]=="pitchdown"):               #pitching down
                self.rov.PitchDown(0)
                CurrentDirection = "pitchdown"

            elif(array[1]=="yawcw"):                   #rotating right 
                self.rov.YawCw(0)
                CurrentDirection = "yawcw"

            elif(array[1]=="yawccw"):                  #rotating left 
                self.rov.YawCCw(0)
                CurrentDirection = "yawccw"
            elif(array[1]== "stop"):
                self.rov.Stop()                       #motors stopped
#####################################################################################################################################
## as speed will be given now (addition speed >0)the motors will operate with speed equals their minimum speed plus the added speed##
#####################################################################################################################################
        
        elif(array[0]=="speed"):
            if (CurrentDirection == "forward"):
                self.rov.forward(int(array[1]))
            elif (CurrentDirection == "backward"):
                self.rov.Backward(int(array[1]))
            elif (CurrentDirection == "right"):
                self.rov.Right(int(array[1]))
            elif (CurrentDirection == "left"):
                self.rov.Left(int(array[1]))
            elif (CurrentDirection == "up"):
                self.rov.Up(int(array[1]))   
            elif (CurrentDirection == "down"):
                self.rov.Down(int(array[1])) 
            elif (CurrentDirection == "rolltoright"):
                self.rov.RollToRight(int(array[1]))
            elif (CurrentDirection == "rolltoleft"):
                self.rov.RollToLeft(int(array[1]))
            elif (CurrentDirection == "pitchup"):
                self.rov.PitchUp(int(array[1]))
            elif (CurrentDirection == "pitchdown"):
                self.rov.PitchDown(int(array[1]))    
            elif (CurrentDirection == "yawcw"):
                self.rov.YawCw(int(array[1]))
            elif (CurrentDirection == "yawccw"):
                self.rov.YawCCw(int(array[1]))  
        return

