# ============================================================
# Context Managers
# - with statement ensures setup and teardown
# - __enter__ and __exit__ define the protocol
# ============================================================

# Notes:
# - A context manager guarantees cleanup code runs, even if an error occurs.
# - `__enter__()` runs at the start of `with` and can return a resource.
# - `__exit__()` runs at the end of `with` for normal exit or exceptions.
# - Returning False from `__exit__` means exceptions are not suppressed.
# - `@contextmanager` is a shorter way to define the same behavior.

# Class-based context manager example
class ManagedResource:
    def __init__(self, name="resource"):
        self.name = name

    def __enter__(self):
        print(f"[class] Opening {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"[class] Error in {self.name}: {exc_val}")
        print(f"[class] Closing {self.name}")
        return False

# Decorator-based context manager example
from contextlib import contextmanager

@contextmanager
def managed_resource(name="resource"):
    print(f"[decorator] Opening {name}")
    try:
        yield name
    except Exception as error:
        print(f"[decorator] Error in {name}: {error}")
        raise
    finally:
        print(f"[decorator] Closing {name}")

# Demo usage
if __name__ == "__main__":
    print("--- class-based context manager ---")
    with ManagedResource("db-connection") as resource:
        print(f"Using {resource.name}")

    print("\n--- decorator-based context manager ---")
    with managed_resource("api-client") as resource_name:
        print(f"Using {resource_name}")

    print("\n--- safe file read with with-statement ---")
    demo_path = "/tmp/context_demo.txt"
    with open(demo_path, "w", encoding="utf-8") as file:
        file.write("line 1\nline 2\n")

    with open(demo_path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
