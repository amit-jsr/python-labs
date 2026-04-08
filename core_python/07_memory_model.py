# Topic: Memory Model, GIL & __slots__
# - Python uses reference counting for memory management
# - Mutable vs immutable types — aliasing bugs
# - GIL: only one thread executes Python bytecode at a time

# TODO: Demonstrate aliasing bug with mutable types
a = [1, 2, 3]
b = a           # b is NOT a copy — same object!
# What happens when you do b.append(4)?

# TODO: Use id() to confirm two variables point to the same object
# TODO: Fix the aliasing bug using copy

import copy

# TODO: Demonstrate the nested list bug with shallow copy vs deep copy
nested = [[1, 2], [3, 4]]
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)
# Modify nested[0][0] — which copies are affected?

# TODO: Write a class with __slots__ to restrict attributes and save memory
class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
