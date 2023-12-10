# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port,  Stop
from pybricks.robotics import DriveBase


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
def solve_mission_10():
    drivebase.settings(straight_speed=130, straight_acceleration=900,
                       turn_rate=80, turn_acceleration=85)
    right_attachent_motor.run_angle(speed=100, rotation_angle=180,
                                    then=Stop.HOLD, wait=True)
    drivebase.turn(30)


solve_mission_10()
