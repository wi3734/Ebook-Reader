##
##The goal of this project is to make an e-book reader that imports a txt file of
##whatever book or anything.
##Import the book (anything with .txt extension)
##indicating page number

class Ebook_runner():
    def __init__(self):
        self.current_book = Book()

    def start(self):
        input("Ebook Reader, PRESS ENTER")
        self.current_book.open_page()
        pass

class Book():
    def __init__(self):
        self.book = open('', encoding='utf-8') #first arg. for a name of the ebook you are trying to import
        self.pages = Page(self.book)
        self.current_page = 0

    def open_page(self):
        print("Book name: {}, Total page: {}".format("book name", self.pages.numbers_of_pages)) #replace the first arg with a name of the book
        self.current_page = int(input("What page to start with? "))
        self.pages.display(self.current_page)

        while True:
            temp1 = input("To the next page: N, To the previous page: P> ")

            if temp1 == 'n':
                self.current_page += 1
                self.turn_next(self.current_page)
                if self.current_page > self.pages.numbers_of_pages:
                    print("End of the page!")

            if temp1 == 'p':
                self.current_page -= 1
                self.turn_previous(self.current_page)
                if self.current_page <= 0:
                    print("This is the first page!")

    def turn_next(self, page):
        self.pages.display(page)

    def turn_previous(self, page):
        self.pages.display(page)

class Page():
    def __init__(self, book):
        self.book = book
        self.pages = {}
        self.numbers_of_pages = 0
        self.each_page = []
        self.numbers_of_lines = 0
        self.line_count = 0
        self.divide_into_pages()

    def divide_into_pages(self): #divide the book into 40 lines per one page
        temp_lines = self.book.readlines()
        per_page = 0 #referring to lines of each page of the book

        self.numbers_of_lines = len(temp_lines) - 1

        while self.line_count != self.numbers_of_lines:
            per_page += 1
            newly_formed = temp_lines[self.line_count].strip()
            self.each_page.append(newly_formed)
            self.line_count += 1

            if per_page == 40: #if per_page reaches 40
                self.numbers_of_pages += 1
                self.pages[self.numbers_of_pages] = self.each_page #add to the pages
                self.each_page = []
                per_page = 0


    def display(self, page_number):
        print(('-'*30), f"Page {page_number}", ('-'*30))

        for x in self.pages[page_number]:
            print(x)

        print(('-'*30), f"Page {page_number}", ('-'*30))


x1 = Ebook_runner()
x1.start()
