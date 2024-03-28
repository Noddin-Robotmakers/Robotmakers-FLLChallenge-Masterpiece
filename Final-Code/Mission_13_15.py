# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
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


# FUNCTIONS Representing Robot Behaviors
# ======================================

# solve mission 13 and return home
def solve_mission_13_and_return_to_base():
    # Settings for drivebase
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Drive forward
    drivebase.straight(distance=280, then=Stop.HOLD, wait=True)

    # Turn to face the mission
    drivebase.turn(angle=-54, then=Stop.HOLD, wait=True)

    # Drive into the mission
    drivebase.straight(distance=115, then=Stop.HOLD, wait=True)
    # Grab the expert
    right_attachment_motor.run_angle(speed=1000, rotation_angle=-150,
                                     then=Stop.COAST, wait=True)
    # Turn to face the mission
    drivebase.turn(angle=8, then=Stop.HOLD, wait=True)
    # Drive into the mission
    drivebase.straight(distance=170, then=Stop.HOLD, wait=True)

    # Drive back
    drivebase.straight(distance=14, then=Stop.HOLD, wait=False)

    # Turn the chicken
    right_attachment_motor.run_angle(speed=1000, rotation_angle=1000,
                                     then=Stop.COAST, wait=False)

    # Hook on the lever for mission 12
    left_attachment_motor.run_angle(speed=1000, rotation_angle=720,
                                    then=Stop.COAST, wait=True)

    # Change drivebase speed to go back to Home
    drivebase.settings(straight_speed=900,
                       straight_acceleration=900,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)

    # Drive backwards
    drivebase.straight(distance=-600, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_mission_13_and_return_to_base()
