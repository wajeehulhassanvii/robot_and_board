import unittest
from unittest import TestCase, mock
from unittest.mock import patch


class TestMain(TestCase):
    # Mock and test the read_command_file function in the main
    @mock.patch('main.read_command_file', return_value="RIGHT\nLEFT")
    def test_read_command_file(self, mock_read_command_file):
        self.assertEqual(len(mock_read_command_file("./command_list.txt").split("\n")), 2) # noqa


if __name__ == "__main__":
    unittest.main()
