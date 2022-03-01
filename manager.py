from tkinter import *
from tkinter import messagebox as mb
import hashlib
import smtplib
import datetime
import re
from random import *
from email.message import EmailMessage
def create_account():
    def validate(rec_otp):
        if len(sender_otp.get()) == 6:
            if rec_otp == sender_otp.get():
                mb.showinfo("success", "Otp validated succesfully")
            else:
                mb.showerror("Try again", "Invalid otp!!\nTry again")
        else:
            mb.showerror("Error", "Please enter a valid otp")
    def send_otp(rec, sender_otp):
        # Stripping out white spaces at both ends
        rec = rec.strip()
        # Regular expression for gmail validation
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, rec):
            try:
                #Create your SMTP session
                server = smtplib.SMTP('smtp.gmail.com', 587)

                #Use TLS to add security
                server.starttls()

                #User Authentication
                server.login("pwdmanager2022@gmail.com","I love devil@7")
                otp = ""
                lis = [str(i) for i in range(10)]
                for i in range(6):
                    otp += choice(lis)
                #Defining The Message
                sender_otp.set(otp)
                message = """Hey user!!!
                Welcome to password manager
                your 6 digit otp is {}""".format(otp)
                #Sending the Email
                email = EmailMessage()
                email["From"] = "pwdmanager2022@gmail.com"
                email["To"] = rec
                email["Subject"] = "Create Account"
                email.set_content(message)
                server.send_message(email)
                #smtp.sendmail("pwdmanager2022@gmail.com",rec,message)

                #Terminating the session
                server.quit()
                mb.showinfo("info", "OTP sent succesfully check your mail")#+str(sender_otp.get()))
                return
            except Exception as ex:
                mb.showerror("error", "Something went wrong plese try again")
                return
        else:
            mb.showerror("error", "Please enter valid email")
    global cre_win
    cre_win = Toplevel(win)
    cre_win.geometry("500x380")
    cre_win.title("Create account")
    cre_win.resizable(0,0)
    cre_win.config(bg = "#9AD9D6")
    Label(cre_win, text = "Create your account", font = ("Comic Sans MS", 15), bg = "#9AD9D6").place(x = 140, y = 8)
    Label(cre_win, text = "=========  ====== =========", font = ("Comic Sans Ms", 10), bg = "#9AD9D6").place(x = 140, y = 37)
    Label(cre_win, text = "Enter email : ", font=("Times New Roman", 13),bg = "#9AD9D6").place(x = 70, y = 70)
    email_id = Entry(cre_win, width = 30, font = ( "Times New Roman", 9))
    email_id.place(x = 180, y = 70)
    sender_otp = StringVar()
    Button(cre_win, text = "Send OTP", font=('Helvetica', 12), bg='orange', command=lambda:send_otp(email_id.get(), sender_otp)).place(x = 170, y = 97)
    Label(cre_win, text = "Enter otp : ", font =("Times New Roman", 13),bg = "#9AD9D6").place(x = 70, y = 140)
    rec_otp = Entry(cre_win, width = 30, font = ( "Times New Roman", 9))
    rec_otp.place(x = 180, y = 140)
    Button(cre_win, text = "Submit",font=('Helvetica', 12), bg='orange', command=lambda:validate(rec_otp.get())).place(x = 170, y = 165)
def generate():
    def gen(pas):
        pa = ""
        lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
        upper = [chr(i) for i in range(ord('A'), ord("Z")+1)]
        digits = [str(i) for i in range(10)]
        special_characters = [i for i in "!#$%*( :\)[]{}|,.?/@+-="]
        combined = lower + upper + digits + special_characters
        pa = choice(upper) + choice(lower) + choice(digits) + choice(special_characters)
        for i in range(12):
            pa += choice(combined)
        pas.set(pa)
    global gen_win
    gen_win = Toplevel(win)
    gen_win.geometry('500x280')
    gen_win.title("Generate")
    gen_win.resizable(0,0)
    gen_win.config(bg = "#4cd273")
    password = StringVar()
    Label(gen_win, text = "Generate your password", font =("Comic Sans MS", 18), bg = "#4cd273").place(x = 140, y = 10)
    Button(gen_win, text='Generate', font=('Helvetica', 14), bg='orange', command=lambda:gen(password)).place(x=210, y=60)

    Label(gen_win, text='Password is:', font=("Times New Roman", 15), bg='Bisque').place(
            x=205, y=115)
    text_entry = Entry(gen_win, width=40, text=password, state='readonly',font=("Times New Roman", 15))
    text_entry.place(x=45, y=165, height=40)


win = Tk()
win.geometry('700x400')
win.title("Password Manager")
win.resizable(0,0)
win.config(bg = '#1CF2E7')
info = r'''Hey Buddy!!!
This is Dev.
I am your password manager.
I keep your passwords safe and secure.
I can suggest you a secure passowrd if you need one.
'''
#mb.showinfo("Read me", info)
Label(win, text = "Password Manager", font =( 'Playfair Display', 25), bg = '#1CF2E7').place(x = 210, y = 20)
Button(win, text='Generate', width=25, font=('Times New Roman', 13), bg='SteelBlue', command=generate).place(
        x=240, y=100)
Button(win, text='Create Account', width=25, font=('Times New Roman', 13), bg='SteelBlue', command=create_account).place(
        x=240, y=160)
win.update()
win.mainloop()
