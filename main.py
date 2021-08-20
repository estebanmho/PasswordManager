from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search_account():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "There is no password document")
    else:
        try:
            account = data[website_input.get()]
        except :
            messagebox.showerror("Error", "The website does not exist")
        else:
            messagebox.showinfo(website_input.get(), f"Email: {account['email']}\nPassword: {account['password']}")


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    char_list = [random.choice(letters) for char in range(nr_letters)]


    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]

    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = char_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please don't leave any fields empty!")
    else:
        if messagebox.askokcancel(title=website_input.get(), message=f"This are the details you enteres:\n Website: {website}\nEmail:{email} \nPassword:{password}\n It is ok to save?"):
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            finally:
                data.update(new_data)

            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas_image = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas_image.create_image(100, 100, image=image)
canvas_image.grid(padx=20, pady=20,row=0,column=1)

website_label = Label(text="Website:", font=("Times New Roman", 16, "normal"))
website_label.grid(padx=(50, 0), row=1, column=0, sticky="E")
email_label = Label(text="Email/Username:", font=("Times New Roman", 16, "normal"))
email_label.grid(padx=(50, 0), row=2, column=0, sticky="E")
password_label = Label(text="Password:", font=("Times New Roman", 16, "normal"))
password_label.grid(padx=(50, 0), row=3, column=0, sticky="E")

website_input = Entry(width=42)
website_input.grid(row=1, column=1, columnspan=2, sticky="W", padx=20)
website_input.focus()
email_input = Entry(width=70)
email_input.grid(row=2, column=1, columnspan=2, sticky="W", padx=20)
email_input.insert(0, "esteban@gmail.com")
password_input = Entry(width=42)
password_input.grid(row=3, column=1, sticky="W", padx=(20,0))

generate_button = Button(text="Generate Password", width=19, padx=0, command=password_generator)
generate_button.grid(row=3, column=2)
generate_button = Button(text="Search", width=19, padx=0, command=search_account)
generate_button.grid(row=1, column=2)
add_button = Button(text="Add", width=61, command=save_password)
add_button.grid(row=4, column=1, columnspan=2,  pady=(10, 40),padx=(0,40))


window.mainloop()