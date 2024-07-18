from connect_mysql import connect_database
authors = { "Roald Dahl":  {"Name": "Roald Dahl",
                            "Biography": "He was born to aliens and learned to write when he was 12"},
            "Hunter S Thompson": {"Name": "Hunter S Thomson",
                                  "Biography": "He wasn't born at all and that made living very hard for him..."}
            }

class Authors:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

def add_author():
    author = input("What author would you like to add? ")
    bio = input("Tell me the life story of the author: ")
    authors.update({author: {"Name": author, "Biography": bio}})
    print("Success! The author " + author + " has been added to our collection!")

def view_author_details():
    author = input("Which author would you like to hear more about? ")
    print(authors.get(author))

def display_authors():
    print(authors.keys())

def author_menu():
    while True:
        try:
            print("User Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Quit to previous menu")
            choice = input("Enter a menu choice:")
            if choice == "1":
                add_author()
            elif choice == "2":
                view_author_details()
            elif choice == "3":
                display_authors()
            elif choice == "4":
                break
            else:
                print("You entered an incorrect option")
        except:
            print("Something went wrong")
