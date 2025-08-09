from model.LibraryItem import LibraryItem
class Book(LibraryItem):
    def __init__(self, title, author, book_id, available=True):
        super().__init__(title, author)
        self.book_id = book_id
        self.available = available

    def display_info(self):
        super().display_info()
        status = "Available" if self.available else "Not Available"
        print(f"Book ID: {self.book_id} | Status: {status}")
    def check_availability(self):
        return self.available