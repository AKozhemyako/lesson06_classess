class Point:
    def __init__(self, point: Point = None):
        if point is None:
            self.x = x
            self.y = y
        else:
            self.x = point.x
            self.y = point.y

    def __str__(self) -> str:
        return f"Point({self.x},{self.y})"