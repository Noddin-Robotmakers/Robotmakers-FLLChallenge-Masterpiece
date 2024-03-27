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

# Solve Missions #4 and #5 and go to the other Base
def solve_missions_4_5_and_go_to_other_base():
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=100,
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
    drivebase.straight(distance=570, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=190, then=Stop.HOLD, wait=True)
    # Go backward
    drivebase.straight(distance=-190, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=43, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=235, then=Stop.HOLD, wait=True)
    # Half-complete mission 5
    drivebase.turn(angle=80, then=Stop.HOLD, wait=True)
    # Complete M5
    drivebase.straight(distance=900, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)

    # Go to the other side
    drivebase.straight(distance=1220, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_missions_4_5_and_go_to_other_base()
