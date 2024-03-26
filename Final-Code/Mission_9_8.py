# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# CONSTANTS
# =========
STRAIGHT_SPEED = 101
STRAIGHT_ACC = 101
TURN_RATE = 70
TURN_ACC = 80


# VARIABLE (HUB)
# ==============
hub = InventorHub()

# VARIABLES (DRIVING MOTORS + DRIVEBASE)
# ======================================
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 56, 110)

# VARIABLES (ATTACHMENT MOTORS)
# =============================
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)

# FUNCTIONS
# =========

# Solve mission 3
# ---------------
def solve_mission_9_8():
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

# Main program
# ------------
solve_mission_9_8()
