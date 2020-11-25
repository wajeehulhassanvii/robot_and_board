import unittest
from unittest import TestCase

from models.position import Position
from models.board import Board
from models.robot import Robot


class TestRobot(TestCase):
    def test_robot_initialization(self):
        """Test robot initialization with public and board variable"""
        position = Position(2, 3)
        board = Board(5, 5)
        robot = Robot(position, "NORTH", board)
        self.assertEqual(f"X: {position.x} Y: {position.y} Direction: NORTH", robot.report())

    def test_turn_left(self):
        """Test different scenarios of turn left function"""
        position = Position(2, 3)
        board = Board(5, 5)
        robot = Robot(position, "NORTH", board)
        robot.turn_left()
        self.assertEqual(robot.direction, "WEST")
        robot.turn_left()
        self.assertEqual(robot.direction, "SOUTH")
        robot.turn_left()
        self.assertEqual(robot.direction, "EAST")
        robot.turn_left()
        self.assertEqual(robot.direction, "NORTH")

    def test_turn_right(self):
        """Test different scenarios of turn right function"""
        position = Position(2, 3)
        board = Board(5, 5)
        robot = Robot(position, "NORTH", board)
        robot.turn_right()
        self.assertEqual(robot.direction, "EAST")
        robot.turn_right()
        self.assertEqual(robot.direction, "SOUTH")
        robot.turn_right()
        self.assertEqual(robot.direction, "WEST")
        robot.turn_right()
        self.assertEqual(robot.direction, "NORTH")
        robot.turn_right()
        self.assertEqual(robot.direction, "EAST")

    def test_move_forward(self):
        """Test different scenarios of move forward function"""
        position = Position(4, 4)
        board = Board(5, 5)
        robot = Robot(position, "NORTH", board)
        robot.move_forward()
        self.assertEqual(robot.position.y, position.y)

        position = Position(4, 4)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.move_forward()
        self.assertEqual(robot.position.x, position.x)

        position = Position(2, 2)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.move_forward()
        self.assertEqual(robot.position.x, 3)

        position = Position(2, 2)
        board = Board(5, 5)
        robot = Robot(position, "NORTH", board)
        robot.move_forward()
        self.assertEqual(robot.position.y, 3)

    def test_change_position(self):
        """Test the change position function, when the robot has already been initialized"""
        new_position = Position(2, 2)
        position = Position(4, 4)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.change_position(new_position, "WEST")
        self.assertEqual(robot.position, new_position)
        self.assertEqual(robot.direction, "WEST")

    def test_execute_line_command(self):
        """Test execute line command, test whether the robot acts according to the command given."""
        position = Position(4, 4)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.execute_line_command("RIGHT")
        self.assertEqual(robot.direction, "SOUTH")

        position = Position(4, 4)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.execute_line_command("LEFT")
        self.assertEqual(robot.direction, "NORTH")

        position = Position(4, 4)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.execute_line_command("MOVE")
        self.assertEqual(robot.position.x, position.x)

        position = Position(3, 3)
        board = Board(5, 5)
        robot = Robot(position, "NORTH", board)
        robot.execute_line_command("MOVE")
        self.assertEqual(robot.position.y, 4)

        position = Position(3, 3)
        board = Board(5, 5)
        robot = Robot(position, "EAST", board)
        robot.execute_line_command("MOVE")
        self.assertEqual(robot.position.x, 4)


if __name__ == "__main__":
    unittest.main()
