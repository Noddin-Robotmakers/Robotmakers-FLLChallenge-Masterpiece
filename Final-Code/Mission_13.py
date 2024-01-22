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
# ======================================
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

# solve mission 13
# ----------------
def solve_mission_13_and_return_to_base():
    # Settings for drivebase
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE,
                       turn_acceleration=TURN_ACC)
    # Drive forward
    drivebase.straight(distance=240, then=Stop.HOLD, wait=True)
    # Turn to face the mission
    drivebase.turn(angle=-47, then=Stop.HOLD, wait=True)
    # Drive into the mission
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)
    # Hook on to the craft creator lid
    right_attachent_motor.run_angle(speed=1000, rotation_angle=-150,
                                    then=Stop.COAST, wait=True)
    # Turn to face the mission
    drivebase.turn(angle=5, then=Stop.HOLD, wait=True)
    # Drive into the mission
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)
    
    # Drive back
    drivebase.straight(distance=8, then=Stop.HOLD, wait=False)

    # Hook on to the craft creator lid
    right_attachent_motor.run_angle(speed=1000, rotation_angle=150,
                                    then=Stop.COAST, wait=False)

    # Hook on the lever for mission 12
    left_attachent_motor.run_angle(speed=1000, rotation_angle=720,
                                   then=Stop.COAST, wait=True)
    # Drive backwards
    drivebase.straight(distance=-360, then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=-55, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=300, then=Stop.HOLD, wait=True)
    # Hook on the lever for mission 8
    left_attachent_motor.run_angle(speed=1000, rotation_angle=155,
                                   then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(angle=10, then=Stop.HOLD, wait=True)
    # Go forward
    drivebase.straight(distance=380, then=Stop.HOLD, wait=True)
    # Drive back to home
    left_attachent_motor.run_angle(speed=1000, rotation_angle=-160,
                                   then=Stop.COAST, wait=True)
    drivebase.straight(distance=-1050, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_mission_13_and_return_to_base()
