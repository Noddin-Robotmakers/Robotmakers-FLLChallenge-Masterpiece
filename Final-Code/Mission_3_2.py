# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
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
left_attachment_motor = Motor(port=Port.B)
right_attachment_motor = Motor(port=Port.A)


# FUNCTIONS Representing Robot Behaviors
# ======================================

# Solve Missions #3 and #2
def solve_missions_3_2():
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Drive from the home area to mission 2
    drivebase.straight(distance=610, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(-3)
    # Complete Mission 2
    drivebase.straight(distance=215, then=Stop.HOLD, wait=True)
    # Drive backward
    drivebase.straight(distance=-150, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=66, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=140, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=78, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=345, then=Stop.HOLD, wait=True)
    # Turn to face Mission 3
    drivebase.turn(angle=-102, then=Stop.HOLD, wait=True)
    # Complete Mission 3
    drivebase.straight(distance=320, then=Stop.HOLD, wait=True)


# Return back to base and collect Noah
def return_to_base():
    # Return to home
    drivebase.drive(speed=-900, turn_rate=24)
    # Wait
    wait(5000)


# MAIN PROGRAM
# ============
solve_missions_3_2()
return_to_base()
