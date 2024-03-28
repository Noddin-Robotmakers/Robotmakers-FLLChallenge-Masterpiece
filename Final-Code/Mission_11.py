# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 80
TURN_ACC = 85


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

# solve Mission #11
def solve_m11():
    # Settings for drivebase
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Go forward
    drivebase.straight(200)
    # Turn
    drivebase.turn(-90)
    # Go forward
    drivebase.straight(700)
    # Turn
    drivebase.turn(95)
    # Go forward
    drivebase.straight(155)
    # Do M11
    right_attachment_motor.run_angle(speed=1000, rotation_angle=1650,
                                     then=Stop.COAST, wait=True)


# Return to other home Base
def return_to_other_base():
    # Go forward
    drivebase.straight(-155)
    # Turn
    drivebase.turn(-90)
    # Go forward
    drivebase.straight(300)
    # Turn
    drivebase.turn(-90)
    # Go forward
    drivebase.straight(200)
    # Turn
    drivebase.turn(-90)
    # Go forward
    drivebase.straight(200)
    # Turn
    drivebase.turn(-90)


# MAIN PROGRAM
# ============
solve_m11()
return_to_other_base()
