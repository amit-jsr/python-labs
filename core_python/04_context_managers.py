# Topic: Context Managers
# - with statement ensures setup and teardown
# - __enter__ and __exit__ define the protocol

# TODO: Write a context manager using a class that logs open/close of a resource
class ManagedResource:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# TODO: Write the same context manager using @contextmanager decorator
from contextlib import contextmanager

@contextmanager
def managed_resource():
    pass

# TODO: Use your context manager to safely open and read a file
