import json

USERS_FILE="user_data.json"
BOOKS_FILE="books_data.json"


def load_data():

    global Users, book
    try:
        with open(USERS_FILE, "r") as f:
            Users = json.load(f)
        with open(BOOKS_FILE, "r") as f:
            book = json.load(f)
    except FileNotFoundError:

        Users={"Abel": {"password":12345, "borrowed":""},
               "Kebede": {"password":12344, "borrowed":"" },
               "Yeabsira": {"password": 36900, "borrowed":"" },
               "Nathan": {"password":12467, "borrowed":"" },
               "Eyob": {"password":77777, "borrowed":"" },
               "Abenezer":{"password": 11111, "borrowed":""}
               }
        book= ["a", "b", "c", "d", "e", "f"]


def save_data():

    with open(USERS_FILE, "w") as f:
        json.dump(Users, f, indent=4)

    with open(BOOKS_FILE, "w") as f:
        json.dump(book, f, indent=4)


def login():

    name= input("Name: ")
    if name in Users:
        while True:
            while True:
                try:
                    password=int(input("Password: "))
                    break
                except ValueError:
                    print("Password must be an integer")
            if password == Users[name]["password"]:
                        return name
            else:
                print("Password does not match")
    else:
        print("You are not a member of the library")
    return login()

def menu(name):

            print(f"{name}, Welcome to Ethio library")
            print("What would you like to do?")
            print("1. Borrow a book")
            print("2. Return a book")
            print("3. Check for borrowed book")
            print("4. Exit")
            nums={1,2,3,4}

            while True:
                try:
                    choice= int(input("Choose a number: "))
                    if choice in nums:
                        return choice
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Choose a number")


def borrow(name):
        if Users[name]["borrowed"]:
            print(f"Denied, you must return {Users[name]['borrowed']} first")
            return
        print(f"Available books: {book}")
        borrowed_book = input("Enter a book name: ")

        if borrowed_book in book:
            Users[name]["borrowed"] = borrowed_book
            book.remove(borrowed_book)
            save_data()
            print(f"You have borrowed {borrowed_book}")

        elif borrowed_book not in book:
            print("This book is not currently available")


def returnbook(name):
        if Users[name]["borrowed"] == "":
            print("You have not borrowed any books to return!")
            return

        return_book = input("Enter a book name: ")

        if return_book == Users[name]["borrowed"]:
            book.append(return_book)
            Users[name]["borrowed"]= ""
            save_data()
            print(f"You have returned {return_book}")

        else:
            print(f"You have not borrowed {return_book}")


def check(name):

        print(Users[name]["borrowed"])


def library():

    load_data()
    name = login()

    if not name:
        return
    while True:
        choice= menu(name)

        if choice == 1:
            borrow(name)

        elif choice == 2:
            returnbook(name)

        elif choice == 3:
            check(name)

        elif choice == 4:
            print("Thank you for using Ethio library")
            return

library()