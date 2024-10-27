# if, if elif, if else, if elif else
# Arithmetic Operators
# Assignment Operators

# Comparison Operators > < == >= <= !=
# Logical Operators and or not 
# Membership Operators in not in






# Initialize an empty list to store the books
library = []

def add_book(title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "is_checked_out": False
    }
    library.append(book)
    print(f'Added "{title}" by {author}.')

def display_books():
    if not library:
        print("No books in the library.")
        return
    for book in library:
        status = "Checked Out" if book["is_checked_out"] else "Available"
        print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {status}')

def check_out_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            if not book["is_checked_out"]:
                book["is_checked_out"] = True
                print(f'Checked out "{title}".')
            else:
                print(f'"{title}" is already checked out.')
            return
    print(f'Book titled "{title}" not found.')

def return_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            if book["is_checked_out"]:
                book["is_checked_out"] = False
                print(f'Returned "{title}".')
            else:
                print(f'"{title}" was not checked out.')
            return
    print(f'Book titled "{title}" not found.')

# Main loop for user interaction
while True:
    print("\n1. Add a book")
    print("2. Display all books")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter publication year: "))
        add_book(title, author, year)
    elif choice == "2":
        display_books()
    elif choice == "3":
        title = input("Enter book title to check out: ")
        check_out_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ")
        return_book(title)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")


