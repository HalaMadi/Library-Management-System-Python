from Reservable import Reservable 
from model.LibraryItem import LibraryItem

class DVD(LibraryItem, Reservable):
    def __init__(self, title, author, dvd_id, available=True):
        super().__init__(title, author)
        self.dvd_id = dvd_id
        self.available = available
        self.reserved_by = None

    def display_info(self):
        super().display_info()
        status="Available" if self.available else "Not Available"
        print(f"DVD ID: {self.dvd_id} | Status: {status}")

    def check_availability(self):
        return self.available
    
    def reserve(self,user):
        try:
            if self.reserved_by is None:
                self.reserved_by=user
                print(f"{self.title} reserved by {user}.")
            else:
                raise Exception("This DVD is already reserved.")
        except Exception as e:
            print(f"Error reserving DVD: {e}")