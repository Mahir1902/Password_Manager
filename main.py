from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)


    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    website = website_input.get()
    email_username = email_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website,
                                   message=f'Details entered:\nEmail: {email_username}\nPassword: {password}\nDo you want to save?')
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Opps', message='Please fill all fields.')
    else:
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{website} | {email_username} | {password}\n')

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
image = PhotoImage(file='logo.png')
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 95, image=image)
canvas.grid(row=0, column=1)

website_text = Label(text='Website:')
website_input = Entry()
website_input.focus()
website_text.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)
website_input.config(width=45)

email_text = Label(text='Email/Username:')
email_input = Entry()
email_input.insert(0, 'mahirhaque7@gmail.com')
email_text.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)
email_input.config(width=45)

password_text = Label(text='Password:')
password_input = Entry()
password_text.grid(row=3, column=0)
password_input.grid(row=3, column=1)
password_input.config(width=27)

generate_button = Button(text='Generate Password', command=generate_pass)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', command=add_info)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(width=36)

window.mainloop()
