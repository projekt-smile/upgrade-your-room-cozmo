import cozmo
import time
import grovepi

# Lichtsensor ist an PIN A1 angeschlossen
light_sensor = 1

# Ein Schwellwert, damit der Lichtsensor
# nicht bei jeder kleinen Änderung reagiert
threshold = 10

#Angabe, dass der Sensor einen INPUT Wert liefert
grovepi.pinMode(light_sensor, "INPUT")

def cozmo_program(robot: cozmo.robot.Robot):

    while True:
        # wenn der Lichtsensor größer, gleich 500 Lumen misst, dann...
        if grovepi.analogRead(light_sensor) >= 500: 
            #Hier kann eine oder mehrere Aktionen rein
            time.sleep(2)

        # wenn der Lichtsensor weniger als 500 Lumen misst, dann...    
        elif grovepi.analogRead(light_sensor) < 500: 
            #Hier kann eine oder mehrere Aktionen rein
            time.sleep(2)

                
cozmo.run_program(cozmo_program)


