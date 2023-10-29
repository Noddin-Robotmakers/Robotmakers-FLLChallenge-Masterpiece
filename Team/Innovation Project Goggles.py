from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
distance = UltrasonicSensor(port=Port.A)

while True:
    if distance.distance() <= 50:
        hub.speaker.beep(500, 100)
