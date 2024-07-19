from connect_mysql import connect_database
conn = connect_database()
if conn is not None:
        cursor = conn.cursor()

class Books:
    def __init__(self, id, title, author, genre, isbn, publication_date, availability_status):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability_status = availability_status

def borrow_book():
    user_id = input("Enter your user ID: ")
    book_borrowed = input("Enter in the book ID: ")
    borrow_date = input("Enter in the borrow_date: ")
    return_date = input("Enter in the return date: ")
    query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_id, book_borrowed, borrow_date, return_date))
    conn.commit()
    print(f"You've checked out {book_borrowed}")

def return_book():
    title = input("Which title would you like to return? ")
    author_id = input("What is the author ID associated with this book? ")
    genre_id = input("What is the genre ID associated with this book? ")
    isbn = input("What is the isbn? ")
    publication_date = input("What is the publication date? ")
    availability = True
    query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (title, author_id, genre_id, isbn, publication_date, bool(availability)))
    conn.commit()
    print(f"You've checked in {title}")

def search_books():
        search_book = input("What book are you trying to find? ")
        query = "SELECT * FROM books WHERE title = %s"
        cursor.execute(query, (search_book,))
        row = cursor.fetchone()
        print(row)


def display_books():
    query = "SELECT * FROM books"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_book():
        title = str(input("Enter title: "))
        author_id = input("Enter author ID: ")
        genre_id = input("Enter the genre ID: ")
        isbn = input("Enter ISBN #: ")
        publication_date = input("Enter the publication date: ")
        query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (title, author_id, genre_id, isbn, publication_date))
        conn.commit()
        print("Book Added!!!!")

def books_menu():
    while True:
            print("Book Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Quit to previous menu")
            choice = input("Enter a menu choice:")
            if choice == "1":
                add_book()
            elif choice == "2":
                borrow_book()
            elif choice == "3":
                return_book()
            elif choice == "4":
                search_books()
            elif choice == "5":
                display_books()
            elif choice == "6":
                break
            else:
                print("You entered an incorrect option")




