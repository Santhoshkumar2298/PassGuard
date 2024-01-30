from datetime import datetime
from tkinter import *
from tkinter import messagebox
from Password import Password
from config import AUTH_KEY


# ---------------------------- FUNCTIONS ---------------------------
def check_auth():
    key = secret_key_input.get()
    if key != "":
        if key == AUTH_KEY:
            destroy_home()
            canvas.create_image((390, 298), image=pass_page)
            Password(canvas, go_home_callback)
        else:
            messagebox.showerror(title="Access Denied !", message="Authentication Error")
    else:
        messagebox.showwarning(title="Invalid Entry!", message="Please Enter the Secret Key to proceed")


# ------------------------------ DELETE HOME ------------------------
def destroy_home():
    global secret_key_input, submit_btn
    canvas.delete("all")

    secret_key_input.destroy()
    submit_btn.destroy()


# ------------------------------- GOHOME CALLBACK -------------------------
def go_home_callback():
    canvas.delete("all")
    home()


# ---------------------------- UI ELEMENTS -------------------------
window = Tk()
window.title("PassGuard_pro_v1.0 ©SANTHOSHKUMAR_V. All rights reserved")
window.resizable(False, False)
window.config(bg="#ffffff")

width = 800
height = 600
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (width / 2) - 20
y = (hs / 2) - (height / 2) - 40
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

back_img = PhotoImage(file="images/pass_back.png")
pass_page = PhotoImage(file="images/passguard.png")

canvas = Canvas(window, width=800, height=600, bg="#ffffff", relief="ridge")
canvas.place(x=0, y=0)
secret_key_input = Entry()
submit_btn = Button()

current_year = datetime.now().year


def home():
    global secret_key_input, submit_btn
    secret_key_input = Entry(width=30)
    submit_btn = Button(text="Authenticate", bg="#01418d", fg="#ffffff", font=("Verdana", 8, "bold"),
                        command=check_auth)

    canvas.create_image((350, 298), image=back_img)
    canvas.create_text((150, 230), text="Enter Auth Key", fill="#ffffff", font=("Verdana", 12, "bold"))

    secret_key_input.focus()
    secret_key_input.place(x=75, y=250)

    submit_btn.config(padx=5, pady=5)
    submit_btn.place(x=160, y=280)

    canvas.create_text((400, 550), text=f"{current_year} © Santhoshkumar_V. All rights reserved", fill='#FFFFFF',
                       font=("arial", 8, "bold"))


home()
window.mainloop()
