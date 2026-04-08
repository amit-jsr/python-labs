# Topic: Closures & Scope (LEGB Rule)
# - LEGB: Local -> Enclosing -> Global -> Built-in
# - Closures: inner function remembers enclosing scope

# TODO: Demonstrate LEGB with a variable named 'x' at each scope level
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # which x?
    inner()

# TODO: Write a closure that returns a multiplier function
def make_multiplier(factor):
    pass

# double = make_multiplier(2)
# double(5) should return 10

# TODO: Use 'global' keyword to modify a global variable inside a function
counter = 0

def increment():
    pass

# TODO: Use 'nonlocal' keyword to modify an enclosing variable
def make_counter():
    count = 0
    def increment():
        pass
    return increment
