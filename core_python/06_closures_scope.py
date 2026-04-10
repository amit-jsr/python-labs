# ============================================================
# Closures & Scope (LEGB Rule)
# ============================================================
# LEGB: Python's scope resolution order
# - Local: inside current function
# - Enclosing: inside enclosing function (for nested functions)
# - Global: module level
# - Built-in: Python's built-in names (len, str, etc.)
#
# Closures: inner function "remembers" variables from enclosing scope
# - Use 'global' to modify global variables inside functions
# - Use 'nonlocal' to modify enclosing variables in nested functions

# Notes:
# - Reading a variable: Python searches L -> E -> G -> B
# - Assigning creates a NEW local variable (unless you use global/nonlocal)
# - Closures are useful for factory functions, decorators, callbacks
# - nonlocal only works with enclosing scope, not global scope

# ============================================================
# Example 1: LEGB demonstration
# ============================================================

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(f"  Local x: {x}")  # Prints "local"
    inner()
    print(f"Enclosing x: {x}")  # Prints "enclosing"

# ============================================================
# Example 2: Closure with factory function
# ============================================================

def make_multiplier(factor):
    """Returns a function that multiplies by factor."""
    def multiplier(n):
        return n * factor  # 'factor' is from enclosing scope
    return multiplier

# ============================================================
# Example 3: global keyword
# ============================================================

counter = 0

def increment():
    """Modify global counter variable."""
    global counter
    counter += 1
    return counter

# ============================================================
# Example 4: nonlocal keyword
# ============================================================

def make_counter():
    """Returns a counter function with internal state."""
    count = 0
    def increment():
        nonlocal count  # Modify enclosing 'count', not create local one
        count += 1
        return count
    return increment


# ============================================================
if __name__ == "__main__":
    print("--- 1. LEGB Rule ---")
    print(f"Global x: {x}")
    outer()
    
    print("\n--- 2. Closure: make_multiplier ---")
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(f"double(5): {double(5)}")
    print(f"triple(5): {triple(5)}")
    print(f"double(10): {double(10)}")
    
    print("\n--- 3. global keyword ---")
    print(f"Initial counter: {counter}")
    print(f"After increment(): {increment()}")
    print(f"After increment(): {increment()}")
    print(f"Global counter: {counter}")
    
    print("\n--- 4. nonlocal keyword ---")
    counter1 = make_counter()
    counter2 = make_counter()
    print(f"counter1(): {counter1()}")
    print(f"counter1(): {counter1()}")
    print(f"counter2(): {counter2()}")
    print(f"counter1(): {counter1()}")

