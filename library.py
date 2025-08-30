books = []   # each book will be stored as [title, author]

# 1. Add a new book
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    books.append([title, author])   # store as list [title, author]
    print("Book added!\n")

# 2. Display all books
def display_books():
    if not books:
        print("No books in inventory.\n")
    else:
        print("\n=== Book Inventory ===")
        for i, book in enumerate(books, 1):   # book is [title, author]
            print(i, ":", book[0], "by", book[1])
        print()

# 3. Search for a book
def search_book():
    title = input("Enter Book Title to Search: ")
    for book in books:
        if book[0] == title:   # check only title
            print("Book Found:", book[0], "by", book[1], "\n")
            found = True
            break
    if not found:
        print("Book not found.\n")

# 4. Remove a book
def remove_book():
    title = input("Enter Book Title to Remove: ")
    author = input("Enter Author Name to Remove: ")
    found = False
    for book in books:
        if book[0] == title and book[1] == author:   # match both
            books.remove(book)
            print("Book removed!\n")
            found = True
            break
    if not found:
        print("Book not found.\n")

# Main menu
while True:
    print("==== Book Store Menu ====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")
