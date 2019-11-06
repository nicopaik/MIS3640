class Point:
    """
    represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        """
        return a Point object in a human-readable format
        """
        return f'({self.x}, {self.y})'

    def __add__(self, other_point):
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        new_point = Point(new_x, new_y)
        return new_point

    def __sub__ (self, other_point):
        new_x = self.x - other_point.x
        new_y = self.y - other_point.y
        new_point = Point(new_x, new_y)
        return new_point
        
    victoria = Point(3,4)
    print(victoria)

    myat = Point(5, 5)

    print(victoria + myat)
    print(myat - victoria)

