# Function to read books from file
def read_books():
    books = []
    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")
        books.append([data[0], data[1], int(data[2])])

    file.close()
    return books


# Function to update file
def update_file(books):
    file = open("books.txt", "w")

    for book in books:
        file.write(f"{book[0]},{book[1]},{book[2]}\n")

    file.close()


# Display all books
def display_books():
    books = read_books()

    print("\nBook ID\tBook Name\t\tQuantity")
    print("-" * 40)

    for book in books:
        print(book[0], "\t", book[1], "\t", book[2])


# Search book by ID
def search_book(book_id):
    books = read_books()

    for book in books:
        if book[0] == book_id:
            print("\nBook Found")
            print("ID:", book[0])
            print("Name:", book[1])
            print("Quantity:", book[2])
            return

    print("Book not found.")


# Issue book
def issue_book(book_id):
    books = read_books()

    for book in books:
        if book[0] == book_id:
            if book[2] > 0:
                book[2] -= 1
                update_file(books)
                print("Book issued successfully.")
            else:
                print("Book unavailable.")
            return

    print("Book not found.")


# Return book
def return_book(book_id):
    books = read_books()

    for book in books:
        if book[0] == book_id:
            book[2] += 1
            update_file(books)
            print("Book returned successfully.")
            return

    print("Book not found.")


# Display unavailable books
def unavailable_books():
    books = read_books()

    print("\nUnavailable Books:")
    for book in books:
        if book[2] == 0:
            print(book[0], "-", book[1])


# Display books requiring restocking
def restocking_books():
    books = read_books()

    print("\nBooks Requiring Restocking:")
    for book in books:
        if book[2] < 2:
            print(book[0], "-", book[1], "-", book[2], "copies")


# Main Menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        book_id = input("Enter Book ID: ")
        search_book(book_id)

    elif choice == 3:
        book_id = input("Enter Book ID to issue: ")
        issue_book(book_id)

    elif choice == 4:
        book_id = input("Enter Book ID to return: ")
        return_book(book_id)

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")