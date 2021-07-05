import pathlib
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
import mysql.connector
from student_package import student
from admin import start_admin


class Login:
    __username = ""
    __password = ""
    __n = 1

    def __search_username(self, username):
        command1 = "select Aid, Password from Admin where Aid=%s"
        command2 = "select Regno, Password from Student where Regno=%s"
        self.__cur1.execute(command1, [username, ])
        admin = self.__cur1.fetchall()
        self.__cur1.execute(command2, [username, ])
        user = self.__cur1.fetchall()

        if (len(admin) + len(user)) < 1:
            # username not found
            messagebox.showinfo('Error!', 'Invalid Username')
            return False
        else:
            return True

    def __verify_password(self, username, password):
        command1 = "select Aid, Password from Admin where Aid=%s AND Password=%s"
        command2 = "select Regno, Password from Student where Regno=%s AND Password=%s"
        self.__cur1.execute(command1, [username, password])
        admin = self.__cur1.fetchall()
        self.__cur1.execute(command2, [username, password])
        user = self.__cur1.fetchall()

        if (len(admin) + len(user)) < 1:
            # username not found
            messagebox.showinfo('Error!', 'Invalid Password')
            return False
        else:
            if len(admin) > 1:
                admin.start_admin()
            else:
                student.start_student()
            return True

    def __next_or_login(self):

        if len(self.__login_input.get()) == 0:
            print("Empty input")
            messagebox.showinfo("Invalid Input", "Input field can't be empty")
            return

        # if n==1 then read username from login_input
        if self.__n == 1:
            username_input = str(self.__login_input.get())

            result = self.__search_username(username_input)

            if result is True:
                print("username found")
                self.__backbt.place(relx=0.345555, rely=0.58 + 0.1, anchor=CENTER)
                self.__username_display.configure(text=username_input)
                self.__username_display.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.__login_input.delete(0, END)
                self.__login.config(text="Login")
                print("true")
                self.__n = 2
                self.__username = username_input
                self.__login_input.config(show="*")

                return

        # if n==2 then read password from login_input
        if self.__n == 2:
            password_input = str(self.__login_input.get())
            # from here login process will start
            result = self.__verify_password(self.__username, password_input)

            if result:
                # proceed to further page
                print("proceed")
            else:
                return False

    def __back(self):
        if self.__n == 2:
            self.__n = 1
            self.__login_input.config(show='')
            self.__username_display.place_forget()
            self.__backbt.place_forget()
            self.__login.config(text="Next")
            self.__login_input.configure(state=NORMAL)
            self.__login_input.delete(0, END)
            self.__login_input.insert(0, self.__username)
            # self.__login_input.configure(state=DISABLED)
            self.__login_input.place(relx=0.5, rely=0.5 + 0.08, anchor=CENTER)
            # onclick_id = self.__login_input.bind('<Button-1>', self.__placeholder())
            self.__n = 1

    def __init__(self):

        self.__con1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soham",  # Replace XXXX with your MySQL password
            database="library")
        self.__cur1 = self.__con1.cursor()

        self.__win1 = Tk()
        self.__win1.title('Library Management System | Welcome to IIIT Kottayam Library')
        h = (self.__win1.winfo_screenheight() * 4.4) // 5
        # here 50, 6 is the x, y co-ordinate of window respectively
        self.__win1.geometry('%sx%s+%s+%s' % (1150, int(h), 50, 6))
        self.__win1.config(bg='White')
        self.__win1.resizable(False, False)

        # search_user function will be used to search username and password into database and then it will open the next
        # window

        # NEXT BUTTON
        self.__buttonsFont = tkFont.Font(family='product sans', size=15)
        self.__login = Button(self.__win1, text="Next", bg="#4285F4", cursor='hand2', activebackground="#356AC3",
                              activeforeground="white",
                              font=self.__buttonsFont, anchor='c', width=13, relief="flat", fg="white",
                              command=lambda: self.__next_or_login())
        self.__login.place(relx=0.655555, rely=0.58 + 0.1, anchor=CENTER)

        # LOGIN PICTURE
        filePath = pathlib.Path(__file__).parent.absolute()
        self.__img = PhotoImage(file=str(str(filePath) + "\\images\\login_logo.png"))

        self.__login_logo = Label(image=self.__img, bg="white", height=250, width=250)
        self.__login_logo.place(relx=0.5, rely=0.25, anchor=CENTER)

        # LOGIN INPUT
        self.__entryFont = tkFont.Font(family='product sans', size=15)
        self.__login_input = Entry(self.__win1, width=38,
                                   highlightthickness=3,
                                   font=self.__entryFont,
                                   selectborderwidth=3,
                                   relief='flat',
                                   bg="#E4FBFF",
                                   selectbackground="white")
        self.__login_input.insert(0, "Username")
        # self.__login_input.configure(state=DISABLED)
        self.__login_input.place(relx=0.5, rely=0.5 + 0.08, anchor=CENTER)

        # self.__onclick_id = self.__login_input.bind('<Button-1>', lambda event: self.placeholder())
        self.__login_input.bind('<Return>', (lambda event: self.__next_or_login()))
        self.__login_input.bind('<Escape>', (lambda event: self.__back()))
        self.__login_input.bind('<Button-1>', lambda event: self.__login_input.delete(0, END))

        # USERNAME DISPLAY : Label to display user name after clicking on next button
        self.__username_display = Label(bg="white", borderwidth=1, font=self.__buttonsFont)

        # BACK BUTTON
        self.__buttonsFont = tkFont.Font(family='product sans', size=15)
        self.__backbt = Button(self.__win1, text="Back",
                               cursor='hand2', bg="#4285F4",
                               activebackground="#356AC3",
                               activeforeground="white",
                               font=self.__buttonsFont,
                               anchor='c',
                               width=13,
                               relief="flat",
                               fg="white")

        self.__backbt.config(command=lambda backbt=self.__backbt: self.__back())

        self.__win1.mainloop()


obj = Login()
