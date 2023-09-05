# ----------------------------------------------------------------------------- #
#                                                                               #              
#    Project:        SmokingThatVexPak                                          #
#    Module:         main.py                                                    #
#    Author:         Chase Hutcheson, Landon Hahn                               #
#    Created:        August 25 2023                                             #
#    Description:    Team 7882Z Robot Code                                      # 
#                                                                               #
#                                                                               #                                                                          
#    Configuration:  None                                                       #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Define Motors
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
# Define Controller
controller = Controller(ControllerType.PRIMARY)

# Define Autonomous
def autonomous():
    brain.screen.print("No Auton Yet :(")

# Driver Control Function
def driver_control():
    while True:
        # Gets Controller Joystick Axis Position and Labels them as Speed
        left_speed = controller.axis3.position()
        right_speed = controller.axis2.position()

        # Makes Motor Spin via Joystick Position (Note: -position means reverse)
        left_motor.spin(DirectionType.FORWARD, left_speed, VelocityUnits.PERCENT)
        right_motor.spin(DirectionType.FORWARD, right_speed, VelocityUnits.PERCENT)
            
competition = Competition(driver_control, autonomous)