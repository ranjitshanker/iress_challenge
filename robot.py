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
"""
import sys
from command import parse_commands
    
def main():
    len_arg = len(sys.argv)
    command_list = ""
 
    if len_arg > 1  :
        file_name = sys.argv[1]  
        try:
            with open(file_name, 'r', encoding="utf-8") as file:
                # read all lines at once
                command_list = file.read()
        except IOError:
                print("ERROR!!Check the file")
                sys.exit(2) 
    else:
        print("Enter commands line by line , type exit to quit")
        while True:          
            # rstrip() required because readlines does not strip newlines 
            # e.g.: If you type "exit", line will actually be "exit\n",
            line = sys.stdin.readline().rstrip('\n')
            if line.lower() == 'exit':
                break
            else:
                command_list = '\n'.join([command_list,line])
 
    # parse the list of commands
    parse_commands(command_list)
        
if __name__ == '__main__':
    main()