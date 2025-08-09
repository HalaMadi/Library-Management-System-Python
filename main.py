from model.Book import Book
from model.Magazine import Magazine
from model.DVD import DVD
class Main:
    def run(self):
        book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1, available=True)
        book1.display_info()
       
if __name__ == "__main__":
    main = Main()
    main.run()
