from connect_mysql import connect_database
library = { "Tarzan" :
                {"Title" : "Tarzan",
                "Author": "George",
                "Genre": "Romance",
                "ISBN": 1,
                "Publication Date": 2023,
                "Availability Status": "Available"},
            "Fear and Loathing in Las Vegas" :
                {"Title" : "Fear and Loathing in Las Vegas",
                "Author": "Hunter S Thompson",
                "Genre": "Romance",
                "ISBN": 2,
                "Publication Date": 2023,
                "Availability Status": "Available"},
            "Jaws" : {
                "Title": "Jaws",
                "Author": "Shakespear",
                "Genre": "Romance",
                "ISBN": 3,
                "Publication Date": 2001,
                "Availability Status": "Unavailable"
            }
           }


class Books:
    def __init__(self, title, author, genre, isbn, publication_date, availability_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability_status = availability_status

def borrow_book(library):
    book_barrowed = input("Which title would you like to borrow? ")
    if book_barrowed in library:
        library[book_barrowed ]["Availability Status"] = "Unavailable"
        print(f"You've checked out {book_barrowed}")

def return_book(library):
    book_barrowed = input("Which title would you like to return? ")
    if book_barrowed in library:
        library[book_barrowed ]["Availability Status"] = "Available"
        print(f"You've checked in {book_barrowed}")

def search_books(library):
        search_book = input("What book are you trying to find? ")
        print(library.get(search_book))

def display_books(library):
    [print(key, ':', value) for key, value in library.items()]

def add_book(library):
        title = str(input("Enter title: "))
        author = input("Enter author: ")
        genre = input("Enter the genre: ")
        isbn = input("Enter ISBN #: ")
        publication_date = input("Enter the publication date: ")
        availability_status = True
        library.update({title: {"Title": title, "Author": author, "Genre": genre, "ISBN": isbn, "Publication Date": publication_date, "Avaliability Status": availability_status}})
        print("Book Added!!!!")

def books_menu():
    while True:
        try:
            print("Book Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Quit to previous menu")
            choice = input("Enter a menu choice:")
            if choice == "1":
                add_book(library)
            elif choice == "2":
                borrow_book(library)
            elif choice == "3":
                return_book(library)
            elif choice == "4":
                search_books(library)
            elif choice == "5":
                display_books(library)
            elif choice == "6":
                break
            else:
                print("You entered an incorrect option")
        except:
            print("Something went wrong")



