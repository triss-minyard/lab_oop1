class Book:
    def init(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        print("Название: ", self.title)
        print("Автор: ", self.author)
        print("Год издания: ", self.year )


book1 = Book("Война и мир", "Лев Толстой", 1869)
book1.get_info()


book2 = Book("1984", "Джордж Оруэлл", 1949)
book2.get_info()
