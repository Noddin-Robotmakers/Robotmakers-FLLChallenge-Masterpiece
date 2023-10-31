# IMPORTS
# =======

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# CONSTANTS
# =========

STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 80
TURN_ACC = 85


# VARIABLE (HUB)
# ==============

hub = InventorHub()


# VARIABLES (DRIVING MOTORS + DRIVEBASE)
# ======================================

left_motor = Motor(port=Port.D,
                   positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 56, 110)


# VARIABLES (ATTACHMENT MOTORS)
# =============================

left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)


# VARIABLES (SENSORS)
# ===================

right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)


# FUNCTIONS
# =========

def solve_mission_3():
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
    # Drive from the home area to mission 2
    drivebase.straight(distance=605, then=Stop.HOLD, wait=True)
    # Turn to the right to the mission
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)
    # Drive in front of Mission 3
    drivebase.straight(distance=556, then=Stop.HOLD, wait=True)
    # Turn left to face Mission 3
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)
    # Wait for half a second to stabilize
    wait(500)
    # Prepare to offset jerk to the left
    drivebase.turn(1)
    # Drive into Mission 3
    drivebase.straight(distance=100, then=Stop.HOLD, wait=True)
    # Stabilize
    wait(500)
    # Turn left to finish the mission
    drivebase.turn(angle=-40, then=Stop.HOLD, wait=True)
    # Stabilize
    wait(500)
    # Turn right (back)
    drivebase.turn(angle=20, then=Stop.HOLD, wait=True)


def return_to_base():
    drivebase.straight(distance=-110, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=20, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-480, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=-120, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=500, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============

solve_mission_3()
return_to_base()
