from models.position import Position
from models.board import Board


class Robot:
    """
    DIRECTION FOR ROBOT
                                 N,M
                      N
              W               E
     0,0              S


    """
    # clockwise direction / turning right
    # anti-clockwise / turning left
    directions_to_direction_string = {
       "NORTH": "1000",
       "EAST": "0100",
       "SOUTH": "0010",
       "WEST": "0001"
    }

    direction_string_to_direction = {
        "1000": "NORTH",
        "0100": "EAST",
        "0010": "SOUTH",
        "0001": "WEST"
    }

    def __init__(self, position, direction, board):
        """Initialized the robot with position, direction and board."""
        self.position = position
        self.direction = direction
        self.board = board

    def report(self):
        """Return the current position and direction string."""
        return f"X: {self.position.x} Y: {self.position.y} Direction: {self.direction}"

    def turn_left(self):
        """Turn towards the left direction."""
        direction = self.direction
        direction_string = self.directions_to_direction_string[direction]
        direction_string = direction_string[1:4] + direction_string[0]
        self.direction = self.direction_string_to_direction[direction_string]
        return self.direction

    def turn_right(self):
        """Turn towards the right direction."""
        direction = self.direction
        direction_string = self.directions_to_direction_string[direction]
        direction_string = direction_string[3] + direction_string[0:3]
        self.direction = self.direction_string_to_direction[direction_string]
        return self.direction

    def move_forward(self):
        """Move forward and if move not available then don't move in any direction."""
        if self.board.move_available_in_direction(self.position, self.direction):
            if self.direction == "NORTH":
                self.position.y = self.position.y + 1
            if self.direction == "SOUTH":
                self.position.y = self.position.y - 1
            if self.direction == "EAST":
                self.position.x = self.position.x + 1
            if self.direction == "WEST":
                self.position.x = self.position.x - 1

    def change_position(self, position, direction):
        """Change position with new give position and direction."""
        if isinstance(position, Position):
            self.position = position
        if direction in self.directions_to_direction_string:
            self.direction = direction

    def execute_line_command(self, command):
        """Execute PLACE, MOVE, REPORT, LEFT, RIGHT command accordingly."""
        if "PLACE" in command:
            command_args = command.split(" ")
            x = int(command_args[1])
            y = int(command_args[2])
            direction = command_args[3]
            position = Position(x, y)
            self.change_position(position, direction)

        if "MOVE" == command:
            self.move_forward()

        if "REPORT" == command:
            print(self.report())

        if "RIGHT" == command:
            self.turn_right()

        if "LEFT" == command:
            self.turn_left()

    def __str__(self):
        """String representation of the string."""
        return f"position {self.position}, direction: {self.direction}"
