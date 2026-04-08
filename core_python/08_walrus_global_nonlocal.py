# Topic: Walrus Operator (:=) and global/nonlocal
# - := assigns and returns a value in one expression
# - global: modify a module-level variable inside a function
# - nonlocal: modify an enclosing (non-global) variable

# --- Walrus Operator ---

# TODO: Use walrus operator in a while loop to read input until 'quit'
# while (line := input("Enter: ")) != "quit":
#     print(f"You entered: {line}")

# TODO: Use walrus operator in a list comprehension to avoid double computation
data = [1, -2, 3, -4, 5]
# Get squares of only positive numbers using walrus in a comprehension

# TODO: Use walrus in an if statement to assign and check in one line
import re
text = "Order number: 12345"
# if match := re.search(r'\d+', text): print(match.group())

# --- global and nonlocal ---

# TODO: Demonstrate global keyword
total = 0

def add_to_total(n):
    # modify total using global
    pass

# TODO: Demonstrate nonlocal keyword
def make_accumulator():
    total = 0
    def add(n):
        # modify total using nonlocal
        pass
    return add
