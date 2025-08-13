from Reservable import Reservable
from model.LibraryItem import LibraryItem
class Book(LibraryItem,Reservable):
    def __init__(self, title, author, book_id, available=True):
        super().__init__(title, author)
        self.book_id = book_id
        self.available = available
        self.reserved_by = None

    def display_info(self):
        super().display_info()
        status = "Available" if self.available else "Not Available"
        print(f"Book ID: {self.book_id} | Status: {status}")
        
    def check_availability(self):
        return self.available

    def reserve(self,user):
        try:
            if self.reserved_by is None:
                self.reserved_by=user
                print(f"{self.title} reserved by {user}.")
            else:
                raise Exception("This book is already reserved.")
        except Exception as e:
            print(f"Error reserving book: {e}")