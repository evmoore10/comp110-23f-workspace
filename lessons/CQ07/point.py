"""Using Point!"""


from __future__ import annotations


class Point:
    """Class for point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Creating points!"""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Multiplying by a factor and updating the points."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Creat new point with updated points."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        "Printing out points."
        return (f"x: {self.x}; y: {self.y}")
    
    def __mul__(self, factor: float | int) -> Point:
        """Multiplying points."""
        x_val = self.x * factor
        y_val = self.y * factor
        return(x_val, y_val)
    
    def __add__(self, factor: float | int) -> Point:
        """Adding number to points."""
        x_val = self.x + factor
        y_val = self.y + factor
        return (x_val, y_val)