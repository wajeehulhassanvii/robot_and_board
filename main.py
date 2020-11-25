"""
Author: Wajeeh Ul Hassan
Email: wajeehulhassan_vii@hotmail.com
Contact number: 0411-773-990
"""
from models.position import Position
from models.board import Board
from models.robot import Robot

# Assuming directions and coordinates to be as below:
"""                             N,M
                  N
          W               E
 0,0              S


"""


COMMAND_LIST = """PLACE 0 0 NORTH
MOVE
REPORT
PLACE 0 0 NORTH
LEFT
REPORT
PLACE 1 2 EAST
MOVE
MOVE
LEFT
MOVE
REPORT"""

COMMAND_LIST = COMMAND_LIST.split("\n")

if __name__ == "__main__":
    initial_position = Position(0, 0)
    initial_direction = "NORTH"
    board = Board(5, 5)

    robot = Robot(position=initial_position,
                  direction=initial_direction,
                  board=board)

    for command in COMMAND_LIST:
        robot.execute_line_command(command)

