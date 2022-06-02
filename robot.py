#!/usr/bin/python

##############################################################################
# robot.py
# Toy robot coding challenge
# Date of creation: 31 May 2022
# Author: Ranjit
##############################################################################
"""
Main file that accepts command line arguments
1. Input can be from a file, or from standard input.
2. Application should handle error states appropriately and be robust to user input
3. Create a console application that can read in commands of the following form -
     PLACE X,Y,F
     MOVE
     LEFT
     RIGHT
     REPORT
Method 1: Execute the command from command line: python robot.py <file_name.txt>
Method 2: Execute the command from command line: python robot.py 
"""
try:
    import configparser
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'configparser'])
finally:
    import configparser
import sys
from command import parse_commands

# To prevent ParsingError, set allow_no_value=True
# ref: https://stackoverflow.com/questions/51864289/configparser-parsingerror-source-contains-parsing-errors-my-ini
config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')

# fetch opening and ending tags of each command set
start_cmd=config['Constraints']['Start_command'].lower() #PLACE
end_cmd=config['Constraints']['Stop_command'].lower()   #REPORT

def main():
    len_arg = len(sys.argv)
    command_list = ""
    final_position = ""
    last_stable_position = ""
 
    if len_arg > 1  :
        file_name = sys.argv[1]  
        try:
            with open(file_name, 'r', encoding="utf-8") as file:
                # read all lines at once
                command_list = file.read()
        except IOError:
                print("ERROR!!Check the file")
                sys.exit(2) 
        # parse the list of commands
        final_position = parse_commands(command_list.lower())
        print(final_position)

    else:
        print("Enter commands line by line , type exit to quit")
        while True:          
            # rstrip() required because readlines does not strip newlines 
            # e.g.: If you type "exit", line will actually be "exit\n",
            line = sys.stdin.readline().rstrip('\n')
            if line.lower() == 'exit':
                print("Exiting the program")
                break
            else:
                # if not exit has been encountered, continue joining the commands
                command_list = '\n'.join([command_list,line]) 
                if start_cmd in line.lower():
                    # if PLACE command has been entered, check if it is a valid PLACE
                    # eg: [place 6,0,north] split to ['', '6,0,north']  the length = 2
                    check_place = line.lower().split(start_cmd) # split at place
                    check_place = [x.strip(' ') for x in check_place] # to be extra cautious
                    if len(check_place) == 2 and check_place[0] == '' and check_place[1]: 
                        check_place = check_place[1].split(',') # e.g. split [6,0,north']  at comma
                        check_place = [x.strip(' ') for x in check_place] # to be extra cautious
                        # Location must satisfy 0<=x<=5 and 0<=y<=5 and position must be (N,S,E,W)
                        if config['Constraints']['Xmin'] <= check_place[0] <= config['Constraints']['Xmax'] and \
                        config['Constraints']['Ymin'] <= check_place[1] <= config['Constraints']['Ymax'] and \
                        check_place[2] in config.options('Position'):
                            last_stable_position = line.lower()
                            command_list = last_stable_position
                        else:
                             # IF the robot is out of table, save the last stable to the command list
                            command_list = last_stable_position
                    else:
                         # This is an invalid PLACE command. eg: PLACE with 4 parameters
                        command_list = ""
                elif  line.lower() == end_cmd :
                    # if user entered REPORT, check  if   PLACE has already been entered.
                    if start_cmd not in command_list.lower():
                        # If PLACE is not entered yet, clear previous commands
                        command_list = ""
                    else:                  
                        final_position = parse_commands(command_list.lower())
                        print(final_position) 
                        if final_position != "Output: Invalid command or position or coordinates":
                            final_position = final_position.replace("Output:", "place")
                            command_list = final_position
                        else:
                            command_list = last_stable_position
                    
if __name__ == '__main__':
    main()