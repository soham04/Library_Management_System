from tkinter import *
from PIL import ImageTk, Image
# import pymysql
from tkinter import messagebox
import mysql.connector
from tkinter import font as tkFont
from tkcalendar import Calendar, DateEntry  # pip install tkcalendar
from tkinter import ttk
from student_package import student
# from admin_updated import *
from admin import start_admin
import os


def start_login(w="Default"):
    global n, win1, username, password, isempty
    if __name__ != "__main__":
        w.destroy()
    win1 = Tk()
    win1.title('Library Management System   |   Welcome to IIIT Kottayam Library')
    h = (win1.winfo_screenheight() * 4.4) // 5
    # here 50, 6 is the x, y co-ordinate of window respectively
    win1.geometry('%sx%s+%s+%s' % (1150, int(h), 50, 6))
    win1.config(bg='White')
    win1.resizable(False, False)

    n = 1
    username = password = ""
    isempty = True

    # search_user funtion will be used to serch username and password into database and then it will open the next window
    def search_user():
        global n, username, password, win
        found = False
        command1 = "select Aid, Password from Admin where Aid=%s AND Password=%s"
        var = [username, password]
        command2 = "select Regno, Password from Student where Regno=%s AND Password=%s"
        try:
            # Add your own database name and password here to reflect in the code
            # before running this program create a databse python_pro
            # Create tables admin and student in database python_pro
            con1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sohamsql",  # Replace XXXX with your MySQL password
                database="Library")
            cur1 = con1.cursor()
            cur1.execute(command1, var)
            admin = cur1.fetchall()
            cur1.execute(command2, var)
            user = cur1.fetchall()

            if (len(admin) + len(user)) < 1:
                messagebox.showinfo('Error!', 'Invalid user name or password')
                # back() will erase the data entered by user
                back()
            else:
                if len(admin) > 0:
                    # messagebox.showinfo('sucess','Login Success as Admin')
                    cur1.close()
                    con1.close()
                    found = True
                    back()
                    start_admin(admin[0][0], admin[0][1], win1)
                    # start_admin(admin[0][0],admin[0][1])  -----> admin function call
                    # admin function call will be there
                    # win.destroy()
                if (found != True):
                    cur1.close()
                    con1.close()

                    back()
                    # messagebox.showinfo('sucess','Login Success as Student')
                    student.start_student(user[0][0], user[0][1], win1)

                    # back()
                    # if str(user[0][2]) == "yes":
                    #     messagebox.showinfo('Message', 'You are restricted.')
                    # else:
                    #     student.start_student(user[0][0], user[0][1], win1)

        except Exception as e:
            print(e)
            found = False
            back()
            messagebox.showinfo("Error!", "Something went wrong")
            # back() will erase the data entered by user

    def next_or_login():
        global n, username, password, isempty
        if (login_input.get() == '' or isempty):
            # print("Empty input")
            messagebox.showinfo("Error!", "Input field can't be empty")
            return

        # if n==1 then read username from login_input
        if n == 1:
            username = str(login_input.get())

            login_input.delete(0, END)
            backbt.place(relx=0.345555, rely=0.58 + 0.1, anchor=CENTER)
            unsername_display.configure(text=username)
            unsername_display.place(relx=0.5, rely=0.5, anchor=CENTER)
            n = n + 1
            login.config(text="Login")

            # start
            isempty = True
            login_input.insert(0, "Password")
            login_input.configure(state=DISABLED)
            login_input.place(relx=0.5, rely=0.5 + 0.08, anchor=CENTER)
            onclick_id = login_input.bind('<Button-1>', placeholder)
            # end
            return

        # if n>=2 then read password from login_input
        if n >= 2:
            password = str(login_input.get())
            # from here login process will start
            search_user()

    def back():
        global n
        login_input.delete(0, END)
        n = 1
        login_input.config(show='')
        unsername_display.place_forget()
        backbt.place_forget()
        login.config(text="Next")
        # start
        isempty = True
        login_input.configure(state=NORMAL)
        login_input.delete(0, END)
        login_input.insert(0, "Username")
        login_input.configure(state=DISABLED)
        login_input.place(relx=0.5, rely=0.5 + 0.08, anchor=CENTER)
        onclick_id = login_input.bind('<Button-1>', placeholder)
        # end

    def placeholder(event):
        global isempty, n
        isempty = False
        login_input.configure(state=NORMAL)
        login_input.delete(0, END)
        try:
            login_input.unbind('<Button-1>', onclick_id)
        except:
            print()
        if n > 1:
            login_input.config(show="*")

    # Next button
    buttonsFont = tkFont.Font(family='product sans', size=15)
    login = Button(win1, text="Next", bg="#4285F4", cursor='hand2', activebackground="#356AC3",
                   activeforeground="white",
                   font=buttonsFont, anchor='c', width=13, relief="flat", fg="white", command=next_or_login)
    login.place(relx=0.655555, rely=0.58 + 0.1, anchor=CENTER)

    # Login Picture
    img = PhotoImage(file="D:\\team_project\\project\\login_logo.png")
    # img = PhotoImage(
    # file="C:\\Users\\91969\\Desktop\\SEM 3\\IT WORKSHOP 3\\Project\\Project_code\\Student_section\\Student\\Changable_code\\login_logo.png")
    login_logo = Label(image=img, bg="white", height=250, width=250)
    login_logo.place(relx=0.5, rely=0.25, anchor=CENTER)

    # Login input
    entryFont = tkFont.Font(family='product sans', size=15)
    login_input = Entry(win1, width=38, highlightthickness=3, font=entryFont, selectborderwidth=3,
                        relief='flat', bg="pink", selectbackground="white")
    # start
    login_input.insert(0, "Username")
    login_input.configure(state=DISABLED)
    login_input.place(relx=0.5, rely=0.5 + 0.08, anchor=CENTER)
    onclick_id = login_input.bind('<Button-1>', placeholder)
    # end
    login_input.bind('<Return>', (lambda event: next_or_login()))
    login_input.bind('<Escape>', (lambda event: next_or_login()))

    # Login buttons
    # buttonsFont = tkFont.Font(family='product sans', size=15)
    # Label to display user name after clicking on next button
    unsername_display = Label(bg="white", borderwidth=1, font=buttonsFont)

    # Back Button
    backbt = Button(win1, text="Back", cursor='hand2', bg="#4285F4", activebackground="#356AC3",
                    activeforeground="white",
                    font=buttonsFont, anchor='c', width=13, relief="flat", fg="white", command=back)

    win1.mainloop()


if __name__ == "__main__":
    start_login()
