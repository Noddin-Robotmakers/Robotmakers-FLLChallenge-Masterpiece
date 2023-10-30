from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

distance_sensor = UltrasonicSensor(port=Port.A)

while True:
    if distance_sensor.distance() <= 1000:  # When senses somthing within 1 meter
        hub.speaker.volume(100)
        hub.speaker.beep(500, 100)

    elif distance_sensor.distance() <= 2000:  # When senses somthing over 1 meter
        hub.speaker.volume(25)
        hub.speaker.beep(500, 100)
