# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 100
STRAIGHT_ACC = 100
TURN_RATE = 100
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

# Sensors
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)


# FUNCTIONS Representing Robot Behaviors
# ======================================

# Solve Mission #2
def solve_m2():
    # Settings for drivebase
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Drive forward
    drivebase.straight(distance=600, then=Stop.HOLD, wait=True)


# Return to Base
def return_to_base():
    # Drive backward
    drivebase.straight(distance=-200, then=Stop.HOLD, wait=True)
    # Turn to face base
    drivebase.turn(angle=30, then=Stop.HOLD, wait=True)
    # Drive backward to go Home
    drivebase.straight(distance=-800, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_m2()
return_to_base()
