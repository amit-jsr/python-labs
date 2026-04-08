# Topic: Dunder (Magic) Methods
# - __len__, __getitem__, __repr__, __str__, __eq__, __lt__

# TODO: Build a custom BookShelf class that:
# - stores a list of book titles
# - supports len(shelf)
# - supports shelf[0] indexing
# - has a readable __repr__ and __str__
# - supports == comparison between two shelves

class BookShelf:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        pass

    def __getitem__(self, index):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass
