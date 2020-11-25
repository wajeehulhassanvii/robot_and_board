class Board:
    MIN_N = 0
    MIN_M = 0

    def __init__(self, n=5, m=5):
        """Initialize Board object."""
        if n < self.MIN_N:
            self.MAX_N = 1
        else:
            self.MAX_N = n
        if m < self.MIN_M:
            self.MAX_M = 1
        else:
            self.MAX_M = m

    # def move_available(self, position):
    #     """ will be called before everytime "MOVE" command is received,
    #     if move available then return True"""
    #     return True if self.MIN_N < position.x < self.MAX_N and self.MIN_M < position.y < self.MAX_M else False

    def move_available_in_direction(self, position, direction):
        """ will be called before everytime "MOVE" command is received,
        if move available then return True"""
        available = False
        if direction == "NORTH":
            available = position.y + 1 < self.MAX_M # 4 + 1 < 5
        if direction == "SOUTH":
            available = position.y - 1 >= self.MIN_M # 0 - 1 >= 0 FALSE,,,,, 1 - 1 >= 0  TRUE
        if direction == "EAST":
            available = position.x + 1 < self.MAX_N # 4 + 1 < 5
        if direction == "WEST":
            available = position.x - 1 >= self.MIN_N # 0 - 1 >= 0 FALSE,,,,, 1 - 1 >= 0  TRUE
        return available
