class Position:
    def __init__(self, x=1, y=1):
        """Initialize Position object."""
        if x < 0:
            self.x = 0
        else:
            self.x = x

        if y < 0:
            self.y = 0
        else:
            self.y = y

    def __eq__(self, other_position):
        """Check whether other Position object is equal or not."""
        return self.x == other_position.x and self.y == other_position.y

    def __str__(self):
        """String representation of the Position object."""
        return f"x: {self.x}, y: {self.y}"
