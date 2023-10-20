from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()
left_motor = Motor(port=Port.D)
right_motor = Motor(port=Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)
drivebase = DriveBase(left_motor, right_motor, 13, 125)


def line_track():
    if (left_color_sensor.color() == Color.NONE) or (right_color_sensor.color() == Color.NONE):
        # checks if the color detected is black and moves forward if it is
        left_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
        right_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
    else:
        while (left_color_sensor.color() != Color.NONE) or (right_color_sensor.color() != Color.NONE):
            # if there is no black then go left and then if still no black then it movex right
            left_motor.run_angle(speed=-700, rotation_angle=10, then=Stop.HOLD, wait=False)
            if (left_color_sensor.color() != Color.NONE) or (right_color_sensor.color() != Color.NONE):
                while (left_color_sensor.color() != Color.NONE) or (right_color_sensor.color() != Color.NONE):
                    right_motor.run_angle(speed=-700, rotation_angle=10, then=Stop.HOLD, wait=False)
                    if (left_color_sensor.color() == Color.NONE) or (right_color_sensor.color() == Color.NONE):
                        left_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
                        right_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
                        



