class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.length = 0
        self.pages = {1: []}


def is_page_full(current_book):
    length = len(current_book.pages)
    if len(current_book.pages[length]) < 5:
        return False
    return True


def create_new_page(current_book):
    length = len(current_book.pages)
    current_book.pages[length + 1] = []


def write_to_page(current_book, response):
    length = len(current_book.pages)
    current_book.pages[length].append(response)


def main():
    my_book = Book("Journal", "Richie")
    repeat = True
    while repeat:
        response = str(input("Enter the contents of the page: "))
        if is_page_full(my_book):
            create_new_page(my_book)
        write_to_page(my_book, response)

        print(my_book.pages)

main()
