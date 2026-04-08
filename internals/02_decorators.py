# ============================================================
# Decorators
# ============================================================
# A decorator wraps a function to extend or modify its behavior
# without changing the function's source code.
#
# Pattern:
#   def decorator(func):
#       def wrapper(*args, **kwargs):
#           # do something before
#           result = func(*args, **kwargs)
#           # do something after
#           return result
#       return wrapper
#
# Key built-ins: @property, @<prop>.setter, @staticmethod
# Notes:
#   Decorators can be stacked (multiple @decorators on the same function) and are applied from the bottom up.
#   Decorators cannot be comma-separated on one line.
# ============================================================

import time
import json
import functools


# --- 1. Basic decorator: prints "before" and "after" a call ---
def my_decorator(func):
    @functools.wraps(func)          # preserves original func name & docstring
    def wrapper(*args, **kwargs):
        print(f"[before] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[after]  {func.__name__} finished")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")


# --- 2. Timer decorator: measures execution time ---
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.1)     # simulate some work
    return a + b

# --- 3. JSON field extractor decorator: returns only the State value ---
def state(func):
    """Logs a call, then extracts the 'State' field from returned JSON text."""
    def wrapper(*args, **kwargs):
        print(f"[test] Running {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        result = json.loads(result).get('State', 'Unknown')
        print(f"[test] {func.__name__} finished with result={result}")
        return result
    return wrapper

@state
def get_address(text):
    """Returns title-cased text so the state decorator can parse it as JSON."""
    return text.title()


# --- 4. Math-transform decorators for chaining demos ---
def decorator1(func):
    """Adds 1 to the wrapped function's numeric result."""
    def wrapper(x):
        result = func(x)
        return result + 1
    return wrapper

def decorator2(func):
    """Squares the wrapped function's numeric result."""
    def wrapper(x):
        result = func(x)
        return result ** 2
    return wrapper

@decorator2
@decorator1
def foo(x):
    return x



# --- 3. Class with @property, @<prop>.setter, @staticmethod ---
class Circle:
    def __init__(self, radius):
        self._radius = radius   # store in a "private" attribute

    @property
    def radius(self):
        """Getter – returns the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter – validates that radius is positive before storing."""
        if value <= 0:
            raise ValueError(f"radius must be > 0, got {value}")
        self._radius = value

    @property
    def area(self):
        """Derived property – computed on the fly, no setter needed."""
        return 3.14159 * self._radius ** 2

    @staticmethod
    def cm_to_m(cm):
        """Unit conversion helper – doesn't need self or the class."""
        return cm / 100

# ============================================================
if __name__ == "__main__":
    print("--- my_decorator ---")
    greet("Alice")

    print("\n--- timer ---")
    result = slow_add(3, 4)
    print(f"slow_add result: {result}")

    print("\n--- Circle: @property & @staticmethod ---")
    c = Circle(5)
    print(f"radius : {c.radius}")
    print(f"area   : {c.area:.2f}")

    c.radius = 10               # uses the setter
    print(f"updated radius: {c.radius}")

    try:
        c.radius = -3           # triggers ValueError
    except ValueError as e:
        print(f"caught error → {e}")

    print(f"50 cm in metres: {Circle.cm_to_m(50)}")

    print(foo(3))  # Output: 8, because ((3 + 1) * 2)
