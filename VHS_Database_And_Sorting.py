def add_tape():
    print("What tape do you want to add? Enter title, genre, and release year.")

def remove_tape():
    print("What tape would you like to delete from the database? Enter a valid title and release year.")

def search_by_title():
    print("Enter a title and release year to check if it is already in the database.")

def display_entire_collection():
    print("Placeholder text")

def display_genre_and_year():
    print("Placeholder text")

def add_genre():
    print("Enter a new genre to the database")

def remove_genre():
    print("Remove a genre from the database")

def save_database():
    print("Placeholder text")

def load_database():
    print("Placeholder text")


print("Hello, and welcome to VHS Database and Sorting! What would you like me to do for you?")
print("1) Add a new tape to the database")
print("2) Remove a tape from the database")
print("3) Search for a tape already in the database")
print("4) Display your full VHS collection")
print("5) Display all tapes in a specific genre by year")
print("6) Add a genre to the database")
print("7) Remove a genre from the database")
print("8) Save your database")
print("9) Load your database")
user_command = int(input("Enter a command number 1-9: "))

if user_command == 1:
    add_tape()
if user_command == 2:
    remove_tape()
if user_command == 3:
    search_by_title()
if user_command == 4:
    display_entire_collection()
if user_command == 5:
    display_genre_and_year()
if user_command == 6:
    add_genre()
if user_command == 7:
    display_genre_and_year()
if user_command == 8:
    save_database()
if user_command == 9:
    load_database()