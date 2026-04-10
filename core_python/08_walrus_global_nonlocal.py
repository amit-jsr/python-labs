# ============================================================
# Walrus Operator (:=)
# ============================================================
# Assigns and returns value in one expression (Python 3.8+).
#
# Common uses:
# - if/while statements (assign + check)
# - List comprehensions (avoid double computation)
# - Capture intermediate values
#
# Syntax: (variable := expression)

# Notes:
# - Reduces code duplication
# - Don't overuse — readability matters
# - For global/nonlocal: see 06_closures_scope.py

import re

# ============================================================
# Example 1: Walrus in while loop (file reading pattern)
# ============================================================

def demo_while_loop():
    """Walrus in while loop pattern."""
    print("--- Walrus in while loop ---")
    print("Traditional way (calls input twice):")
    print("# line = input('Enter: ')")
    print("# while line != 'quit':")
    print("#     process(line)")
    print("#     line = input('Enter: ')  # Duplicate call!\n")
    
    print("With walrus operator (single call):")
    print("# while (line := input('Enter: ')) != 'quit':")
    print("#     process(line)\n")
    
    # Real example with list instead of input
    data = ["hello", "world", "quit", "ignored"]
    i = 0
    results = []
    while (item := data[i] if i < len(data) else "quit") != "quit":
        results.append(item.upper())
        i += 1
    print(f"Processed: {results}")


# ============================================================
# Example 2: Walrus in list comprehension
# ============================================================

def demo_comprehension():
    """Avoid double computation."""
    print("\n--- Walrus in comprehension ---")
    data = [1, -2, 3, -4, 5, -6, 7]
    
    # Without walrus: compute positive check twice
    print("Without walrus (inefficient):")
    print("squares = [x**2 for x in data if x > 0]")
    squares_old = [x**2 for x in data if x > 0]
    print(f"Result: {squares_old}")
    
    # With walrus: filter and transform in one pass
    print("\nWith walrus (compute once, use twice):")
    print("squares = [(val := x) ** 2 for x in data if (val := x) > 0]")
    # Better example: expensive computation
    def expensive(x):
        return x * 2
    
    print("\nMore realistic — expensive computation:")
    print("results = [val for x in data if (val := expensive(x)) > 5]")
    results = [val for x in data if (val := expensive(x)) > 5]
    print(f"Result: {results}")


# ============================================================
# Example 3: Walrus in if statement (regex pattern)
# ============================================================

def demo_if_statement():
    """Assign and check in one line."""
    print("\n--- Walrus in if statement ---")
    text = "Order number: 12345, Date: 2024-01-15"
    
    # Traditional way
    print("Traditional way:")
    print("match = re.search(r'\\d+', text)")
    print("if match:")
    print("    print(match.group())\n")
    
    # With walrus
    print("With walrus operator:")
    print("if match := re.search(r'\\d+', text):")
    print("    print(match.group())\n")
    
    if match := re.search(r'\d+', text):
        print(f"Found number: {match.group()}")
    
    # Multiple patterns
    print("\nChecking multiple patterns:")
    if order_match := re.search(r'Order number: (\d+)', text):
        print(f"Order: {order_match.group(1)}")
    if date_match := re.search(r'Date: ([\d-]+)', text):
        print(f"Date: {date_match.group(1)}")


# ============================================================
# Example 4: Walrus in complex conditions
# ============================================================

def demo_complex_conditions():
    """Walrus in complex checks."""
    print("\n--- Walrus in complex conditions ---")
    
    data = [10, 25, 30, 5, 15]
    threshold = 20
    
    # Filter and process values above threshold
    print(f"Data: {data}, Threshold: {threshold}")
    print("\nif (filtered := [x for x in data if x > threshold]):")
    print("    print(f'Found {len(filtered)} items: {filtered}')\n")
    
    if (filtered := [x for x in data if x > threshold]):
        print(f"Found {len(filtered)} items: {filtered}")
        print(f"Average: {sum(filtered) / len(filtered):.1f}")
    else:
        print("No items above threshold")


# ============================================================
# Quick reference: global and nonlocal
# ============================================================
# For detailed examples, see: 06_closures_scope.py
#
# global — modify module-level variable:
#   counter = 0
#   def increment():
#       global counter
#       counter += 1
#
# nonlocal — modify enclosing function variable:
#   def make_counter():
#       count = 0
#       def increment():
#           nonlocal count
#           count += 1
#           return count
#       return increment
# ============================================================


# ============================================================
if __name__ == "__main__":
    demo_while_loop()
    demo_comprehension()
    demo_if_statement()
    demo_complex_conditions()
    
    print("\n" + "="*60)
    print("Key Takeaway: Walrus operator (:=)")
    print("- Assigns AND returns value in one expression")
    print("- Reduces code duplication")
    print("- Common in: while loops, if statements, comprehensions")
    print("- Don't overuse — readability matters!")
    print("="*60)
