from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password = ""


def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_lst = random.sample(letters, 4) + random.sample(symbols, 4) + random.sample(numbers, 4)
    random.shuffle(password_lst)

    global password
    for ch in password_lst:
        password += ch
    pyperclip.copy(password)
    password_field.insert(END, string=password)
# ---------------------------- SAVE DATA  ------------------------------- #


def add():
    global password
    email = email_field.get()
    website = website_field.get()
    password = password_field.get()

    check = messagebox.askokcancel(title=website,
        message=f"These are the details entered: \nEmail/Username:{email}\nPassword: {password}\nIs it OK to save?")

    if check:
        if email == "" or website == "" or password == "":
            warning_label.config(text="DO NOT LEAVE A FIELD EMPTY")
        else:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
            email_field.delete(0, END)
            website_field.delete(0, END)
            password_field.delete(0, END)
            password = ""
            warning_label.config(text="")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(600, 600)
window.title("Password Manager")
logo = PhotoImage(file="logo.png")

logo_label = Label(image=logo)
logo_label.place(x=190, y=80)

website_label = Label(text="Website:", font=("Ubuntu", 18), fg="Grey")
website_label.place(x=110, y=278)
website_field = Entry(width=35)
website_field.place(x=190, y=280)
website_field.focus()

email_label = Label(text="Email/Username:", font=("Ubuntu", 18), fg="Grey")
email_label.place(x=45, y=318)
email_field = Entry(width=35)
email_field.place(x=190, y=320)

password_label = Label(text="Password:", font=("Ubuntu", 18), fg="Grey")
password_label.place(x=100, y=360)
password_field = Entry(width=16)
password_field.place(x=190, y=360)

warning_label = Label(text="", font=("Ubuntu", 18), fg="Red")
warning_label.place(x=190, y=450)


generate_button = Button(text="Generate Password", font=("Ubuntu", 14), bg="Grey", fg="Black",
                         highlightthickness=1, command=generator)
generate_button.place(x=360, y=359)

add_button = Button(text="Add", font=("Ubuntu", 14),
                    bg="Grey", fg="Black", highlightthickness=1, width=36, command=add)
add_button.place(x=190, y=400)

window.mainloop()
