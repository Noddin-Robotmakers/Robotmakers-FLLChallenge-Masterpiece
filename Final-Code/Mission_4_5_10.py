# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Stop
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
right_color_sensor = (Port.E)
left_color_sensor = (Port.F)


# FUNCTIONS
# =========
def solve_mission_4():
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)
    drivebase.straight(distance=-60, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=40, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-400, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=50, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-350, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-300, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=-120, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=250, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=-60, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=70, then=Stop.HOLD, wait=True)
    right_attachent_motor.run_angle(speed=500, rotation_angle=100,
                                    then=Stop.HOLD, wait=True)
    drivebase.straight(distance=-100, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=50, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=195, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=40, then=Stop.HOLD, wait=True)
    drivebase.straight(distance=80, then=Stop.HOLD, wait=True)
    drivebase.turn(angle=35, then=Stop.HOLD, wait=True)
    drivebase.drive(speed=400, turn_rate=15)
    wait(4000)
    drivebase.stop()


# MAIN PROGRAM
# ============
solve_mission_4()
