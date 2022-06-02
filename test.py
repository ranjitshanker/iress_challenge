#!/usr/bin/python

##############################################################################
# test.py
# Toy robot coding challenge
# Date of creation: 1 June 2022
# Author: Ranjit
##############################################################################
"""
Runnable integration tests for  Toy robot coding challenge
Execute the command from command line: python test.py
"""

import unittest
from command import parse_commands

def strip_white_space(str):
    return str.replace(" ", "").replace("\t", "").lower()
   
class CheckRobot(unittest.TestCase):  
    def test_valid_1(self):   
        command_list = '\
        PLACE 0,0,NORTH\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 0, 1, NORTH"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 
 
    def test_valid_2(self):   
        command_list = '\
        PLACE 0,0,NORTH\n\
        LEFT\n\
        REPORT'
        expected_output = "Output: 0, 0, WEST"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 
 
    def test_valid_3(self):   
        command_list = '\
        PLACE 1,2, EAST\n\
        MOVE\n\
        MOVE\n\
        LEFT\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 3, 3, NORTH"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_invalid_cmd_4(self):   
        command_list = '\
        PLACE 0,0,NORTH\n\
        MOVER\n\
        LEFT\n\
        REPORT'
        expected_output = "Output: Invalid command or position or coordinates"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_invalid_cmd_5(self):   
        command_list = '\
        PLACER 0,0,NORTH\n\
        MOVE\n\
        LEFT\n\
        REPORT'
        expected_output = "Output: Invalid command or position or coordinates"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 
 
    def test_invalid_place_6(self):   
        command_list = '\
        PLACE 1,6,NORTH\n\
        MOVE\n\
        LEFT\n\
        REPORT'
        expected_output = "Output: Invalid command or position or coordinates"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_valid_prevent_fall_7(self):   
        command_list = '\
        PLACE 2,3,NORTH\n\
        MOVE\n\
        MOVE\n\
        MOVE\n\
        LEFT\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 1, 5, WEST"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 
  
    def test_valid_empty_8(self):   
        command_list = '\
        PLACE 2,3,SOUTH\n\
        \n\
        MOVE\n\
        MOVE\n\
        RIGHT\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 1, 1, WEST"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_valid_multi_place_9(self):   
        command_list = '\
        PLACE 2,3,SOUTH\n\
        MOVE\n\
        PLACE 3,3, EAST\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 4, 3, EAST"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_invalid_no_place_10(self): 
        command_list = '\
        MOVE\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: No PLACE command"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_invalid_no_report_11(self): 
        command_list = '\
        PLACE 2,3,SOUTH\n\
        MOVE'
        expected_output = "Output: No REPORT command"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_valid_comeback_fall_12(self): 
        command_list = '\
        PLACE 0,0,SOUTH\n\
        MOVE\n\
        RIGHT\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 0, 0, WEST"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_no_valid_command_13(self): 
        command_list = '\
        m'
        expected_output = "Output: No PLACE command"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_no_command_14(self): 
        command_list = ''
        expected_output = "Output: Empty input command"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_ignore_till_place_15(self): 
        command_list = '\
        MOVE\n\
        RIGHT\n\
        REPORT\n\
        PLACE 0,0,EAST\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 1, 0, EAST"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_invalid_place_16(self):   
        command_list = '\
        PLACE 1,6,NORTH\n\
        REPORT'
        expected_output = "Output: Invalid command or position or coordinates"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 

    def test_valid_no_file_17(self): 
        expected_output = "Output: 3, 5, NORTH"
        with open('./test_files/directions.txt', 'r', encoding="utf-8") as file:
            self.assertEqual(parse_commands(file.read().lower()), expected_output) 

    def test_valid_empty_file_18(self): 
        expected_output = "Output: Empty input command"
        with open('./test_files/empty.txt', 'r', encoding="utf-8") as file:
            self.assertEqual(parse_commands(file.read().lower()), expected_output) 

    def test_valid_junk_file_19(self): 
        expected_output = "Output: Invalid command or position or coordinates"
        with open('./test_files/junk.txt', 'r', encoding="utf-8") as file:
            self.assertEqual(parse_commands(file.read().lower()), expected_output) 

    def test_boundary_20(self):   
        command_list = '\
        PLACE 4,5, NORTH\n\
        MOVE\n\
        REPORT'
        expected_output = "Output: 4, 5, NORTH"
        self.assertEqual(parse_commands(strip_white_space(command_list)), expected_output) 
    
if __name__ == '__main__':  
    unittest.main()