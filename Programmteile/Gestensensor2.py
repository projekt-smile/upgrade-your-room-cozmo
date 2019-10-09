import cozmo
import time
import grovepi
import grove_gesture_sensor

g=grove_gesture_sensor.gesture()
g.init()


def cozmo_program(robot: cozmo.robot.Robot):
    while True:
        gest=g.return_gesture()
        #Übeprüft die erkannt Geste
        if gest==g.FORWARD:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.BACKWARD:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        else:
            print("error")
        time.sleep(.1)
        
cozmo.run_program(cozmo_program)


