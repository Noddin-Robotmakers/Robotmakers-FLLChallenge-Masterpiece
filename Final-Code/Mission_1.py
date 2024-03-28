# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 900
TURN_RATE = 900
TURN_ACC = 300


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

# Solve Mission #1 and Return to Base
def solve_m1_and_return_to_base():
    # Settings for drivebase
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Drive forward
    drivebase.straight(distance=400, then=Stop.HOLD, wait=True)
    # Drive backward
    drivebase.straight(distance=-40, then=Stop.HOLD, wait=True)
    # Drive forward
    drivebase.straight(distance=60, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(-15)

    # Drive backward to base
    drivebase.straight(distance=-400, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_m1_and_return_to_base()
