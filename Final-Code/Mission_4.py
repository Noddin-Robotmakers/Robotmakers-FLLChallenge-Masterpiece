# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 80
TURN_ACC = 85


# VARIABLES Representing Robot Electronics
# ========================================

# Hub
hub = InventorHub()

# Driving Motors & Drivebase
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 56, 110)

# Attachment Motors
left_attachment_motor = Motor(port=Port.B)
right_attachment_motor = Motor(port=Port.A)

# Sensors
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)


# FUNCTIONS Representing Robot Behaviors
# ======================================

# Solve Mission #4 and go to the other Base
def solve_m4_and_go_to_other_base():
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=80,
                       turn_acceleration=85)

    # Go forward
    drivebase.straight(distance=550, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=60, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=30, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=580, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)
    # Release pedestal and audiance members
    drivebase.straight(distance=170, then=Stop.HOLD, wait=True)
    # Go backward
    drivebase.straight(distance=-170, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=900, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)

    # Go to other base
    drivebase.straight(distance=1300, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_m4_and_go_to_other_base()
