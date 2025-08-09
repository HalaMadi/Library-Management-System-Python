from LibraryItem import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, author, dvd_id, availability):
        super().__init__(title, author)
        self.dvd_id = dvd_id
        self.availability = availability

    def display_info(self):
        print(f"DVD Title: {self.title}, Author: {self.author}, ID: {self.dvd_id}")

    def check_availability(self):
        if self.availability:
            print(f"The DVD '{self.title}' is available.")
        else:
            print(f"The DVD '{self.title}' is not available.")
