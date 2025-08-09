from LibraryItem import LibraryItem
class Book(LibraryItem):
    def __init__(self, title, author, book_id, availability):
        super().__init__(title, author)
        self.book_id = book_id
        self.availability = availability

    def display_info(self):
        print(f"Book Title: {self.title}, Author: {self.author}, ID: {self.book_id}")
    def check_availability(self):
        if self.availability:
            print(f"The book '{self.title}' is available.")
        else:
            print(f"The book '{self.title}' is not available.")