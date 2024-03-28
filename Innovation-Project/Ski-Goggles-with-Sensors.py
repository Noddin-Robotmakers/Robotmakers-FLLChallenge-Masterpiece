from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port

hub = PrimeHub()

distance_sensor = UltrasonicSensor(port=Port.A)

while True:
    # when sensing something within 1 meter away
    if distance_sensor.distance() <= 1000:
        hub.speaker.volume(100)
        hub.speaker.beep(500, 100)

    # when sensing something over 1 meter away
    elif distance_sensor.distance() <= 2000:
        hub.speaker.volume(25)
        hub.speaker.beep(500, 100)
