# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 101
STRAIGHT_ACC = 101
TURN_RATE = 70
TURN_ACC = 80


# VARIABLES Representing Robot Electronics
# ========================================

# Hub
hub = InventorHub()

# Driving Motors & Drivebase
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 56, 110)

# Attachment Motors
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)


# FUNCTIONS Representing Robot Behaviors
# ======================================

# Solve missions #9 and #8
def solve_missions_9_8():
    # Set initial drivebase speed
    drivebase.settings(straight_speed=600,
                       straight_acceleration=400,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Go forward
    drivebase.straight(distance=40, then=Stop.HOLD, wait=True)
    # Go backward
    drivebase.straight(distance=-40, then=Stop.HOLD, wait=True)
    # Change drivebase speed
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Go forward
    drivebase.straight(distance=840, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_missions_9_8()
