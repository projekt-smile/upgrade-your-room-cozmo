import cozmo
import time
import grovepi

# der Bewegungssensor ist an Pin D8 angeschlossen
motion_sensor = 8

# eine Variable, in der du einen Wert speichern kannst
motion = 0

# Angabe, dass der Sensor einen INPUT liefert
grovepi.pinMode(motion_sensor, "INPUT")



def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        try:
            motion = grovepi.digitalRead(motion_sensor)
                #überprüft, ob eine Bewegung wahrgenommen wurde mit 0 oder 1
            if motion == 0 or motion == 1:
                #wenn Bewegung wahgenommen (1), dann...
                if motion == 1: 
                    print("Eine unbakannte Bewegung wurde erkannt")
                #ansonsten   
                else:
                    print("Nicht erkannt")
                    
            time.sleep(0.2)

        except IOError:
            print("IOError")
                
cozmo.run_program(cozmo_program)


