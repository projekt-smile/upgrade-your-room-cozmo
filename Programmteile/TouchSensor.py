import cozmo
import time
import grovepi


# an PIN D4 angeschlossen
touch_sensor = 4

# Angabe, dass der Sensor einen INPUT liefert
grovepi.pinMode(touch_sensor,"INPUT")

def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        # wenn der Touch Sensor berührt wurde (1), dann...
        if grovepi.digitalRead(touch_sensor) == 1: 
            #Hier kann eine oder mehrer Aktionen rein

cozmo.run_program(cozmo_program)
