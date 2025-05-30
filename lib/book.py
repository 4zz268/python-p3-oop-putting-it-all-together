# Book class for OOP lab
class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count
        self._genre = None

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be a positive integer")

    page_count = property(get_page_count, set_page_count)

    def get_genre(self):
        return self._genre

    def set_genre(self, value):
        self._genre = value

    genre = property(get_genre, set_genre)

    def read(self):
        print(f"You start reading '{self.title}' by {self.author}.")
