from connect_mysql import connect_database
users = {1: {"Name": "Jeff", "Library ID": 1, "Books Checked out": ["One flew over the Cuckoos Nest", "Maverick"]}, 2: {"Name": "Bill", "Library ID": 2, "Books Checked out": ["Peter Pan"]},}

class Users:
    def __init__(self, name, library_id, books_checked_out):
        self.name = name
        self._library_id = library_id
        self.books_checked_out = books_checked_out

def add_user():
    name = input("Enter your name: ")
    library_id = input("Enter your library ID: ")
    books_out = []
    users.update({library_id: {"Name": name, "Library ID": library_id, "Books check out": books_out }})

def view_user_details():
    user = int(input("Enter the Library ID of the User you wish to view: "))
    print(users[user + 1])

def display_users():
    [print(key, ':', value) for key, value in users.items()]

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
            print("It's been fun anyway")
