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
TURN_RATE = 80
TURN_ACC = 85


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
left_attachment_motor = Motor(port=Port.B)
right_attachment_motor = Motor(port=Port.A)

# VARIABLES (SENSORS)
# ===================
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)


# FUNCTIONS
# =========

def solve_mission_4():
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)
    drivebase.straight(distance=550, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=60, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=30, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=570, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=190, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-190, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=43, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=235, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=80, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=900, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=1220, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_mission_4()
