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
left_attachment_motor = Motor(port=Port.B)
right_attachment_motor = Motor(port=Port.A)

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
    drivebase.straight(distance=260, then=Stop.HOLD, wait=True)
    # Turn to face the mission
    drivebase.turn(angle=-50, then=Stop.HOLD, wait=True)
    # Drive into the mission
    drivebase.straight(distance=400, then=Stop.HOLD, wait=True)
    # Hook on to the craft creator lid
    right_attachment_motor.run_angle(speed=1000, rotation_angle=180,
                                     then=Stop.COAST, wait=False)
    # Hook on the lever for mission 12
    left_attachment_motor.run_angle(speed=1000, rotation_angle=100,
                                    then=Stop.COAST, wait=True)
    # Drive back to home
    drivebase.straight(distance=-700, then=Stop.HOLD, wait=True)


# MAIN PROGRAM
# ============
solve_mission_13_and_return_to_base()
