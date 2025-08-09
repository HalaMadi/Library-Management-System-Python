from LibraryItem import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, author, dvd_id, available=True):
        super().__init__(title, author)
        self.dvd_id = dvd_id
        self.available = available

    def display_info(self):
        super().display_info()
        print(f"DVD ID: {self.dvd_id}")

    def check_availability(self):
        return self.available