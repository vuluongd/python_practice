"""
Tạo class Library quản lý danh sách 
Book: Book: thuộc tính title, author, year.
Library: phương thức add_book(), remove_book(title), list_books()

"""
class Book:
    def __init__(self, title, author, year):
        self.title = title 
        self.author = author
        self.year = year
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        before = len(self.books)
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        after = len(self.books)

        if before == after:
            print(f"Sách '{title}' không tìm thấy")
        else:
            print(f"Đã xóa: {title} ")

    def list_books(self):
        if not self.books:
            print("Library is empty")

        else:
            print("Books in library:")
            for book in self.books:
                print(" -", book)

library = Library()

library.add_book(Book("The great Gatsby", "F.Scott Fitzgerald", 1925))
library.add_book(Book("Dumb Luck", "Vu Trong Phuc", 1936))
library.add_book(Book("The hundred year-old man climb out the window and disappeared","Jonas Jonasson", "2009"))
library.add_book(Book("1984", "Geogre Orwell", 1949))


library.list_books()


library.remove_book("1984")

print("Sau khi xóa")
library.list_books()