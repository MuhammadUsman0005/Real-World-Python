books = {
    "Python Basics" : 12,
    "Pride and Prejudice" : 6,
    "The Great Gatsby" : 13,
    "The God of the Woods" : 5,
    "The Lord of the Rings" : 3,
    "Harry Potter Series" : 9,
    "Project Hail Mary" : 10,
    "A Little Life" : 17,
    "Crime and Punishment" : 4,
    "War and Peace" : 13,
    "Rich Dad, Poor Dad" : 22
}

students = {
    "Std_name" : ["Books list"]
}

print("1. Show all available books")
print("2. Issue a book")
print("3. Return a book")
print("4. Show issued books")

choice = int(input("Enter your choice: "))
 
# - - - - - - - - - - - Show all books - - - - - - - - 

if choice == 1:
    print("\nAvailable Books:")
    for name, copies in sorted(books.items()):
        print(f"{name} : {copies}")
# - - - - - - - - - - - Issue a book - - - - - -
elif choice == 2:
    student_name = input("Enter your name: ").strip()
    if student_name == "":
        print("Invalid name!")
        exit()
    book_name = input("Enter book name to issue: ").strip()
    if book_name not in books:
        print("Book not found!")
        exit()
    # Create student entry if new
    if student_name not in students:
        students[student_name] = []
    # Limit check
    if len(students[student_name]) >= 3: 
        print("Issue limit reached! (Max 3 books)")
        exit()
    confirmation = input(("Are you sure you want to issue this book? ")).low()
    if confirmation == 'yes':
         # Availability check
        if books[book_name] == 0:
            print("No copies available!")
            exit()
         # Issue book
        students[student_name].append(book_name)
        books[book_name] -= 1
        print("Book issued successflly!")
        
        print("Current books of", student_name,":",students[student_name])
    else:
        print("Operation cancelled!")
        exit()

# - - - - -  - - - - - Return a book - - - - - - - 

elif choice == 3:

    student_name = input("Enter your name: ").strip()
    if student_name not in students:
        print("Student not found!")
        exit()
    print("\n1. Return a single book")
    print("2. Return ALL books")
    sub_choice = int(input("Enter choice: "))
 # --- RETURN ONE BOOK ---
    if sub_choice == 1:
        book_name = input("Enter a book name to return: ").strip()
        if book_name not in students[student_name]:
            print("This book was not issued to", student_name)
            exit()
        
        students[student_name].remove(book_name)
        books[book_name] += 1
        print("Book returned successfully!")
        print("Current books of ",student_name,": ",students[student_name])
# --- RETURN ALL BOOKS ---
    elif sub_choice == 2:
        if len(students[student_name]) == 0:
            print("No books to return!")
            exit()

        for book in students[student_name]:
            books[book] += 1

        students[student_name].clear()
        print("All books returned successfully!")
    else:
        print("Invalid choice!")
# - - - - - - - - -  show student books - - - - - - 
elif choice == 4:
    student_name = input("Enter your name: ").strip()

    if student_name not in students:
        print("Student not found!")
        exit()

    print(student_name,"'s books:", sorted(students[student_name]))
else:
    print("Invalid choice!")