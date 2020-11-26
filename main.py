"""
Author: Wajeeh Ul Hassan
Email: wajeehulhassan_vii@hotmail.com
Contact number: 0411-773-990
"""
from pathlib import Path

from models.position import Position
from models.board import Board
from models.robot import Robot

# Assuming directions and coordinates to be as below:
"""                             N,M
                  N
          W               E
 0,0              S


"""


def read_command_file(filepath):
    return Path(filepath).read_text()


command_filepath = "command_list.txt"
COMMAND_LIST = read_command_file(command_filepath).split("\n")

if __name__ == "__main__":
    initial_position = Position(0, 0)
    initial_direction = "NORTH"
    board = Board(5, 5)

    robot = Robot(position=initial_position,
                  direction=initial_direction,
                  board=board)

    for command in COMMAND_LIST:
        robot.execute_line_command(command)
