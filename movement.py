#!/usr/bin/python

##############################################################################
# movement.py
# Toy robot coding challenge
# Date of creation: 31 May 2022
# Author: Ranjit
##############################################################################
"""
Move the robot subject to the following constraints
1. Move the toy robot one unit forward in the direction it is currently facing.
2. Any movement that would result in the robot falling from the table must be prevented,
3. However further valid movement commands must still be allowed.
"""
try:
    import configparser
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'configparser'])
finally:
    import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')    
# fetch step size
step_size=int(config['Constraints']['Step_size'])

def check_table_limits(x,y):
    # check if robot's movements are within boundaries
    within_limits = False
    if int(config['Constraints']['Xmin']) <= x <= int(config['Constraints']['Xmax']) and \
    int(config['Constraints']['Ymin']) <= y <= int(config['Constraints']['Ymax']):
        within_limits = True
    return within_limits
    
class Robot():
    def __init__(self,full_command,x,y,position,exec_command): 
        # constructor to initialise variables
        self.full_command = [x.upper() for x in full_command]
        self.x = x
        self.y = y
        self.position = position
        self.exec_command = exec_command
        
    def turn(self, cmd, position):
        # change robot's orientation if user inputs Left/Right
        if cmd == 'left':
            if position == 'north':
                return 'west'
            elif position == 'south':
                return 'east'
            elif  position == 'east':
                return 'north'
            elif position == 'west':
                return 'south'
        else:
            if position == 'north':
                return 'east'
            elif position == 'south':
                return 'west'
            elif  position == 'east':
                return 'south'
            elif position == 'west':
                return 'north'
                
    def move(self, x,y,position):
        # prevent robot falling from the table
        # however further valid movement commands must still be allowed.
        if position == 'north':
            if check_table_limits(x,y+step_size):
                return x,y+step_size
            else:
                return x,y
        elif position == 'south':
            if check_table_limits(x,y-step_size):
                return x,y-step_size 
            else:
                return x,y               
        if position == 'east':
            if check_table_limits(x+step_size,y):
                return x+step_size,y
            else:
                return x,y            
        elif position == 'west':
            if check_table_limits(x-step_size,y):
                return x-step_size,y
            else:
                return x,y
                
    def print_cmd(self):
        for cmd in self.exec_command:
            if cmd == 'move':
                new_x,new_y=self.move(int(self.x),int(self.y),self.position)
                self.x = new_x
                self.y = new_y
            elif cmd == 'left' or cmd == 'right':
                new_position = self.turn(cmd, self.position)
                self.position = new_position
            else:
                print("Input: ",self.full_command,". Output: ",str(self.x)+', '+str(self.y)+', '+self.position.upper())


