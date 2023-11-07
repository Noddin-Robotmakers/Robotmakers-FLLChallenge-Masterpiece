#################################################################################
# IMPORTS                                                                       #
#################################################################################

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


#################################################################################
# CONSTANTS                                                                     #
#################################################################################

STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 80
TURN_ACC = 85


#################################################################################
# VARIABLES                                                                     #
#################################################################################

# The Hub
hub = InventorHub()

# Driving Motors and Drivebase                                        #
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 56, 110)

# Attachment Motors
left_attachent_motor = Motor(port=Port.B)
right_attachent_motor = Motor(port=Port.A)

# Sensors
right_color_sensor = ColorSensor(Port.E)
left_color_sensor = ColorSensor(Port.F)


#################################################################################
# FUNCTIONS                                                                     #
#################################################################################

#################################################################################
# Function for following the line                                               #
#################################################################################

def follow_the_line():
    
    if (left_color_sensor.color() == Color.NONE) or (right_color_sensor.color() == Color.NONE):
        
        #########################################################################
        # Checks if the color detected is black and moves forward if it is.     #
        #########################################################################

        left_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
        right_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
    
    else:
        
        while (left_color_sensor.color() != Color.NONE) or (right_color_sensor.color() != Color.NONE):
            
            #####################################################################################
            # If there is no black then go left and then if still no black then it moves right. #
            #####################################################################################
            
            left_motor.run_angle(speed=-700, rotation_angle=10, then=Stop.HOLD, wait=False)
            if (left_color_sensor.color() != Color.NONE) or (right_color_sensor.color() != Color.NONE):
                while (left_color_sensor.color() != Color.NONE) or (right_color_sensor.color() != Color.NONE):
                    right_motor.run_angle(speed=-700, rotation_angle=10, then=Stop.HOLD, wait=False)
                    if (left_color_sensor.color() == Color.NONE) or (right_color_sensor.color() == Color.NONE):
                        left_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)
                        right_motor.run_angle(speed=-700, rotation_angle=30, then=Stop.HOLD, wait=False)

#################################################################################
# Function to solve Mission 3                                                   #
#################################################################################

def solve_mission_3():

    #############################################################################
    # Drivebase settings for speed and acceleration                             #
    #############################################################################
    
    drivebase.settings(straight_speed=STRAIGHT_SPEED,
                       straight_acceleration=STRAIGHT_ACC,
                       turn_rate=TURN_RATE, 
                       turn_acceleration=TURN_ACC)

    #############################################################################
    # Drive to Mission 3                                                        #
    #############################################################################

    # Drive from the home area to next to Mission 2.
    drivebase.straight(distance=605, then=Stop.HOLD, wait=True)
    # Turn to the right to face the mission.
    drivebase.turn(angle=90, then=Stop.HOLD, wait=True)
    # Drive in front of Mission 3.
    drivebase.straight(distance=556, then=Stop.HOLD, wait=True)
    # Turn left to face Mission 3.
    drivebase.turn(angle=-90, then=Stop.HOLD, wait=True)

    #############################################################################
    # Turn to Mission 3 in order to get ready to perform the mission            #
    #############################################################################

    # Wait for half a second to stabilize.
    wait(500)
    # Jerk preparation since it jerks because the design is a bit faulty.
    drivebase.turn(1)
    # Drive into Mission 3.
    # It jerks to the left, negating the 1 degree the robot turned earlier. 
    drivebase.straight(distance=100, then=Stop.HOLD, wait=True)
    # Stabilize to make sure it does not go an extra few millimeters forward or backward.
    wait(500)
    
    #############################################################################
    # Perform Mission 3                                                         #
    #############################################################################

    # Turn left to finish the mission by pushing one screen up, 
    # resulting in all the other ones to go up as well.
    drivebase.turn(angle=-40, then=Stop.HOLD, wait=True)
    # Stabilize to make sure the robot does not turn an extra few degrees right or left 
    # and to make sure the screens stay up.
    wait(500)
    # Turn right (back) to its position before the screens were up.
    drivebase.turn(angle=20, then=Stop.HOLD, wait=True)


#################################################################################
# Return to home base after completing Mission 3.                               #
#################################################################################

def return_to_base():
    # Back up.
    drivebase.straight(distance=-110, then=Stop.HOLD, wait=True)
    # Turn to face the back of the robot to the rolling camera.
    drivebase.turn(angle=20, then=Stop.HOLD, wait=True)
    # Back up.
    drivebase.straight(distance=-480, then=Stop.HOLD, wait=True)
    # Turn to face the back of the robot to the home area.
    drivebase.turn(angle=-120, then=Stop.HOLD, wait=True)
    # Drive backwards to go into the home area.
    drivebase.straight(distance=500, then=Stop.HOLD, wait=True)

#################################################################################
# MAIN PROGRAM                                                                  #
#################################################################################
solve_mission_3()
return_to_base()
