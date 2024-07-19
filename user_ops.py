from connect_mysql import connect_database


conn = connect_database()
if conn is not None:
        cursor = conn.cursor()

class Users:
    def __init__(self, name, library_id, books_checked_out):
        self.name = name
        self._library_id = library_id
        self.books_checked_out = books_checked_out

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter your library ID: ")
    query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
    cursor.execute(query, (name, library_id))
    conn.commit()
    print("Success! The user " + name + " has been added to our database!")

def view_all_users(cursor):
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def view_user_details():
    view_all_users(cursor)
    user_id = input("Of which user would you like to see more details? Please enter the user ID: ")
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    row = cursor.fetchone()
    print(row)

def display_users():
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def user_menu():
    while True:
        try:
            print("User Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Quit to previous menu")
            choice = input("Enter a menu choice:")
            if choice == "1":
                add_user()
            elif choice == "2":
                view_user_details()
            elif choice == "3":
                display_users()
            elif choice == "4":
                break
            else:
                print("You entered an incorrect option")
        except:
            print("Something went wrong")
        finally:
            conn.close()
