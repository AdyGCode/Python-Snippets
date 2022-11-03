class Book:
    def __init__(self, name=None, height=None):
        if name is None:
            name = ""
        if height is None:
            height = -1
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height}mm)"


def print_book_list(list_of_books=None):
    if list_of_books is not None:
        for book in list_of_books:
            print(book)

if __name__ == "__main__":
    book_list = []
    book_list.append(Book("Foundation", 143))
    book_list.append(Book("Foundation and Empire", 143))
    book_list.append(Book("Hound of the Baskervilles", 192))
    book_list.append(Book("I, Robot", 145))

    print_book_list(book_list)
    find_me = "I, Robot"

    position = -1
    steps = 0
    for book in book_list:
        steps += 1
        if book.name == find_me:
            position = steps - 1
            break
        if book.name > find_me:
            break

    if position >= 0:
        print(f"Book \"{find_me}\" was found at position {position}"
              f" in {steps} steps")
    else:
        print(f"Book {find_me} was not found in {steps} steps")
