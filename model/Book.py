from LibraryItem import LibraryItem
class Book(LibraryItem):
    def __init__(self, title, author, book_id, available=True):
        super().__init__(title, author)
        self.book_id = book_id
        self.available = available

    def display_info(self):
        super().display_info()
        print(f"Book ID: {self.book_id}")
    def check_availability(self):
        return self.available