from LibraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, magazine_id, available=True):
        super().__init__(title, author)
        self.magazine_id = magazine_id
        self.available = available

    def display_info(self):
        super().display_info()
        print(f"Magazine ID: {self.magazine_id}")

    def check_availability(self):
        return self.available
