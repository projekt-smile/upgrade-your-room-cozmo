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
        elif gest==g.LEFT:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.RIGHT:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.UP:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.DOWN:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.CLOCKWISE:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.ANTI_CLOCKWISE:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==g.WAVE:
            #Hier kann eine oder mehrer Aktionen rein
            time.sleep(5)
        elif gest==0:
            print("Keine Geste erkannt")
        else:
            print("error")
        time.sleep(.1)
        
cozmo.run_program(cozmo_program)


