class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        author.add_book(book)
        Book.all_books += 1
        return book

    def group_by_author(self, author):
        books = [book for book in self.books if book.author == author]
        return books

    def group_by_year(self, year: int):
        books = [book for book in self.books if book.year == year]
        return books

    def __str__(self):
        return f"Library '{self.name}': {len(self.books)} books, {len(self.authors)} authors"

    def __repr__(self):
        return f"Library(name='{self.name}')"


class Book:
    all_books = 0

    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.year}, {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', year='{self.year}', author='{self.author}')"


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"{self.name}, {self.country}, {self.birthday}"

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"


king = Author("Steven King", "USA", "21 september 1947")

my_library = Library("My Library")

my_library.new_book("It", 1986, king)
my_library.new_book("Doctor Sleep", 2013, king)
my_library.new_book("Duma Key", 2008, king)

steven_king = my_library.group_by_author(king)
for author in steven_king:
    print(author)

steven_king_year = my_library.group_by_year(2008)
for year in steven_king_year:
    print(f"\n- {year}")

total_books = Book.all_books
print(f"\nTotal books: {total_books}")

print(my_library)
