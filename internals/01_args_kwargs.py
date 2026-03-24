# ============================================================
# *args and **kwargs
# ============================================================
# *args  → packs extra positional arguments into a TUPLE
# **kwargs → packs extra keyword arguments into a DICT
# Rule: order must be -> normal args, *args, **kwargs
# ============================================================


# --- 1. *args: variable positional arguments ---
def print_all(*args):
    print(f"args type: {type(args)}")   # always a tuple
    for item in args:
        print(f"  {item}")

# --- 2. **kwargs: variable keyword arguments ---
def print_info(**kwargs):
    print(f"kwargs type: {type(kwargs)}")  # always a dict
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# --- 3. combining normal args + *args + **kwargs ---
def combined(required, *args, **kwargs):
    print(f"required : {required}")
    print(f"extra args   : {args}")
    print(f"extra kwargs : {kwargs}")

# --- 4. real-world use case: wrapper/decorator pattern ---
def logger(func):
    def wrapper(*args, **kwargs):       # captures anything the original func takes
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)  # passes everything through
        print(f"Done {func.__name__}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

# --- 5. unpacking with * and ** when calling a function ---
def greet(name, age, gender, city):
    print(f"Hi {name}, age {age}, gender {gender} from {city}")


# ============================================================
if __name__ == "__main__":
    print("--- print_all ---")
    print_all(1, 2, 3, "hello", [4, 5])

    print("\n--- print_info ---")
    print_info(name="Alice", age=30, city="New York")

    print("\n--- combined ---")
    combined("must_have", 1, 2, 3, name="Bob", age=25)

    print("\n--- logger wrapper ---")
    result = add(3, 4)
    print(f"Result: {result}")

    print("\n--- unpacking * and ** ---")
    info_list = ["Alice", 30]           # unpack as positional args
    info_dict = {"gender": "female", "city": "New York"}    # unpack as keyword args
    #info_dict = {"gender": "female", "city": "New York", "gender": "male", "gender":"other"}    # unpack as keyword args, note that duplicate keys will be overwritten later ones 
    greet(*info_list, **info_dict)
