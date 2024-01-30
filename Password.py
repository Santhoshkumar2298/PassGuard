from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter import messagebox, simpledialog
from config import USERNAME, SECRET_KEY, EMAIL_ID, EMAIL_PASS
from random import choice, randint, shuffle
from datetime import datetime
import pyperclip
import json
import os
import pandas as pd
import smtplib

FONT = ("Microsoft Sans Serif", 10, "bold")
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'",
           '"', ',', '.', '/', '<', '>', '?']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
DATA_PATH = "./data.json"
current_year = datetime.now().year


def create_csv():
    with open(DATA_PATH, 'r') as file:
        json_data = json.load(file)
    df = pd.DataFrame(json_data).transpose()
    df.to_csv("data.csv")


def open_data():
    secret_key = simpledialog.askstring("Authentication Required !", "Enter Secret Key :")

    if secret_key == SECRET_KEY:
        create_csv()
        os.system(f"start ./data.csv")

    else:
        messagebox.showerror("UnAuthorized", "You are not allowed to see the file")


def send_data():
    secret_key = simpledialog.askstring("Authentication Required !", "Enter Secret Key :")
    if secret_key == SECRET_KEY:
        create_csv()

        message = MIMEMultipart()
        message["From"] = EMAIL_ID
        message["To"] = EMAIL_ID
        message["Subject"] = "Secret Data from PassGuard_v1.0"
        message.attach(MIMEBase("application", "octet-stream"))

        with open("./data.csv", "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name="attachment.txt")
            part['Content-Disposition'] = f'attachment; filename="data.csv"'
            message.attach(part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ID, EMAIL_PASS)
            server.sendmail(EMAIL_ID, EMAIL_ID, message.as_string())

        messagebox.showinfo("Information", "Data successfully sent to your Mail")


class Password:
    def __init__(self, canvas: Canvas, home):
        self.canvas = canvas
        self.go_home = home
        self.content_canvas = Canvas(self.canvas, width=700, height=300, bg="#ffffff", relief="ridge")
        self.content_canvas.place(x=50, y=250)

        self.content_canvas.create_text((60, 30), text="Website Title", font=FONT,
                                        fill="#000000")
        self.input_title = Entry(width=70, highlightbackground="blue", highlightcolor="blue", highlightthickness=2)
        self.input_title.focus()
        self.input_title.place(x=170, y=270)

        self.search_btn = Button(width=10, bg="green", fg="#FFFFFF", text="Search", font=FONT, command=self.search)
        self.search_btn.place(x=610, y=270)

        self.content_canvas.create_text((50, 70), text="Email /\nUsername", font=FONT, fill="#000000", justify="center")
        self.input_username = Entry(width=90, highlightcolor="blue", highlightthickness=2, highlightbackground="blue")
        self.input_username.insert(0, USERNAME)
        self.input_username.place(x=170, y=310)

        self.content_canvas.create_text((50, 110), text="Password", font=FONT, fill="#000000")
        self.input_pass = Entry(width=70, highlightcolor="blue", highlightbackground="blue", highlightthickness=2)
        self.input_pass.place(x=170, y=350)
        self.generate_pass_btn = Button(width=10, bg="green", fg="#FFFFFF", text="Generate", font=FONT,
                                        command=self.generate_pass)
        self.generate_pass_btn.place(x=610, y=345)

        self.save_btn = Button(width=50, bg="#039BE5", fg="#ffffff", text="Save / Update", font=FONT,
                               command=self.save_data)
        self.save_btn.place(x=70, y=390)

        self.open_data_btn = Button(width=15, bg="#039BE5", fg="#ffffff", text="My Pass List", font=FONT,
                                    command=open_data)

        self.send_data_btn = Button(width=25, bg="#039BE5", fg="#ffffff", text="Send Data to Mail", font=FONT,
                                    command=send_data)
        if os.path.isfile(DATA_PATH):
            self.open_data_btn.place(x=550, y=390)
            self.send_data_btn.place(x=300, y=440)

        self.logout_btn = Button(width=15, bg="red", fg="#ffffff", text="Logout", font=FONT, command=self.logout)
        self.logout_btn.place(x=570, y=500)

        self.canvas.create_text((400, 570), text=f"{current_year} © Santhoshkumar_V. All rights reserved",
                                        fill='#FFFFFF',
                                        font=("arial", 8, "bold"))

        self.password = ""
        self.new_data = {}

    def search(self):
        try:
            with open("data.json", "r") as file:
                if len(self.input_title.get()) != 0:
                    data = json.load(file)

                    if self.input_title.get().title() in data:
                        search_title = self.input_title.get().title()
                        messagebox.showinfo("Data Found",
                                            f"Website : {search_title}\n\nUsername : {data[search_title]["email"]}"
                                            f"\n\nPassword : {data[search_title]["password"]}")
                    else:
                        messagebox.showinfo("Data Not Found", f"Data Not Found for the term : {self.input_title.get()}")

                else:
                    messagebox.showwarning("Insufficient Data", "Please enter the title of the website")

        except FileNotFoundError:
            messagebox.showinfo("Information", "No data found")

    def generate_pass(self):
        letter_list = [choice(LETTERS) for _ in range(randint(8, 10))]
        symbol_list = [choice(SYMBOLS) for _ in range(randint(2, 4))]
        num_list = [choice(NUMBERS) for _ in range(randint(2, 4))]

        password_list = letter_list + symbol_list + num_list
        shuffle(password_list)

        self.password = "".join(password_list)

        self.input_pass.delete(0, "end")
        self.input_pass.insert(0, self.password)
        pyperclip.copy(self.password)

    def save_data(self):
        entered_title = self.input_title.get()
        entered_username = self.input_username.get()

        if len(entered_title) == 0 or len(entered_username) == 0 or len(self.input_pass.get()) == 0:
            messagebox.showinfo("Insufficient Data", "Please fill all the fields to proceed")
        else:
            self.new_data = {entered_title.title(): {"email": entered_username, "password": self.input_pass.get()}}

            try:
                with open(DATA_PATH, "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(DATA_PATH, "w") as file:
                    json.dump(self.new_data, file, indent=4)

                if os.path.isfile(DATA_PATH):
                    self.open_data_btn.place(x=550, y=390)
                    self.send_data_btn.place(x=300, y=440)

            else:
                data.update(self.new_data)
                with open(DATA_PATH, "w") as file:
                    json.dump(data, file, indent=4)
                if os.path.isfile(DATA_PATH):
                    self.open_data_btn.place(x=550, y=390)
                    self.send_data_btn.place(x=300, y=440)

            finally:
                messagebox.showinfo("Information",
                                    f"The following data saved Successfully. \n\nWebsite: {entered_title}\n\nUsername:"
                                    f" {entered_username}\n\nPassword: {self.input_pass.get()}")
                self.input_title.delete(0, "end")
                self.input_pass.delete(0, "end")

    def logout(self):
        self.content_canvas.destroy()
        self.input_title.destroy()
        self.input_pass.destroy()
        self.input_username.destroy()
        self.search_btn.destroy()
        self.generate_pass_btn.destroy()
        self.send_data_btn.destroy()
        self.save_btn.destroy()
        self.open_data_btn.destroy()
        self.logout_btn.destroy()
        self.go_home()
