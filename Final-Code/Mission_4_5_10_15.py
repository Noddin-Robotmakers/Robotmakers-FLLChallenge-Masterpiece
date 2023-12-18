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
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)

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
    drivebase.straight(distance=-60, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=40, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-100, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=100, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-270, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=15, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=-15, then=Stop.HOLD, wait=True)
    drivebase.settings(straight_speed=300,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)
    drivebase.straight(distance=-200, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_mission_4()
