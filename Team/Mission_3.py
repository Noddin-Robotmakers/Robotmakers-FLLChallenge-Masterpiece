from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

hub = InventorHub()
left_motor = Motor(port=Port.D)
right_motor = Motor(port=Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)
drivebase = DriveBase(left_motor, right_motor, 56, 110)


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

def part_one():
    drivebase.settings(straight_speed=100, straight_acceleration=800, turn_rate=80, turn_acceleration=400)
    drivebase.straight(distance=-60, then=Stop.HOLD, wait=True)
    line_track()
    line_track()
    line_track()
    line_track()
    line_track()
    drivebase.straight(distance=-25, then=Stop.HOLD, wait=True)
    left_motor.run_angle(speed=-300, rotation_angle=270, then=Stop.HOLD, wait=True)

def part_two():
    drivebase.straight(distance=-400, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=92, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-90, then=Stop.HOLD, wait=True)
    right_attachent_motor.run_angle(speed=700, rotation_angle=280, then=Stop.HOLD, wait=True)
    wait(500)
    right_attachent_motor.run_angle(speed=200, rotation_angle=-260, then=Stop.HOLD, wait=True)
    right_attachent_motor.run_angle(speed=700, rotation_angle=280, then=Stop.HOLD, wait=True)
    wait(500)
    right_attachent_motor.run_angle(speed=200, rotation_angle=-260, then=Stop.HOLD, wait=True)


def return_to_base():
    drivebase.straight(distance=590, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-680, then=Stop.HOLD, wait=True)


part_one()
part_two()
return_to_base()



