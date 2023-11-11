# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS
# =========
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 70
TURN_ACC = 70


# VARIABLE (HUB)
# ==============
hub = InventorHub()

# VARIABLES (DRIVING MOTORS + DRIVEBASE)
# ==============================
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
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

# Solve mission 3
# ---------------

def solve_mission_3():
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
    # Drive from the home area to mission 2
    drivebase.straight(distance=575, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=40, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=180, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=60, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=332, then=Stop.HOLD, wait=True)
    # Turn to face mission
    drivebase.turn(angle=-87, then=Stop.HOLD, wait=True)
    # Do the mission
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)

# Return back to base
# -------------------


def return_to_base():
    # Drive backward
    drivebase.straight(distance=-600, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)
    # Drive backwards
    drivebase.straight(distance=800, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_mission_3()
return_to_base()
