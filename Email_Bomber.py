from tkinter import *
import Settings as set
from tkinter import messagebox
from _tkinter import TclError


def submit_details():
    server = mailServer_text.get()
    user = fromEmail_text.get()
    passwd = password_text.get()
    to = toEmail_text.get()
    body = body_text.get()

    if len(user) == 0 or len(passwd) == 0 or len(to) == 0 or len(body) == 0:
        messagebox.showwarning(title="Error", message="Please Fill all the Details!")
    else:
        try:
            freq = int(num_text.get())
            messagebox.showinfo(title="Checking...", message="Checking the information...")
            set.bomb_email(server, user, passwd, to, body, freq)
        except ValueError:
            messagebox.showwarning(title="Error", message="Please enter Natural Numbers!")


window = Tk()
window.wm_title("Email-Bomber ☠")
window.geometry("720x480")
window.resizable(False, False)
window.configure(background='AntiqueWhite1')

try:
    photo = PhotoImage(file="bg.gif")
    w = Label(window, image=photo)
    w.pack()
    ent = Entry(window)
    ent.pack()
    ent.focus_set()
except TclError:
    messagebox.showerror(title="Error", message="The background file not found, exiting..")
    sys.exit(1)


lb_mailServer = Label(window, text="Mail Server:", font=("arial", "14", "bold"), bd=1, fg="black").place(x=60, y=110)

lb_toEmail = Label(window, text="To Email:", font=("arial", "14", "bold"), bd=5, fg="black").place(x=60, y=150)

lb_fromEmail = Label(window, text="From Email:", font=("arial", "14", "bold"), bd=5, fg="black").place(x=60, y=190)

lb_password = Label(window, text="Password:", font=("arial", "14", "bold"), bd=5, fg="black").place(x=60, y=230)

lb_body = Label(window, text="Body:", bd=5, font=("arial", "14", "bold"), fg="black").place(x=60, y=270)

lb_freq = Label(window, text="Number:", font=("arial", "14", "bold"), bd=5, fg="black").place(x=60, y=310)

# -----------------

mailServer_text = StringVar()
en_mailServer_text = Entry(window, font=("arial", "14", "bold"), textvariable=mailServer_text, bd=1).place(x=200, y=110)

toEmail_text = StringVar()
en_toEmail_text = Entry(window, font=("arial", "14", "bold"), textvariable=toEmail_text, bd=1).place(x=200, y=150)

fromEmail_text = StringVar()
en_fromEmail_text = Entry(window, font=("arial", "14", "bold"), textvariable=fromEmail_text, bd=1).place(x=200, y=190)

password_text = StringVar()
en_password_text = Entry(window, font=("arial", "14", "bold"), textvariable=password_text, bd=1, show="*").place(x=200, y=230)

body_text = StringVar()
en_body_text = Entry(window, font=("arial", "14", "bold"), textvariable=body_text, bd=1).place(x=200, y=270)

num_text = StringVar()
en_freq_text = Entry(window, font=("arial", "14", "bold"), textvariable=num_text, bd=1).place(x=200, y=310)

# -----------------

send = Button(window, text="Start", width=100, command=submit_details, bd=2, bg="yellow", fg="black").place(x=5, y=400)


window.mainloop()
