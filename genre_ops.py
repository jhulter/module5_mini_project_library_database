from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
        cursor = conn.cursor()

class Genres:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

def add_genre():
    name = input("What genre would you like to add to our collection? ")
    description = input("Describe the genre you would like to add: ")
    category = input("What category does this genre fall under? ")
    query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, description, category))
    conn.commit()
    print("Success! The genre " + name + " has been added to our database!")

def view_all_genres(cursor):
    query = "SELECT * FROM genres"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_genre_details():
    view_all_genres(cursor)
    genre_id = input("Of which user would you like to see more details? Please enter the genre ID: ")
    query = "SELECT * FROM genre WHERE id = %s"
    cursor.execute(query, (genre_id,))
    row = cursor.fetchone()
    print(row)

def display_genres():
    query = "SELECT * FROM genres"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def genre_menu():
    while True:
        try:
            print("User Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Quit to previous menu")
            choice = input("Enter a menu choice:")
            if choice == "1":
                add_genre()
            elif choice == "2":
                view_genre_details()
            elif choice == "3":
                display_genres()
            elif choice == "4":
                break
            else:
                print("You entered an incorrect option")
        except:
            print("Something went wrong")
        finally:
            conn.close()
