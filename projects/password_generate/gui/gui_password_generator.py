import random
from tkinter import Tk, Label, Button, StringVar, IntVar, Entry

import pyperclip

# Set screen
root = Tk()
root.geometry("400x400")
root.title("Password Generator")

# Value
password_string = StringVar()
password_length = IntVar()


def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for i in range(password_length.get()):
        password += random.choice(pass1)
    password_string.set(password)


def copy_to_clipboard():
    random_password = password_string.get()
    pyperclip.copy(random_password)


# Draw
Label(root, text="PASSWORD GENERATOR", width="300", height="2",
      font=("Times", 20)).pack()

Label(root, text="Enter Password Length", width="100", height="1",
      font=("Helvetica", 16)).pack()
Entry(root, textvariable=password_length, width="30").pack()
Button(root, text="Generate Password", command=generate).pack()

Entry(root, textvariable=password_string, width="30").pack()
Button(root, text="Copy to clipboard", command=copy_to_clipboard).pack()
root.mainloop()
