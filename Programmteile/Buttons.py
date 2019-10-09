import cozmo
import time
import grovepi

# an PIN D2 angeschlossen
button = 2

#Angabe, das der Button einen INPUT-Wert liefert
grovepi.pinMode(button, "INPUT")

def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        # wenn der Button gedrückt wurde (1), dann...
        if grovepi.digitalRead(button)== 1: 
            #Hier kann eine Aktion oder mehrere rein.
            
cozmo.run_program(cozmo_program)
            
            
            
            
            
            
            
            
            
            
            
            
    
