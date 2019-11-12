# Allgemein

Dieses Image für den Raspberry Pi enthält alle benötigten Pakete um direkt mit dem Cozmo, einem Pi und einem Handy zu basteln.

Bei der Betriebssoftware handelt es sich um Raspbian mit Desktopsupport. Zusätzlich wurde das [Cozmo SDK](http://cozmosdk.anki.com/docs/index.html), [Android Debug Bridge](https://developer.android.com/studio/command-line/adb), [GrovePi](https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/) und, falls nicht vorher vorhanden, Python 3.5 installiert.

## Installation und Benutzung des Images

Die .zip herunterladen, entpacken und die .img-Datei auf eine SD-Karte schreiben, es wird [BalenaEtcher](https://www.balena.io/etcher/) empfohlen.

Ist das Image auf der SD-Karte kann diese in den Pi gesteckt werden. Beim Smartphone sollte nun, sofern nicht bereits geschehen, in den Entwicklereinstellungen USB-Debugging aktiviert werden. Anschließend das Smartphone mit dem Cozmo verbinden, erste Schritte werden in diesem [Video](https://www.youtube.com/watch?time_continue=74&v=8-LokttVEzo&feature=emb_title) von Anki erklärt. Nun kann das Smartphone mit der Cozmo App im SDK-Modus über Kabel an den Pi angeschlossen werden. Der SDK-Modus ist in der App in den Einstellungen erreichbar.

Ob das Smartphone vom Pi erkannt wurde, kann mit dem Befehl ```adb devices``` getestet werden.
Erfolgt keine Auflistung, wurde das Gerät nicht korrekt erkannt und es sollten die vorherigen Schritte überprüft werden.

Python Programme können nun ```import cozmo``` benutzen, um auf das Cozmo-SDK zuzugreifen und die dort vorhandenen Befehle für die Interaktion mit dem Cozmo zu benutzen.

## Das Image selber erstellen

Um das Rad nicht neu zu erfinden soll hier auf die originale [Dokumentation](http://cozmosdk.anki.com/docs/install-linux.html) des SDKs verwiesen werden. Dort werden alle zuvor genannten Schritte ebenfalls und detaillierter beschrieben.

## Example/Usage

```python
import cozmo
from cozmo.objects import LightCube1Id
from cozmo.util import degrees, distance_mm, speed_mmps
   
def cozmo_program(robot: cozmo.robot.Robot):
    cube = robot.world.get_light_cube(LightCube1Id)               
    if cube is not None:
        cube.set_lights(cozmo.lights.Light(cozmo.lights.Color(rgb=(136,0,255))))
        
    robot.drive_straight(distance_mm(1000), speed_mmps(150)).wait_for_completed()
    robot.say_text(say_time).wait_for_completed()
```
