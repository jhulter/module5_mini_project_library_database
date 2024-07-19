from connect_mysql import connect_database
conn = connect_database()
if conn is not None:
    cursor = conn.cursor()

class Authors:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

def add_author():
    name = input("What author would you like to add? ")
    biography = input("Tell me the life story of the author: ")
    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, biography))
    conn.commit()
    print("Success! The author " + name + " has been added to our collection!")


def view_all_authors(cursor):
    query = "SELECT * FROM authors"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_author_details():
    view_all_authors(cursor)
    author_id = input("Of which author would you like to see more details? Please enter the author ID: ")
    query = "SELECT * FROM authors WHERE id = %s"
    cursor.execute(query, (author_id,))
    row = cursor.fetchone()
    print(row)

def display_authors():
    query = "SELECT * FROM authors"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def author_menu():
    while True:

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



