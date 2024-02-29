# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# CONSTANTS
# =========
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
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
def solve_mission_3():
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)                
    # Drive from the home area to mission 2
    drivebase.straight(distance=620, then=Stop.HOLD, wait=True)
    drivebase.turn(-3)
    # Drive forward
    drivebase.straight(distance=215, then=Stop.HOLD, wait=True)
    # Drive backwards
    drivebase.straight(distance=-150, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=86, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=140, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=53, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=330, then=Stop.HOLD, wait=True)
    # Turn to face mission 3
    drivebase.turn(angle=-106, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=320, then=Stop.HOLD, wait=True)
    

# Return back to base
# -------------------


def return_to_base():
    # Return to home
    drivebase.drive(speed=-900, turn_rate=24)
    # Wait
    wait(5000)

solve_mission_3()
return_to_base()
