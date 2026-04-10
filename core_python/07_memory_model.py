# ============================================================
# Memory Model, GIL & __slots__
# ============================================================
# Python memory:
# - Reference counting tracks object usage
# - id() returns memory address
# - Immutable: int, str, tuple (can't modify)
# - Mutable: list, dict, set (can modify in place)
#
# GIL (Global Interpreter Lock):
# - Only one thread executes Python at a time
# - Use multiprocessing for CPU tasks, threading for I/O
#
# __slots__:
# - Restricts attributes, saves memory (~40%)
# - No __dict__ per instance

# Notes:
# - a = b creates reference, not copy
# - copy.copy() for shallow, copy.deepcopy() for nested
# - Shallow: copies top level, nested objects still shared
# - __slots__ prevents dynamic attributes

# ============================================================
# Example 1: Aliasing bug with mutable types
# ============================================================

def demo_aliasing_bug():
    """Show how aliasing causes bugs."""
    a = [1, 2, 3]
    b = a  # b is NOT a copy — same object!
    
    print(f"a: {a}, b: {b}")
    print(f"id(a): {id(a)}, id(b): {id(b)}")
    print(f"a is b: {a is b}")  # True — same object!
    
    b.append(4)  # Modify through b
    print(f"After b.append(4):")
    print(f"a: {a}, b: {b}")  # Both changed!
    
    # Fix: use copy
    c = a.copy()  # or list(a) or a[:]
    c.append(5)
    print(f"\nAfter c = a.copy(); c.append(5):")
    print(f"a: {a}, c: {c}")  # Only c changed


# ============================================================
# Example 2: Shallow vs Deep copy
# ============================================================

import copy

def demo_shallow_vs_deep():
    """Nested structure copy problem."""
    nested = [[1, 2], [3, 4]]
    
    # Shallow copy: copies outer list, inner lists are references
    shallow = copy.copy(nested)
    # Deep copy: recursively copies everything
    deep = copy.deepcopy(nested)
    
    print(f"Original: {nested}")
    print(f"Shallow:  {shallow}")
    print(f"Deep:     {deep}")
    
    # Modify nested structure
    nested[0][0] = 999
    
    print(f"\nAfter nested[0][0] = 999:")
    print(f"Original: {nested}")      # Changed
    print(f"Shallow:  {shallow}")     #  Also changed! (inner list is shared)
    print(f"Deep:     {deep}")        #  Not changed (fully independent)


# ============================================================
# Example 3: __slots__ for memory optimization
# ============================================================

class WithoutSlots:
    """Regular class — each instance has __dict__."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    """Optimized class — fixed attributes, no __dict__."""
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


def demo_slots():
    """Memory savings with __slots__."""
    regular = WithoutSlots(1, 2)
    slotted = WithSlots(1, 2)
    
    print(f"WithoutSlots instance size: {regular.__sizeof__()} bytes")
    print(f"WithSlots instance size: {slotted.__sizeof__()} bytes")
    
    # Regular class allows dynamic attributes
    regular.z = 3
    print(f"regular.z = {regular.z}")
    
    # Slotted class does NOT
    try:
        slotted.z = 3  #  AttributeError
    except AttributeError as e:
        print(f"slotted.z = 3 failed: {e}")
    
    # Check __dict__
    print(f"\nregular.__dict__: {regular.__dict__}")
    try:
        print(f"slotted.__dict__: {slotted.__dict__}")
    except AttributeError:
        print("slotted has no __dict__ (saves memory)")


# ============================================================
# Example 4: GIL demonstration concept
# ============================================================

def demo_gil_concept():
    """Explain GIL without heavy threading code."""
    print("\n--- GIL (Global Interpreter Lock) ---")
    print("- Only ONE thread executes Python bytecode at a time")
    print("- CPU-bound tasks: threads don't help (use multiprocessing)")
    print("- I/O-bound tasks: threads work well (waiting for network/disk)")
    print("- Example: 4-core CPU + 4 threads doing math = NO speedup")
    print("- Example: 4 threads downloading files = ~4x speedup")


# ============================================================
if __name__ == "__main__":
    print("--- 1. Aliasing Bug ---")
    demo_aliasing_bug()
    
    print("\n--- 2. Shallow vs Deep Copy ---")
    demo_shallow_vs_deep()
    
    print("\n--- 3. __slots__ Memory Optimization ---")
    demo_slots()
    
    demo_gil_concept()
