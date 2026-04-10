# ============================================================
#Generators & Iterators
# ============================================================
# - yield: pauses function execution and yields one value at a time.
# - __iter__ and __next__: methods used by Python's iterator protocol.

# Notes:
# - A generator uses `yield` to produce values one-by-one (lazy evaluation), so it is memory efficient for large data.
# - `yield` returns a value and pauses function state; the next iteration resumes from the same place.
# - `square_generator(n)` is useful because it gives each square on demand instead of building the whole list first.

# - An iterator is any object that follows the iterator protocol:
#     - `__iter__()` returns an iterator object
#     - `__next__()` returns next value and raises `StopIteration` when done
# - `Countdown` is a custom iterator example, and `for` loop automatically calls `iter()`/`next()` until `StopIteration` occurs.

# - Use cases: That sequence can drive logic: timing, retries, pagination, IDs, windows, batching,
#   progress, or stopping conditions. The iterator itself is the source of values; the usefulness
#   comes from how you consume them.


def square_generator(n):
    """Yield squares from 1 to n (inclusive)."""
    for num in range(1, n + 1):
        yield num ** 2


def read_large_file(filepath):
    """Yield one line at a time from a file (memory efficient)."""
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


class Countdown:
    """Custom iterator that counts down from start to 0."""

    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Reset so the same object can be iterated again.
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value


if __name__ == "__main__":
    print("--- square_generator(5) ---")
    print(list(square_generator(5)))

    print("\n--- read_large_file demo ---")
    demo_file = "/tmp/generator_demo.txt"
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write("first line\nsecond line\nthird line\n")

    for line in read_large_file(demo_file):
        print(line)

    print("\n--- Countdown(3) ---")
    for value in Countdown(3):
        print(value)
