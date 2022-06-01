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
however further valid movement commands must still be allowed.
"""
class Robot():
    def __init__(self,full_command,x,y,position,exec_command):
        self.full_command = full_command
        self.x = x
        self.y = y
        self.position = position
        self.exec_command = exec_command
    
    def print_cmd(self):
        print("INPUT=",self.full_command,". X=",self.x,". Y=",self.y,". Position=",self.position,". Execute=",self.exec_command)