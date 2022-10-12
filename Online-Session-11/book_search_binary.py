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

    def __lt__(self, other):
        # Define the < operator
        return self.name < other.name

    def __le__(self, other):
        # Define the <= operator
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __eq__(self, other):
        return self.name == other.name


def print_book_list(list_of_books=None):
    if list_of_books is not None:
        for book in list_of_books:
            print(book)


if __name__ == "__main__":
    book_list = []
    book_list.append(Book("Foundation and Empire", 143))
    book_list.append(Book("Hound of the Baskervilles", 192))
    book_list.append(Book("I, Robot", 145))
    book_list.append(Book("Foundation", 143))
    book_list.sort()

    print_book_list(book_list)
    find_me = "I, Robot"

    position = -1
    steps = 0
    begin_position = 0
    end_position = len(book_list)
    while True:
        steps += 1
        middle = (begin_position + end_position) // 2
        current_book = book_list[middle]
        if current_book.name == find_me:
            position = middle
            break

        if current_book.name > find_me:
            end_position = middle
        if current_book.name < find_me:
            begin_position = middle

    if position >= 0:
        print(f"Book \"{find_me}\" was found at position {position}"
              f" in {steps} steps")
    else:
        print(f"Book {find_me} was not found in {steps} steps")
