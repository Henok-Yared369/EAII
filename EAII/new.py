
import tkinter as tk
from tkinter import messagebox

Users = {
    "Abel": {"password": 12345, "borrowed": ""},
    "Kebede": {"password": 12344, "borrowed": ""},
    "Yeabsira": {"password": 36900, "borrowed": ""},
    "Nathan": {"password": 12467, "borrowed": ""},
    "Eyob": {"password": 77777, "borrowed": ""},
    "Abenezer": {"password": 11111, "borrowed": ""}
}

book = ["a", "b", "c", "d", "e", "f"]


def login():
    name = name_entry.get()
    password = password_entry.get()

    try:
        password = int(password)
    except ValueError:
        messagebox.showerror("Error", "Password must be an integer")
        return

    if name not in Users:
        messagebox.showerror(
            "Error",
            "You are not a member of the library"
        )
        return

    if password == Users[name]["password"]:
        menu(name)
    else:
        messagebox.showerror(
            "Error",
            "Password does not match"
        )


def menu(name):
    clear()

    tk.Label(
        root,
        text=f"{name}, Welcome to Ethio Library",
        font=("Arial", 22, "bold")
    ).pack(pady=35)

    tk.Label(
        root,
        text="What would you like to do?",
        font=("Arial", 14)
    ).pack(pady=10)

    tk.Button(
        root,
        text="1. Borrow a book",
        font=("Arial", 13),
        width=25,
        command=lambda: borrow_screen(name)
    ).pack(pady=7)

    tk.Button(
        root,
        text="2. Return a book",
        font=("Arial", 13),
        width=25,
        command=lambda: return_screen(name)
    ).pack(pady=7)

    tk.Button(
        root,
        text="3. Check for borrowed book",
        font=("Arial", 13),
        width=25,
        command=lambda: check(name)
    ).pack(pady=7)

    tk.Button(
        root,
        text="4. Exit",
        font=("Arial", 13),
        width=25,
        command=root.destroy
    ).pack(pady=7)


def borrow_screen(name):
    clear()

    tk.Label(
        root,
        text="Borrow a Book",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    tk.Label(
        root,
        text=f"Available books: {', '.join(book)}",
        font=("Arial", 13)
    ).pack(pady=10)

    tk.Label(
        root,
        text="Enter a book name:",
        font=("Arial", 12)
    ).pack()

    borrowed_entry = tk.Entry(
        root,
        font=("Arial", 14),
        width=20
    )
    borrowed_entry.pack(pady=10)

    def borrow():
        borrowed_book = borrowed_entry.get()

        if borrowed_book in book:
            Users[name]["borrowed"] = borrowed_book
            book.remove(borrowed_book)

            messagebox.showinfo(
                "Success",
                f"You have borrowed {borrowed_book}"
            )

            menu(name)

        else:
            messagebox.showerror(
                "Error",
                "This book is not currently available"
            )

    tk.Button(
        root,
        text="Borrow",
        font=("Arial", 13, "bold"),
        width=15,
        command=borrow
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        font=("Arial", 12),
        width=15,
        command=lambda: menu(name)
    ).pack(pady=5)


def return_screen(name):
    clear()

    tk.Label(
        root,
        text="Return a Book",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    if Users[name]["borrowed"] == "":
        current_text = "You have not borrowed a book."
    else:
        current_text = f"Your borrowed book: {Users[name]['borrowed']}"

    tk.Label(
        root,
        text=current_text,
        font=("Arial", 13)
    ).pack(pady=10)

    tk.Label(
        root,
        text="Enter a book name:",
        font=("Arial", 12)
    ).pack()

    returned_entry = tk.Entry(
        root,
        font=("Arial", 14),
        width=20
    )
    returned_entry.pack(pady=10)

    def return_book():
        returned_book = returned_entry.get()

        if returned_book == Users[name]["borrowed"]:
            book.append(returned_book)
            Users[name]["borrowed"] = ""

            messagebox.showinfo(
                "Success",
                f"You have returned {returned_book}"
            )

            menu(name)

        else:
            messagebox.showerror(
                "Error",
                f"You have not borrowed {returned_book}"
            )

    tk.Button(
        root,
        text="Return",
        font=("Arial", 13, "bold"),
        width=15,
        command=return_book
    ).pack(pady=10)

    tk.Button(
        root,
        text="Back",
        font=("Arial", 12),
        width=15,
        command=lambda: menu(name)
    ).pack(pady=5)


def check(name):
    if Users[name]["borrowed"] == "":
        messagebox.showinfo(
            "Borrowed Book",
            "You have not borrowed a book."
        )
    else:
        messagebox.showinfo(
            "Borrowed Book",
            f"You have borrowed: {Users[name]['borrowed']}"
        )


def clear():
    for widget in root.winfo_children():
        widget.destroy()


root = tk.Tk()
root.title("Ethio Library")
root.geometry("600x500")
root.resizable(False, False)

tk.Label(
    root,
    text="ETHIO LIBRARY",
    font=("Arial", 28, "bold")
).pack(pady=40)

tk.Label(
    root,
    text="Member Login",
    font=("Arial", 16)
).pack(pady=10)

tk.Label(
    root,
    text="Name",
    font=("Arial", 12)
).pack()

name_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
name_entry.pack(pady=5)

tk.Label(
    root,
    text="Password",
    font=("Arial", 12)
).pack()

password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25,
    show="*"
)
password_entry.pack(pady=5)

tk.Button(
    root,
    text="Login",
    font=("Arial", 14, "bold"),
    width=15,
    command=login
).pack(pady=25)

root.mainloop()

