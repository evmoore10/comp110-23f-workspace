"""Using Point!"""


from __future__ import annotations


class Point:
    """Class for point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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