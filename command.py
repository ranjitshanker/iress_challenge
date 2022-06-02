#!/usr/bin/python

##############################################################################
# command.py
# Toy robot coding challenge
# Date of creation: 31 May 2022
# Author: Ranjit
##############################################################################
"""
Parse the  list of commands and apply the below constraints.
1. The first command to the robot must be a PLACE command.
2. Discard all commands in the sequence until a valid PLACE command has been executed.
3. A robot that is not on the table can ignore MOVE, LEFT, RIGHT and REPORT commands.
4. Initial placement of the toy robot should not cause the robot to fall off the table 
"""
try:
    import configparser
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'configparser'])
finally:
    import configparser
import re    
from movement import Robot

# To prevent ParsingError, set allow_no_value=True
# ref: https://stackoverflow.com/questions/51864289/configparser-parsingerror-source-contains-parsing-errors-my-ini
config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')

# fetch opening and ending tags of each command set
start_cmd=config['Constraints']['Start_command'].lower() #PLACE
end_cmd=config['Constraints']['Stop_command'].lower()   #REPORT
    
def check_command(command):
    # this function receives a set of commands between PLACE and REPORT
    final_position = "Output: Invalid command or position or coordinates" # commands outside the scope
    sub_cmd_list = []
    # split this set of commands by new line
    sub_cmd_list = command.splitlines()
    # Strip leading and trailing empty characters eg: ['2,3,SOUTH', '        MOVE']
    sub_cmd_list = [x.strip(' ').lower() for x in sub_cmd_list] 
    # Remove empty strings eg: ['2,3,SOUTH', '', 'MOVE']
    sub_cmd_list = [x for x in sub_cmd_list if x]
    # Finally we have a command set as shown below
    # eg: [' 1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE']
    # The first command is ALWAYS of the form X,Y, Position.
    if sub_cmd_list[0]:  # check if first command is present
        check_place = sub_cmd_list[0].split(",") # split the place command into X,Y, Position
        check_place = [x.strip(' ') for x in check_place] # to be extra cautious
        if len(check_place) == 3: # there MUST be X, Y and Position
            # Location must satisfy 0<=x<=5 and 0<=y<=5 and position must be (N,S,E,W)
            if config['Constraints']['Xmin'] <= check_place[0] <= config['Constraints']['Xmax'] and \
            config['Constraints']['Ymin'] <= check_place[1] <= config['Constraints']['Ymax'] and \
            check_place[2] in config.options('Position'):
                # There can be no more commands (i.e. cases of PLACE,REPORT ) 
                # OR (i.e. cases of PLACE,<command>, REPORT), they must be MOVE or LEFT or RIGHT
                if len(sub_cmd_list[1:]) < 1 or \
                all(elements in config.options('Commands') for elements in [x for x in sub_cmd_list[1:]]):
                    # Concat PLACE to start of command set  
                    sub_cmd_list[0]=start_cmd+' '+sub_cmd_list[0]
                    # To ignore any typo mistakes by user in MOVE,LEFT or RIGHT, uncomment below
                    #sub_cmd_list[1:] = [x for x in sub_cmd_list[1:] if x.lower() in config.options('Commands')]   
                    # Concat REPORT to end of command set  
                    sub_cmd_list.append(end_cmd)  
                    # Pass full_command_set, coordinates, and set of commands after PLACE, to the Robot
                    robot = Robot(sub_cmd_list,check_place[0],check_place[1],\
                    check_place[2],[x for x in sub_cmd_list[1:]])
                    final_position = robot.print_cmd()  
    return final_position
    
def parse_commands(command_list):
    new_command_list=[]   
    final_position = ""
    # Users can input commands with or without quotes. Remove all single & double for uniformity.
    if command_list.strip() != '':
        command_list= re.sub("[\"\']", "", command_list)
        # Fetch the commands between PLACE (start_cmd) & REPORT (end_cmd)
        # To do this, first split the entire command list at PLACEs
        if start_cmd in command_list:
            split_at_place=command_list.split(start_cmd)
            # fetch each of the command set
            for each_set in split_at_place:
                # Then split each of the command at REPORT.
                if end_cmd in each_set:  
                    # We now fetched commands BETWEEN PLACE & REPORT
                    # Check if these commands are valid
                    cmd_between = each_set.split(end_cmd)[0]
                    final_position = check_command(cmd_between)
                else:
                    final_position = "Output: No REPORT command"
        else:
            final_position = "Output: No PLACE command"
    else:
        final_position = "Output: Empty input command"
    return final_position
