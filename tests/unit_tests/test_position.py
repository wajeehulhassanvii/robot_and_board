import unittest
from unittest import TestCase

from models.position import Position


class TestPosition(TestCase):

    def test_position_constructor(self):
        """Test the constructor of Position object"""
        x = 1
        y = 3
        position = Position(x, y)
        self.assertEqual(position.x, x)
        self.assertEqual(position.y, y)

    def test_negative_position(self):
        """Test whether position get initialized with less than MIN coordinates """
        x = -1
        y = 3
        position = Position(x, y)
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, y)

    def test_empty_initialization(self):
        """Test that position is getting initialized with default values if the value has not been given"""
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)


if __name__ == '__main__':
    unittest.main()
