import unittest
from unittest import TestCase

from models.board import Board
from models.position import Position


class TestBoard(TestCase):

    def setUp(self):
        """load common test data"""
        pass

    def test_board_initialization(self):
        """Test the initialization of the board"""
        board = Board()
        self.assertEqual(board.MAX_M, 5)
        self.assertEqual(board.MAX_N, 5)

    def test_negative_board_initialization(self):
        """Test that board does not get initialized with negative values"""
        board = Board(-1, -2)
        self.assertEqual(board.MAX_M, 1)
        self.assertEqual(board.MAX_N, 1)

    def test_move_available_in_direction(self):
        """Test whether robot can move in given direction."""
        board = Board(5, 5)
        position1 = Position(4, 4)
        position2 = Position(0, 2)
        position3 = Position(3, 1)
        position4 = Position(3, 4)
        position_mid = Position(2, 3)

        direction_n = "NORTH"
        direction_s = "SOUTH"
        direction_e = "EAST"
        direction_w = "WEST"

        ma_1_n = board.move_available_in_direction(position1, direction_n)
        self.assertEqual(ma_1_n, False)

        ma_1_s = board.move_available_in_direction(position1, direction_s)
        self.assertEqual(ma_1_s, True)

        ma_2_w = board.move_available_in_direction(position2, direction_w)
        self.assertEqual(ma_2_w, False)

        ma_3_s = board.move_available_in_direction(position3, direction_s)
        self.assertEqual(ma_3_s, True)

        ma_4_n = board.move_available_in_direction(position3, direction_n)
        self.assertEqual(ma_4_n, True)

        ma_1_e = board.move_available_in_direction(position1, direction_e)
        self.assertEqual(ma_1_e, False)

        ma_4_e = board.move_available_in_direction(position4, direction_n)
        self.assertEqual(ma_4_e, False)

        ma_m_e = board.move_available_in_direction(position_mid, direction_e)
        self.assertEqual(ma_m_e, True)
        ma_m_e = board.move_available_in_direction(position_mid, direction_w)
        self.assertEqual(ma_m_e, True)


if __name__ == "__main__":
    unittest.main()
