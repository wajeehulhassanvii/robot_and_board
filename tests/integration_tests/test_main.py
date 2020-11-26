import unittest
from unittest import TestCase, mock
from unittest.mock import patch

patch_read_command_file = patch('robot_and_board.main.read_command_file',
                                return_value="RIGHT\nLEFT")


class TestMain(TestCase):
    @mock.patch('main.read_command_file', return_value="RIGHT\nLEFT")
    def test_read_command_file(self, mock_read_command_file):
        self.assertEqual(len(mock_read_command_file("./command_list.txt").split("\n")), 2)


if __name__ == "__main__":
    unittest.main()
