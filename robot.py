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
"""
import sys,getopt
from command import parse_commands

def usage():
    print("Usage: "+sys.argv[0]+ " -f <file_name> \nOR\nUsage: "+\
    sys.argv[0]+ " -c <commands>")    
    
def main():
    argv = sys.argv[1:]   
    file_commands = ""
    command_list = ""
    
    try:
        opts, args = getopt.getopt(argv, "f:c:")
        if not opts:
            print("ERROR!! No options supplied")
            usage()
    except getopt.GetoptError as err:
        # print help information and exit 
        # ref: #https://docs.python.org/3/library/getopt.html
        print("ERROR!! ",err)
        usage()
        # Unix programs use 2 for command line syntax errors 
        # and 1 for all other kind of errors 
        # ref: https://docs.python.org/3/library/sys.html
        sys.exit(2) 

    for opt, arg in opts:
        if opt in ['-f']:
            file_name = arg
            # open the file in read mode:
            # ref: https://docs.python.org/3/tutorial/inputoutput.html
            with open(file_name, 'r', encoding="utf-8") as file:
                # read all lines at once
                command_list = file.read()
        elif opt in ['-c']:
            command_list = arg            
        """else:
            #ref: https://docs.python.org/3/library/getopt.html
            print("Unhandled option" )
            usage()
            sys.exit(2)"""
 
    # parse the list of commands
    parse_commands(command_list)
        
if __name__ == '__main__':
    main()