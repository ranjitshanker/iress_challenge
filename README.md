# Toy Robot Code Challenge
*Written by Ranjit S*

-------------------------
Challenge
-------------------------
Create a console application that can read in commands of the following form:

     PLACE X,Y,F
     MOVE
     LEFT
     RIGHT
     REPORT

Input:
1. Input can be from a file, or from standard input.

Placement constraints.
1. The first command to the robot must be a PLACE command.
2. Discard all commands in the sequence until a valid PLACE command has been executed.
3. A robot that is not on the table can ignore MOVE, LEFT, RIGHT and REPORT commands.
4. Initial placement of the toy robot should not cause the robot to fall off the table 
5. Application should handle error states appropriately and be robust to user input

Movement constraints
1. Move the toy robot one unit forward in the direction it is currently facing.
2. Any movement that would result in the robot falling from the table must be prevented,
3. However further valid movement commands must still be allowed.
-------------------------
Files
-------------------------
File | Description
--- | ---
README.md | The README file.
config.ini |  Configuration file. Defines step sizes, max and min coordinates, positions, and movements.
robot.py |  Start point for the app. Accepts inputs from file or from standard input. The commands are passed to command.py.
command.py |  check the validity of the commands (movements, coordinates and position) before passing them to movement.py.
movement.py | performs turn (left, right), move (in the direction of the turn) depending on the step_size defined in config.ini. Returns the final position when REPORT is encountered.
test.py | A test script performing 20 test cases.
results.txt | Output of commands executed through the standard input.
directions.txt |  An example file containing valid commands.
\test_files\empty.txt |  A test file in 'test_files' folder, that contains no commands (i.e. empty file).
\test_files\junk.txt |  A test file in 'test_files' folder, that contains invalid commands.
\test_files\directions.txt | A test file in 'test_files' folder, that contains valid commands.
-------------------------
Testing
-------------------------
Function | Description
--- | ---
test_valid_1 | Example a given in the code challenge
test_valid_2 | Example b given in the code challenge
test_valid_3 | Example c given in the code challenge
test_invalid_cmd_4 | Invalid movement command (eg: MOVER)
test_invalid_cmd_5 | Invalid placement command (eg: PLACER)
test_invalid_place_6 | Invalid placement coordinates (eg: PLACE 1,6,NORTH) and trying to MOVE
test_valid_prevent_fall_7 | Prevent falling off from table
test_valid_empty_8 | Ignore any empty commands
test_valid_multi_place_9 | Multiple place commands
test_invalid_no_place_10 | No PLACE command provided by user
test_invalid_no_report_11 | No REPORT command provided by user
test_valid_comeback_fall_12 | prevent falling and remain at the previous stable position
test_no_valid_command_13 | no valid command
test_no_command_14 | empty command
test_ignore_till_place_15 | Ignore previous commands until PLACE is encountered
test_invalid_place_16 | Invalid placement coordinates (eg: PLACE 1,6,NORTH) (different from test_invalid_place_6)
test_valid_no_file_17 | valid commands from file
test_valid_empty_file_18 | empty file 
test_valid_junk_file_19 | invalid commands from file 
test_boundary_20 | test boundary cases
```
python test.py
....................
----------------------------------------------------------------------
Ran 20 tests in 0.007s

OK
```
-------------------------
Features
-------------------------
1. Ignores empty input comands.
2. If typo commands has to be ignored, need to uncomment 2 lines in command.py
3. Use of config.ini to check for valid positions, movements and coordinates. Can be used to add more commands and constraints.
-------------------------
Setup and Execution
-------------------------
1. Download the repository https://github.com/ranjitshanker/iress_challenge
2. Python must be already installed in the system.
3. From the folder iress_challenge, execute the following commands:

a. To run the challenge with **file input**: `python robot.py directions.txt`

b. To run the challenge with **standard input**: `python robot.py`

c. To run **test cases**: `python test.py`

-------------------------
Note on running the script on standard input
-------------------------
1. As mentioned before, the user need to execute the command: *python robot.py* from the console. It will display a message: *Enter commands line by line , type exit to quit*.
2. User can enter commands and when finally done, type *exit* to quit from the application.
3. Whenever the user types *REPORT*, then the application will check if the Robot is on the table (i.e. a previous valid PLACE command). If yes, it will show its position on the table. Otherwise, no position is dispayed.
4. Please refer *results.txt* for output of various commands executed through the standard input.


