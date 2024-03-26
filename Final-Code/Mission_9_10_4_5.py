# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
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
left_attachment_motor = Motor(port=Port.B)
right_attachment_motor = Motor(port=Port.A)

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
    
    # Forward 
    drivebase.straight(distance=-65, then=Stop.HOLD, wait=True)
    # Turn to face M10
    drivebase.turn(angle=44, then=Stop.HOLD, wait=True)
    drivebase.settings(straight_speed=300,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)
    # Ram into M10
    drivebase.straight(distance=-430, then=Stop.HOLD, wait=True)
    # Back up
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)
    # Turn 
    drivebase.turn(angle=-140, then=Stop.HOLD, wait=True)
    # Drive past M10
    drivebase.straight(distance=230, then=Stop.HOLD, wait=True)
    # Turn to face museum
    drivebase.turn(angle=-45, then=Stop.HOLD, wait=True)
    # Drive to museum
    drivebase.straight(distance=635, then=Stop.HOLD, wait=True)
    # Release flap
    right_attachment_motor.run_angle(speed=500, rotation_angle=100,
                                     then=Stop.HOLD, wait=True)
    drivebase.turn(-30)                                  
    # Back up
    drivebase.straight(distance=-135, then=Stop.HOLD, wait=True)
    # Turn to face M5
    drivebase.turn(angle=40, then=Stop.HOLD, wait=True)
    # Drive past museum, and near M5
    drivebase.straight(distance=175, then=Stop.HOLD, wait=True)
    # Half finish M5
    drivebase.turn(angle=44, then=Stop.HOLD, wait=True)
    drivebase.settings(straight_speed=900,
                       straight_acceleration=900,
                       turn_rate=100,
                       turn_acceleration=85)
    # Finish M5
    drivebase.straight(distance=95, then=Stop.HOLD, wait=True)
    # Home base
    drivebase.drive(speed=400, turn_rate=20)
    wait(4000)
    drivebase.stop()


# MAIN PROGRAM
# ============
solve_mission_4()
