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

# Solve Mission #6
def solve_m6():
    # Settings for drive
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Drive forward
    drivebase.straight(850)
    # Drive back
    drivebase.straight(-140)
    # Turn to face mission
    drivebase.turn(40)
    # Drive into mission
    drivebase.straight(230)
    # Do the speakers
    left_attachment_motor.run_angle(speed=1000, rotation_angle=-270,
                                    then=Stop.COAST, wait=True)
    # Drive back
    drivebase.straight(-100)


# Return to Base
def return_to_base():
    # Turn
    drivebase.turn(-60)
    # Drive back to home
    drivebase.straight(-1300)


# MAIN PROGRAM
# ============
solve_m6()
return_to_base()
