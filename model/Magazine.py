from LibraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, magazine_id, availability):
        super().__init__(title, author)
        self.magazine_id = magazine_id
        self.availability = availability

    def display_info(self):
        print(f"Magazine Title: {self.title}, Author: {self.author}, ID: {self.magazine_id}")

    def check_availability(self):
        if self.availability:
            print(f"The magazine '{self.title}' is available.")
        else:
            print(f"The magazine '{self.title}' is not available.")
