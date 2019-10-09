import cozmo
import grovepi
import time

# an Pin D3 angeschlossen
ultrasonic_ranger = 3

def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        try:
            # wenn der Abstand größer, gleich 20 cm ist, dann...
            if grovepi.ultrasonicRead(ultrasonic_ranger) >= 20:
                 print("-")

            # wenn der Abstand kleiner 20 cm ist, dann...
            elif grovepi.ultrasonicRead(ultrasonic_ranger) < 20: 
                #Hier kann eine oder mehrere Aktionen rein
                time.sleep(5)


cozmo.run_program(cozmo_program)




