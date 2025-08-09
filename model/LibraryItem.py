from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title :{self.title} | Author: {self.author} | ")
    @abstractmethod
    def check_availability(self):
        pass