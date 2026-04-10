# ============================================================
# Dunder (Magic) Methods
# ============================================================
# Dunder methods let you customize how built-in operations work.
#
# Categories:
# - String: __repr__, __str__, __format__
# - Container: __len__, __getitem__, __setitem__, __contains__, __iter__, __next__
# - Comparison: __eq__, __lt__, __le__, __gt__, __ge__
# - Arithmetic: __add__, __sub__, __mul__, __truediv__, __mod__, __pow__
# - Other: __call__, __enter__, __exit__, __hash__, __bool__

# Notes:
# - __repr__ for debugging, __str__ for display
# - Return NotImplemented for incompatible types (not False)
# - __getitem__ enables indexing/slicing and iteration
# - __lt__ enables sorted() and < operator
# - Names are fixed — you can't rename them

class Point:
    """2D point with comparison and arithmetic."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Compare by distance from origin — enables sorted()."""
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)


# ============================================================
if __name__ == "__main__":

    print("\n--- Point ---")
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    
    print(f"p1: {p1}, p2: {p2}")
    print(f"p1 == Point(3, 4): {p1 == Point(3, 4)}")
    print(f"p1 < p2: {p1 < p2}")  # False (farther from origin)
    print(f"p1 + p2: {p1 + p2}")
    print(f"sorted: {sorted([Point(5,5), Point(1,1), Point(3,4)])}")
