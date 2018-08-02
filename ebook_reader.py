import sys
##
##The goal of this project is to make an e-book reader that imports a txt file of
##whatever book or anything.
##Import the book (anything with .txt extension)
##indicating page number

class Ebook_runner():
    def __init__(self):
        input1 = input("Type in the name of the file> ")
        self.current_book = Book(input1)

    def start(self):
        input("Ebook Reader, PRESS ENTER")
        self.current_book.open_page()


class Book():
    def __init__(self, book):
        self.book = open(book, encoding='utf-8')
        self.pages = Page(self.book)
        self.current_page = 0

    def open_page(self):
        print("Book name: {}, Total page: {}".format("Alice In Wonderland", self.pages.numbers_of_pages))
        self.current_page = int(input("What page to start with? "))
        self.pages.display(self.current_page)

        while True:
            temp1 = input("To the next page: N, To the previous page: P > ")

            if temp1 == 'n':
                self.turn_next()

            elif temp1 == 'p':
                self.turn_previous()

    def turn_next(self):
        self.current_page += 1

        if self.current_page > self.pages.numbers_of_pages:
            print("End of the page!")
            quit_it = input("Would you like to quit the program? Y or N")

            if quit_it == 'y' or quit_it == 'Y':
                sys.exit(1)

            elif quit_it == 'N' or quit_it == 'n':
                self.current_page = self.pages.numbers_of_pages #assign an int. value of page - the last page - to the variable
                self.pages.display(self.current_page)
        else:
            self.pages.display(self.current_page)

    def turn_previous(self):
        self.current_page -= 1

        if self.current_page <= 0:
            print("This is the first page!")
            self.current_page = 1
            self.pages.display(self.current_page)

        else:
            self.pages.display(self.current_page)

class Page():
    def __init__(self, book):
        self.book = book
        self.pages = {}
        self.numbers_of_pages = 0
        self.each_page = []
        self.numbers_of_lines = 0
        self.line_count = 0
        self.divide_into_pages()

    def divide_into_pages(self): #divide the book into 40 lines per page
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
        print('\n')
        print(('-'*30), f"Page {page_number}", ('-'*30))
        for x in self.pages[page_number]:
            print(x)
        print(('-'*30), f"Page {page_number}", ('-'*30))


x1 = Ebook_runner()
x1.start()
