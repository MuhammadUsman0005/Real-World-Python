books = {
    "Python Basics" : 7,
    "Information Technology" : 12,
    "Rich Dad, Poor Dad" : 4,
    "Atomic Habits" : 9,
    "C++ Fundamentals" : 0
}

print("1. Show all books")
print("2. Issue a book")
print("3. Return a book")

choice = int(input("Enter choice: "))

if choice == 1:
    print("\nAvailable Books:")
    for name in sorted(books.keys()):
        print(f"{name} : {books[name]}")
elif choice == 2:
    book_name = input("Enter book name to issue: ").strip()
    if book_name not in books:
        print("Book not found!")
        exit()
    
    if books[book_name] == 0:
        print("Sorry, no copies available.")
    else:
        confirmation = input("Are you sure you want to issue this book? ").lower()
        if confirmation == 'yes':
            books[book_name] -= 1
            print("Book issued successfully.")
            print("Remaining copies: ", books[book_name])
        else:
            print("Operation cancelled.")
            exit()

elif choice == 3:
    book_name = input("Enter book name to return: ").strip()
    if book_name not in books:
        print("Book not found!")
        exit()
    books[book_name] += 1
    print("Book returned successfully.")
else:
    print("Invalid choice!")