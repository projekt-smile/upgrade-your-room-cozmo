import cozmo
import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def cozmo_program(robot: cozmo.robot.Robot):
    
    purpleColor = cozmo.lights.Color(rgb=(136,0,255))
    cube1 = robot.world.get_light_cube(LightCube1Id)  
    cube2 = robot.world.get_light_cube(LightCube2Id)  
    cube3 = robot.world.get_light_cube(LightCube3Id)  

    while True:
        if cube1 is not None:
            #Setzt die Farbe des Cube1 auf eine selbst erstellte Farbe
            cube1.set_lights(cozmo.lights.Light(purpleColor))
            time.sleep(1)
        if cube2 is not None:
            #Setzt die Farbe des Cube2 auf Blau
            cube2.set_lights(cozmo.lights.blue_light)
            time.sleep(1)
            #Schaltet Cube2 aus
            cube2.set_lights(cozmo.lights.off_light)
        if cube3 is not None:
            #Setzt die Farbe des Cube2 auf Grün
            cube3.set_lights(cozmo.lights.green_light)
            time.sleep(1)
            #Setzt die Farbe des Cube2 auf Rot
            cube3.set_lights(cozmo.lights.red_light)
        else:
            cozmo.logger.warning("Überprüfe die Batterie der Würfel.")
            time.sleep(1)

cozmo.run_program(cozmo_program)
