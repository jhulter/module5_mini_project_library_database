from connect_mysql import connect_database
genres = {"Horror": "Scary! Might not be suitable for children! Very Frightening",
          "Drama": "These can vary, but mostly they're filled with high emotion and human connection.",
          "Romance": "Lovey Dovey, you know the story... The birds and the bees and all that...",
          "Comedy": "Funny... It's supposed to make you laugh.",
          "Action": "Epic stories that have a lot of big events happening and people against people and a hero vs a villain!",
          "Adventure": "Kinda goes hand in hand with action but most likely will involve a long journey with untold perils along the way",
          "Mystery": "There's something you don't know and you're trying to find out whether that be through investigation of a police officer or private eye",
          "Fiction": "Something that never actually happened",
          "Non-fiction": "Something that really did happen",
         "History": "Anything that has to do with what has already happened in the world whether in this lifetime or before, just the true story of anything in the past"}

class Genres:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

def add_genre():
    genre = input("What genre would you like to add to our collection? ")
    description = input("Describe the genre you would like to add: ")
    genres[genre] = description
    print("Success! " + genre + " has been added to your collection!")

def view_genre_details():
    genre = input("Which genre would you like to hear more about? ")
    print(genres.get(genre))

def display_genres():
    print(genres.keys())


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
            print("Well it was fun while it lasted")
