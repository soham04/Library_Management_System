from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
import mysql.connector
from tkinter import font as tkFont
from tkcalendar import Calendar, DateEntry  # pip install tkcalendar
from datetime import date

# from ad_student import *


def start_admin(user, password, win1="default"):

    if __name__ != "__main__":
        win1.destroy()

    today = date.today()
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sohamsql",  # Replace XXXX with your MySQL password
        database="Library")
    cur = con.cursor()
    # '''Create this database(Library) and add the student table as:
    #  create table Students(Fullname varchar(30) NOT NULL,Username varchar(15) NOT NULL,
    # Email varchar(50) NOT NULL,Password varchar(20) NOT NULL,Contact int(10) NOT NULL,
    # Age int(3) NOT NULL,Batch int(4) NOT NULL,Course varchar(20) NOT NULL,PRIMARY KEY (Username));'''

    # '''add books table as:
    #  create table books(B_ID VARCHAR(10) NOT NULL, B_NAME VARCHAR(20) NOT NULL, AUTHOR VARCHAR(30) NOT NULL,
    # S_ID VARCHAR(10) NOT NULL, S_NAME VARCHAR(20) NOT NULL, C_NAME VARCHAR(20) NOT NULL,
    # PRIMARY KEY (B_ID));'''

    Regno = user

    # start
    # fetching data of user after login
    command = "select Aname,Aid,Email,password from admin where Aid=%s and password=%s"
    var = [user, password]
    cur.execute(command, var)
    user_details = cur.fetchall()

    admin = Tk()
    admin.title(str("Hii, "+user_details[0][0]) +
                "  |   Welcome to IIIT Kottayam Library")
    # admin.minsize(width=400,height=400)
    admin.geometry("1150x630+50+5")
    admin.resizable(False, False)
    # creating menubar
    menubar = Menu(admin)

    Canvas1 = Canvas(admin)
    Canvas1.config(bg="#ab9672")  # B8DBE6
    Canvas1.pack(expand=True, fill=BOTH)

    '''def SearchStudents():
        global search_entry
        search = str(search_entry.get())'''

    header_admin = Label(admin, text='ADMIN', bg='#525b59', fg='white')
    header_admin.place(relx=0.65, rely=0.02, relwidth=0.08, relheight=0.05)

    header_username = Button(admin, text=user_details[0][0], fg='black')
    header_username.place(relx=0.74, rely=0.02, relwidth=0.16, relheight=0.05)

    # , bd='2', font=fineFont, command=lambda x=admin: start_login(admin)
    logout = Button(admin, text='Logout', bg='Red',
                    fg='Black', activeforeground='black')
    logout.place(relx=0.9, rely=0.02, relwidth=0.06, relheight=0.05)

    # Reload=Button(admin,text='Reload',fg='black',command=start_admin(user_details[0][1],user_details[0][3]))
    # Reload.place(relx=0.04,rely=0.02,relwidth=0.15,relheight=0.05)

    # headingFrame1 = Frame(admin,bg="#FFBB00",bd=2)
    # headingFrame1.place(relx=0,rely=0.0,relwidth=1,relheight=0.08)

    # headingLabel = Label(headingFrame1, text="Welcome ADMIN", bg='black', fg='white', font=('Courier',15))
    # headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    def student_print(val):
        rows = val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.02, rely=0.04, relwidth=0.94, relheight=0.91)
        lboxs.delete(0, 'end')
        # start
        v = Scrollbar(labelFrame, orient='vertical')
        # v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side=RIGHT, fill=Y)
        h = Scrollbar(labelFrame, orient='horizontal')
        # h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side=BOTTOM, fill=X)
        t = Text(lboxs, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end

        reg = Label(lboxs, text='Registration Number', bg='#97cee3',
                    fg='white', width=23, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_name = Label(lboxs, text='Name', bg='#97cee3',
                       fg='white', width=15, font='BOLD', anchor='w')
        t.window_create(END, window=s_name)
        s_mail = Label(lboxs, text='Batch', bg='#97cee3',
                       fg='white', width=17, font='BOLD', anchor='c')
        t.window_create(END, window=s_mail)
        s_phone = Label(lboxs, text='History', bg='#97cee3',
                        fg='white', width=15, font='BOLD', anchor='c')
        t.window_create(END, window=s_phone)
        s_batch = Label(lboxs, text='Update', bg='#97cee3',
                        fg='white', font='BOLD', width=10, anchor='c')
        t.window_create(END, window=s_batch)
        s_course = Label(lboxs, text='Pending', bg='#97cee3',
                         fg='white', width=14, font='BOLD', anchor='c')
        t.window_create(END, window=s_course)
        s_fine = Label(lboxs, text='Mail', bg='#97cee3',
                       fg='white', width=12, font='BOLD', anchor='c')
        t.window_create(END, window=s_fine)
        t.insert(END, "\n")

        for row in rows:
            x = row[0]
            # )#, anchor='w',text=row[0
            reg = Label(lboxs, bg='yellow', fg='black',
                        width=25, anchor='w', text=row[0])
            t.window_create(END, window=reg)
            s_name = Label(
                lboxs, text=row[1], bg='yellow', fg='black', width=33, anchor='w')
            t.window_create(END, window=s_name)
            s_mail = Label(
                lboxs, text=row[2], bg='yellow', fg='black', width=15, anchor='w')
            t.window_create(END, window=s_mail)
            s_phone = Button(lboxs, text='History', bg='yellow', fg='black',
                             width=15, anchor='c', command=(lambda y=x: print_his(y)))
            t.window_create(END, window=s_phone)
            s_batch = Button(lboxs, text='Update', bg='yellow', fg='black',
                             width=15, anchor='c', command=(lambda y=x: up_stu(y)))
            t.window_create(END, window=s_batch)
            s_course = Button(lboxs, text='Pending', bg='yellow', fg='black',
                              width=15, anchor='c', command=(lambda y=x: pending_stu(y)))
            t.window_create(END, window=s_course)
            s_fine = Button(lboxs, text='Mail', bg='yellow',
                            fg='black', width=15, anchor='c')
            t.window_create(END, window=s_fine)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)

    def book_print(val):
        rows = val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.02, rely=0.04, relwidth=0.94, relheight=0.91)
        lboxs.delete(0, 'end')
        # start
        v = Scrollbar(labelFrame, orient='vertical')
        # v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side=RIGHT, fill=Y)
        h = Scrollbar(labelFrame, orient='horizontal')
        # h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side=BOTTOM, fill=X)
        t = Text(lboxs, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end

        reg = Label(lboxs, text='Book ID', bg='#97cee3',
                    fg='white', width=16, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_name = Label(lboxs, text='Book Name', bg='#97cee3',
                       fg='white', width=15, font='BOLD', anchor='w')
        t.window_create(END, window=s_name)
        s_mail = Label(lboxs, text='Author', bg='#97cee3',
                       fg='white', width=18, font='BOLD', anchor='c')
        t.window_create(END, window=s_mail)
        s_phone = Label(lboxs, text='Subject', bg='#97cee3',
                        fg='white', width=13, font='BOLD', anchor='c')
        t.window_create(END, window=s_phone)
        s_batch = Label(lboxs, text='Category', bg='#97cee3',
                        fg='white', font='BOLD', width=13, anchor='c')
        t.window_create(END, window=s_batch)
        s_course = Label(lboxs, text='Update', bg='#97cee3',
                         fg='white', width=18, font='BOLD', anchor='c')
        t.window_create(END, window=s_course)
        s_fine = Label(lboxs, text='Status', bg='#97cee3',
                       fg='white', width=12, font='BOLD', anchor='c')
        t.window_create(END, window=s_fine)
        t.insert(END, "\n")

        for row in rows:
            x = row[0]
            # )#, anchor='w',text=row[0
            reg = Label(lboxs, bg='yellow', fg='black',
                        width=15, anchor='w', text=row[0])
            t.window_create(END, window=reg)
            s_name = Label(
                lboxs, text=row[1], bg='yellow', fg='black', width=33, anchor='w')
            t.window_create(END, window=s_name)
            s_mail = Label(
                lboxs, text=row[2], bg='yellow', fg='black', width=17, anchor='w')
            t.window_create(END, window=s_mail)
            s_phone = Label(
                lboxs, text=row[3], bg='yellow', fg='black', width=13, anchor='c')
            t.window_create(END, window=s_phone)
            s_batch = Label(
                lboxs, text=row[4], bg='yellow', fg='black', width=20, anchor='c')
            t.window_create(END, window=s_batch)
            s_course = Button(lboxs, text='Update', bg='yellow', fg='black', width=18, anchor='c', command=(
                lambda y=x: update_book_all(y)))  # ,command= book_update()
            t.window_create(END, window=s_course)
            s_fine = Button(lboxs, text='Status', bg='yellow', fg='black',
                            width=18, anchor='c', command=(lambda y=x: b_status(y)))
            t.window_create(END, window=s_fine)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)

    def search_student(val):
        if combo_student.get() == 'Registation Number':
            x = search_entry.get()
            cur.execute(
                "select Regno,Sname,Batch from student where Regno='" + str(x) + "'")
            rows = list(cur.fetchall())
            student_print(rows)

        elif combo_student.get() == 'Name':
            x = search_entry.get()
            cur.execute(
                "select Regno,Sname,Batch from student where Sname='" + str(x) + "'")
            rows = list(cur.fetchall())
            student_print(rows)

    def search_books(val):
        if combo_book.get() == 'Category':
            x = search_entry.get()
            cur.execute(
                "select Bid,Bname,Author,Subject_name,CName from Book where CName='" + str(x) + "'")
            rows = list(cur.fetchall())
            book_print(rows)

        elif combo_book.get() == 'Subject':
            x = search_entry.get()
            cur.execute(
                "select Bid,Bname,Author,Subject_name,CName from Book where Subject_name='" + str(x) + "'")
            rows = list(cur.fetchall())
            book_print(rows)

        elif combo_book.get() == 'Name':
            x = search_entry.get()
            cur.execute(
                "select Bid,Bname,Author,Subject_name,CName from Book where Bname='" + str(x) + "'")
            rows = list(cur.fetchall())
            book_print(rows)

        elif combo_book.get() == 'Book ID':
            x = search_entry.get()
            cur.execute(
                "select Bid,Bname,Author,Subject_name,CName from Book where Bid='" + str(x) + "'")
            rows = list(cur.fetchall())
            book_print(rows)

        elif combo_book.get() == 'Sub Book ID':
            x = search_entry.get()
            cur.execute(
                "select book.Bid,book.Bname,book.Author,book.Subject_name,book.CName from book,Subbook where book.Bid=Subbook.Bid and Sub_bid='" + str(x) + "'")
            rows = list(cur.fetchall())
            book_print(rows)

    '''def search_placeholder(event):
        isempty=False
        search_entry.configure(state=NORMAL)
        search_entry.delete(0, END)
        try:
            search_entry.unbind('<Button-1>', onclick_id)
        except:
            print()
        if n>1:
            search_entry.config(show="*")'''

    # search entry
    search_entry = Entry(admin)
    search_entry.insert(0, 'Search Students/Books')
    search_entry.place(relx=0.04, rely=0.09, relwidth=0.92, relheight=0.06)
    '''search_entry.configure(state=DISABLED)
    onclick_id=search_entry.bind('<Button-1>', search_placeholder)#'''

    # Search Students
    combo_student = ttk.Combobox(admin, values=[
                                 "Search Student Using...", "Registation Number", "Name"], state="readonly")
    combo_student.place(relx=0.04, rely=0.15, relwidth=0.45, relheight=0.05)
    combo_student.current(0)
    combo_student.bind("<<ComboboxSelected>>", search_student)
    # combo_student.pack()
    # sr1 = Button(admin,text="Search Students",bg='#525b59', fg='white')#,command=SearchStudents)
    # sr1.place(relx=0.34,rely=0.15, relwidth=0.15, relheight=0.05)

    # Search books
    combo_book = ttk.Combobox(admin, values=[
                              "Search Books Using...", "Category", "Subject", "Name", "Book ID", "Sub Book ID"], state="readonly")
    combo_book.place(relx=0.51, rely=0.15, relwidth=0.45, relheight=0.05)
    combo_book.current(0)
    combo_book.bind("<<ComboboxSelected>>", search_books)
    # combo_book.pack()
    # sr2 = Button(admin,text="Search Books",bg='#525b59', fg='white')#,command=SearchBooks)
    # sr2.place(relx=0.81,rely=0.15, relwidth=0.15, relheight=0.05)

    # img = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Downloads\\library_1.jpg").resize((1050, 440), Image.ANTIALIAS))
    labelFrame = Label(admin, bg="black")
    # labelFrame.image=img
    labelFrame.place(relx=0.04, rely=0.25, relwidth=0.92, relheight=0.71)

    welcome = Label(labelFrame, text="Welcome to\nIIIT Kottayam Library",
                    fg='white', bg='#504e4e', font='bold')
    welcome.place(relx=0.2, rely=0.35, relheight=0.3, relwidth=0.4)
    welcome.config(font=("Comic", 24))

    # Adding student to the Database
    def adds():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # Validating and add
        def add_stu():
            fname = str(fullname1.get())
            usern = str(username1.get())
            mail = str(email1.get())
            passwrd = str(password1.get())
            cont = str(contact1.get())
            dob = str(dob1.get())
            batch = str(batch1.get())
            course = str(course1.get())
            rest = 'no'
            if(res.get() == 1):
                rest = 'yes'
            bir = dob.split('/')
            dob = ''
            if len(bir[2]) == 4:
                dob = bir[2]+'-'+bir[1]+'-'+bir[0]
            else:
                dob = '20'+bir[2]+'-'+bir[1]+'-'+bir[0]
            fine = '0'
            if(fname == '' or usern == "" or mail == "" or cont == None or dob == None or batch == "" or course == "" or passwrd == "") != False:
                messagebox.showinfo("Can't ADD", "All feilds are required!")
            elif(mail.endswith('@iiitkottayam.ac.in')) != True:
                messagebox.showinfo(
                    "Invalid Email", "Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
            elif(cont.isnumeric() and len(cont) == 10) != True:
                messagebox.showinfo("Invalid Contact Number",
                                    "Enter a valid Contact Number(Length 10)!")
            elif (batch.isnumeric()) != True:
                messagebox.showinfo(
                    "Invalid Batch", "Batch should be number and in format '20XX' !")
            elif(usern.isalnum()) != True:
                messagebox.showinfo("Invalid Username",
                                    "Username should be Alphanumeric!")
            else:
                try:
                    addformula = "INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Course, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    add_student = (fname, usern, passwrd, cont,
                                   mail, batch, dob, fine, course, rest)
                    cur.execute(addformula, add_student)
                    con.commit()
                    fullname1.delete(0, 'end')
                    username1.delete(0, 'end')
                    email1.delete(0, 'end')
                    password1.delete(0, 'end')
                    contact1.delete(0, 'end')
                    dob1.delete(0, 'end')
                    batch1.delete(0, 'end')
                    course1.delete(0, 'end')
                    messagebox.showinfo(
                        "Student Added", "Student is added successfully!")
                except(mysql.connector.errors.IntegrityError):
                    messagebox.showinfo("Can't add Student",
                                        "Oops!!\nUsername already exist!!")

        details = Label(labelFrame, text="Add Details:", bg='white', fg='black', font='BOLD').place(
            relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        fullname = Label(labelFrame, text="Full name", bg='black', fg='white').place(
            relx=0.1, rely=0.18, relwidth=0.25, relheight=0.07)
        username = Label(labelFrame, text="Username", bg='black', fg='white').place(
            relx=0.1, rely=0.27, relwidth=0.25, relheight=0.07)
        email = Label(labelFrame, text="Email Id", bg='black', fg='white').place(
            relx=0.1, rely=0.36, relwidth=0.25, relheight=0.07)
        password = Label(labelFrame, text="Password", bg='black', fg='white').place(
            relx=0.1, rely=0.45, relwidth=0.25, relheight=0.07)
        contact = Label(labelFrame, text="Contact no.", bg='black', fg='white').place(
            relx=0.1, rely=0.54, relwidth=0.25, relheight=0.07)
        dob = Label(labelFrame, text="Date Of Birth", bg='black', fg='white').place(
            relx=0.1, rely=0.63, relwidth=0.25, relheight=0.07)
        batch = Label(labelFrame, text="Batch", bg='black', fg='white').place(
            relx=0.1, rely=0.72, relwidth=0.25, relheight=0.07)
        course = Label(labelFrame, text="Course", bg='black', fg='white').place(
            relx=0.1, rely=0.81, relwidth=0.25, relheight=0.07)
        restrict = Label(labelFrame, text="Is Restricted?", bg='black', fg='white').place(
            relx=0.1, rely=0.90, relwidth=0.25, relheight=0.07)

        res = IntVar()
        res.set(2)

        fullname1 = Entry(labelFrame, bg='#cecece', fg='black')
        fullname1.place(relx=0.5, rely=0.18, relwidth=0.3, relheight=0.06)
        # print('fullname1',fullname1)
        username1 = Entry(labelFrame, bg='#cecece', fg='black')
        username1.place(relx=0.5, rely=0.27, relwidth=0.3, relheight=0.06)
        email1 = Entry(labelFrame, bg='#cecece', fg='black')
        email1.place(relx=0.5, rely=0.36, relwidth=0.3, relheight=0.06)
        password1 = Entry(labelFrame, bg='#cecece', fg='black')
        password1.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.06)
        contact1 = Entry(labelFrame, bg='#cecece', fg='black')
        contact1.place(relx=0.5, rely=0.54, relwidth=0.3, relheight=0.06)
        dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy',
                         state="readonly", bg='#cecece', fg='black')
        dob1.place(relx=0.5, rely=0.63, relwidth=0.15, relheight=0.06)
        batch1 = Entry(labelFrame, bg='#cecece', fg='black')
        batch1.place(relx=0.5, rely=0.72, relwidth=0.3, relheight=0.06)
        course1 = Entry(labelFrame, bg='#cecece', fg='black')
        course1.place(relx=0.5, rely=0.81, relwidth=0.3, relheight=0.06)
        re1 = Radiobutton(labelFrame, text="Yes", bg='#cecece', fg='black')
        re1.place(relx=0.5, rely=0.90, relwidth=0.12, relheight=0.06)
        re1.config(variable=res, val=1)
        re2 = Radiobutton(labelFrame, text="No", bg='#cecece', fg='black')
        re2.place(relx=0.65, rely=0.90, relwidth=0.12, relheight=0.06)
        re2.config(variable=res, val=2)

        add = Button(labelFrame, text='Add', bg='#7d7d7d', fg='black', command=add_stu).place(
            relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

    # View all the students from the database

    def views():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.02, rely=0.04, relwidth=0.94, relheight=0.91)

        # print_his()

        # def show():
        lboxs.delete(0, 'end')
        # start
        v = Scrollbar(labelFrame, orient='vertical')
        # v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side=RIGHT, fill=Y)
        h = Scrollbar(labelFrame, orient='horizontal')
        # h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side=BOTTOM, fill=X)
        t = Text(lboxs, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end
        cur.execute(
            "select Regno, Sname, Email, Phone, Batch, Course, Fine from student order by Regno")
        rows = list(cur.fetchall())

        reg = Label(lboxs, text='Reg.No.', bg='#97cee3',
                    fg='white', width=10, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_name = Label(lboxs, text='Name', bg='#97cee3',
                       fg='white', width=15, font='BOLD', anchor='w')
        t.window_create(END, window=s_name)
        s_mail = Label(lboxs, text='Email', bg='#97cee3',
                       fg='white', width=25, font='BOLD', anchor='c')
        t.window_create(END, window=s_mail)
        s_phone = Label(lboxs, text='Contact', bg='#97cee3',
                        fg='white', width=10, font='BOLD', anchor='c')
        t.window_create(END, window=s_phone)
        s_batch = Label(lboxs, text='Batch', bg='#97cee3',
                        fg='white', font='BOLD', width=10, anchor='c')
        t.window_create(END, window=s_batch)
        s_course = Label(lboxs, text='Course', bg='#97cee3',
                         fg='white', width=9, font='BOLD', anchor='c')
        t.window_create(END, window=s_course)
        s_fine = Label(lboxs, text='Fine', bg='#97cee3',
                       fg='white', width=11, font='BOLD', anchor='c')
        t.window_create(END, window=s_fine)
        s_history = Label(lboxs, text='History', bg='#97cee3',
                          fg='white', font='BOLD', width=10, anchor='c')
        t.window_create(END, window=s_history)
        t.insert(END, "\n")

        for row in rows:
            x = row[0]
            # )#, anchor='w',text=row[0
            reg = Label(lboxs, bg='yellow', fg='black',
                        width=13, anchor='w', text=row[0])
            t.window_create(END, window=reg)
            s_name = Label(
                lboxs, text=row[1], bg='yellow', fg='black', width=22, anchor='w')
            t.window_create(END, window=s_name)
            s_mail = Label(
                lboxs, text=row[2], bg='yellow', fg='black', width=30, anchor='w')
            t.window_create(END, window=s_mail)
            s_phone = Label(
                lboxs, text=row[3], bg='yellow', fg='black', width=13, anchor='c')
            t.window_create(END, window=s_phone)
            s_batch = Label(
                lboxs, text=row[4], bg='yellow', fg='black', width=12, anchor='c')
            t.window_create(END, window=s_batch)
            s_course = Label(
                lboxs, text=row[5], bg='yellow', fg='black', width=12, anchor='c')
            t.window_create(END, window=s_course)
            s_fine = Label(
                lboxs, text=row[6], bg='yellow', fg='black', width=12, anchor='c')
            t.window_create(END, window=s_fine)
            s_history = Button(lboxs, text='History', bg='grey', fg='black', command=(
                lambda y=x: print_his(y)), width=14, anchor='c')  # (lambda y=x : print_his(y))
            t.window_create(END, window=s_history)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end

        # display = Button(labelFrame,text="CLICK TO VIEW",bg='#525b59', fg='white',command=show)
        # display.place(relx=0.35,rely=0.05,relwidth=0.3,relheight=0.1)

    # history
    def print_his(val):
        for widget in labelFrame.winfo_children():
            widget.destroy()

        cur.execute("select DISTINCT Book.Bname,Book.Author,Return_book.Approved_date,Return_book.Return_date,Book.Bid,SubBook.Sub_bid,Return_book.Borrow_ID from Book,Student,SubBook,Return_book WHERE Book.Bid=SubBook.Bid and SubBook.Sub_bid=Return_book.Sub_bid and Return_book.Student_regno='"+str(val)+"'")
        rows = list(cur.fetchall())

        back = Button(labelFrame, text="View Students", bg='#525b59',
                      fg='white', command=views)  # ,command=SearchStudents)
        back.place(relx=0.02, rely=0.02, relwidth=0.155, relheight=0.06)

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.02, rely=0.1, relwidth=0.94, relheight=0.91)

        lboxs.delete(0, 'end')
        # start
        v = Scrollbar(labelFrame, orient='vertical')
        # v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side=RIGHT, fill=Y)
        h = Scrollbar(labelFrame, orient='horizontal')
        # h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side=BOTTOM, fill=X)
        t = Text(lboxs, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end

        reg = Label(lboxs, text='Book Name', bg='#97cee3',
                    fg='white', width=30, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_name = Label(lboxs, text='Author Name', bg='#97cee3',
                       fg='white', width=15, font='BOLD', anchor='w')
        t.window_create(END, window=s_name)
        s_mail = Label(lboxs, text='Approved Date', bg='#97cee3',
                       fg='white', width=15, font='BOLD', anchor='c')
        t.window_create(END, window=s_mail)
        s_phone = Label(lboxs, text='Return Date', bg='#97cee3',
                        fg='white', width=15, font='BOLD', anchor='c')
        t.window_create(END, window=s_phone)
        s_batch = Label(lboxs, text='Book ID', bg='#97cee3',
                        fg='white', font='BOLD', width=10, anchor='c')
        t.window_create(END, window=s_batch)
        s_course = Label(lboxs, text='Sub Book ID', bg='#97cee3',
                         fg='white', width=10, font='BOLD', anchor='c')
        t.window_create(END, window=s_course)
        s_fine = Label(lboxs, text='Borrow ID', bg='#97cee3',
                       fg='white', width=10, font='BOLD', anchor='c')
        t.window_create(END, window=s_fine)
        t.insert(END, "\n")

        for row in rows:
            # x=row[0]
            # )#, anchor='w',text=row[0
            reg = Label(lboxs, bg='yellow', fg='black',
                        width=38, anchor='w', text=row[0])
            t.window_create(END, window=reg)
            s_name = Label(
                lboxs, text=row[1], bg='yellow', fg='black', width=22, anchor='w')
            t.window_create(END, window=s_name)
            s_mail = Label(
                lboxs, text=row[2], bg='yellow', fg='black', width=22, anchor='w')
            t.window_create(END, window=s_mail)
            s_phone = Label(
                lboxs, text=row[3], bg='yellow', fg='black', width=14, anchor='w')
            t.window_create(END, window=s_phone)
            s_batch = Label(
                lboxs, text=row[4], bg='yellow', fg='black', width=13, anchor='c')
            t.window_create(END, window=s_batch)
            s_course = Label(
                lboxs, text=row[5], bg='yellow', fg='black', width=13, anchor='c')
            t.window_create(END, window=s_course)
            s_fine = Label(
                lboxs, text=row[6], bg='yellow', fg='black', width=13, anchor='c')
            t.window_create(END, window=s_fine)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)

    # Deleting Student from the Database

    def deletes():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # Verufy and delete
        def del_stu():
            delst = str(dusername.get())
            if(delst == ''):
                messagebox.showinfo(
                    "Can't Delete", "Enter Student's Registration Number!")
            cur.execute("DELETE FROM Student WHERE Regno='" + delst + "'")
            con.commit()
            dusername.delete(0, 'end')
            messagebox.showinfo("Student Deleted",
                                "Student is Deleted successfully!")

        details = Label(labelFrame, text="Enter Details:", bg='white', fg='black', font='BOLD').place(
            relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        username = Label(labelFrame, text="Registration ID", bg='black', fg='white').place(
            relx=0.1, rely=0.28, relwidth=0.25, relheight=0.08)
        dusername = Entry(labelFrame, bg='#cecece', fg='black')
        dusername.place(relx=0.5, rely=0.28, relwidth=0.3, relheight=0.08)
        delete = Button(labelFrame, text='Delete', bg='#7d7d7d', fg='black', command=del_stu).place(
            relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

    # Update student details
    def updates():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        def up_stu():
            regi = str(st_reg.get())
            for widget in labelFrame.winfo_children():
                widget.destroy()

            cur.execute("select * from student where Regno='" + regi + "'")
            rows = list(cur.fetchall())

            def update_stu():
                fname = str(fullname1.get())
                fine = str(fine1.get())
                mail = str(email1.get())
                passwrd = str(password1.get())
                cont = str(contact1.get())
                dob = str(dob1.get())
                batch = str(batch1.get())
                course = str(course1.get())
                rest = 'no'
                if(res.get() == 1):
                    rest = 'yes'
                bir = dob.split('/')
                dob = ''
                if len(bir[2]) == 4:
                    dob = bir[2]+'-'+bir[1]+'-'+bir[0]
                else:
                    dob = '20'+bir[2]+'-'+bir[1]+'-'+bir[0]

                if(fname == '' or fine == "" or mail == "" or cont == None or dob == None or batch == "" or course == "" or passwrd == "") != False:
                    messagebox.showinfo(
                        "Can't ADD", "All feilds are required!")
                elif(mail.endswith('@iiitkottayam.ac.in')) != True:
                    messagebox.showinfo(
                        "Invalid Email", "Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
                elif(cont.isnumeric() and len(cont) == 10) != True:
                    messagebox.showinfo(
                        "Invalid Contact Number", "Enter a valid Contact Number(Length 10)!")
                elif (batch.isnumeric()) != True:
                    messagebox.showinfo(
                        "Invalid Batch", "Batch should be number and in format '20XX' !")
                else:
                    try:
                        # addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Stream_id, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        # add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                        # cur.execute(addformula, add_student)
                        cur.execute("UPDATE Student SET Sname='" + fname + "',Password='" + passwrd + "',Phone='" + cont + "',Email='" + mail + "',Batch='" +
                                    batch + "',DOB='" + dob + "',Fine='" + fine + "',Course='" + course + "',is_restricted='" + rest + "' WHERE Regno='" + regi + "'")
                        con.commit()
                        fullname1.delete(0, 'end')
                        fine1.delete(0, 'end')
                        email1.delete(0, 'end')
                        password1.delete(0, 'end')
                        contact1.delete(0, 'end')
                        dob1.delete(0, 'end')
                        batch1.delete(0, 'end')
                        course1.delete(0, 'end')
                        messagebox.showinfo(
                            "Student Updated", "Student Details are updated successfully!")
                        updates()
                    except:
                        messagebox.showinfo(
                            "Can't Update Student", "Oops!!\nSomething went wrong!!")

            details = Label(labelFrame, text="Enter Details to Update:", bg='white', fg='black', font='BOLD').place(
                relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
            fullname = Label(labelFrame, text="Full name", bg='black', fg='white').place(
                relx=0.1, rely=0.18, relwidth=0.25, relheight=0.07)
            fine = Label(labelFrame, text="Fine", bg='black', fg='white').place(
                relx=0.1, rely=0.27, relwidth=0.25, relheight=0.07)
            email = Label(labelFrame, text="Email Id", bg='black', fg='white').place(
                relx=0.1, rely=0.36, relwidth=0.25, relheight=0.07)
            password = Label(labelFrame, text="Password", bg='black', fg='white').place(
                relx=0.1, rely=0.45, relwidth=0.25, relheight=0.07)
            contact = Label(labelFrame, text="Contact no.", bg='black', fg='white').place(
                relx=0.1, rely=0.54, relwidth=0.25, relheight=0.07)
            dob = Label(labelFrame, text="Date Of Birth", bg='black', fg='white').place(
                relx=0.1, rely=0.63, relwidth=0.25, relheight=0.07)
            batch = Label(labelFrame, text="Batch", bg='black', fg='white').place(
                relx=0.1, rely=0.72, relwidth=0.25, relheight=0.07)
            course = Label(labelFrame, text="Course", bg='black', fg='white').place(
                relx=0.1, rely=0.81, relwidth=0.25, relheight=0.07)
            restrict = Label(labelFrame, text="Is Restricted?", bg='black', fg='white').place(
                relx=0.1, rely=0.90, relwidth=0.25, relheight=0.07)

            res = IntVar()
            restricted = rows[0][9].lower()
            if restricted == 'no':
                res.set(2)
            else:
                res.set(1)

            st_birth = str(rows[0][6])
            stu_bir = st_birth.split('-')
            st_birth = ''
            st_birth = stu_bir[2]+'/'+stu_bir[1]+'/'+stu_bir[0]

            fullname1 = Entry(labelFrame, bg='#cecece', fg='black')
            fullname1.insert(0, str(rows[0][0]))
            fullname1.place(relx=0.5, rely=0.18, relwidth=0.3, relheight=0.06)
            fine1 = Entry(labelFrame, bg='#cecece', fg='black')
            fine1.insert(0, str(rows[0][7]))
            fine1.place(relx=0.5, rely=0.27, relwidth=0.3, relheight=0.06)
            email1 = Entry(labelFrame, bg='#cecece', fg='black')
            email1.insert(0, str(rows[0][4]))
            email1.place(relx=0.5, rely=0.36, relwidth=0.3, relheight=0.06)
            password1 = Entry(labelFrame, bg='#cecece', fg='black')
            password1.insert(0, str(rows[0][2]))
            password1.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.06)
            contact1 = Entry(labelFrame, bg='#cecece', fg='black')
            contact1.insert(0, str(rows[0][3]))
            contact1.place(relx=0.5, rely=0.54, relwidth=0.3, relheight=0.06)
            dob1 = DateEntry(
                labelFrame, date_pattern='dd/mm/yyyy', bg='#cecece', fg='black')
            dob1.delete(0, 'end')
            dob1.insert(0, st_birth)
            dob1.place(relx=0.5, rely=0.63, relwidth=0.15, relheight=0.06)
            batch1 = Entry(labelFrame, bg='#cecece', fg='black')
            batch1.insert(0, str(rows[0][5]))
            batch1.place(relx=0.5, rely=0.72, relwidth=0.3, relheight=0.06)
            course1 = Entry(labelFrame, bg='#cecece', fg='black')
            course1.insert(0, str(rows[0][8]))
            course1.place(relx=0.5, rely=0.81, relwidth=0.3, relheight=0.06)
            re1 = Radiobutton(labelFrame, text="Yes", bg='#cecece', fg='black')
            re1.place(relx=0.5, rely=0.90, relwidth=0.12, relheight=0.06)
            re1.config(variable=res, val=1)
            re2 = Radiobutton(labelFrame, text="No", bg='#cecece', fg='black')
            re2.place(relx=0.65, rely=0.90, relwidth=0.12, relheight=0.06)
            re2.config(variable=res, val=2)

            update = Button(labelFrame, text='Update', bg='#7d7d7d', fg='black', command=update_stu).place(
                relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

        details = Label(labelFrame, text="Update Student Details:", bg='white', fg='black',
                        font='BOLD').place(relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        user = Label(labelFrame, text="Registration Number", bg='black', fg='white').place(
            relx=0.1, rely=0.28, relwidth=0.25, relheight=0.08)
        st_reg = Entry(labelFrame, bg='#cecece', fg='black')
        st_reg.place(relx=0.5, rely=0.28, relwidth=0.3, relheight=0.08)
        delete = Button(labelFrame, text='Proceed', bg='#7d7d7d', fg='black', command=up_stu).place(
            relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

    # update FUNCTION

    def up_stu(regi):
        # regi=str(st_reg.get())
        for widget in labelFrame.winfo_children():
            widget.destroy()

        cur.execute("select * from student where Regno='" + regi + "'")
        rows = list(cur.fetchall())

        def update_stu():
            fname = str(fullname1.get())
            fine = str(fine1.get())
            mail = str(email1.get())
            passwrd = str(password1.get())
            cont = str(contact1.get())
            dob = str(dob1.get())
            batch = str(batch1.get())
            course = str(course1.get())
            rest = 'no'
            if(res.get() == 1):
                rest = 'yes'
            bir = dob.split('/')
            dob = ''
            if len(bir[2]) == 4:
                dob = bir[2]+'-'+bir[1]+'-'+bir[0]
            else:
                dob = '20'+bir[2]+'-'+bir[1]+'-'+bir[0]

            if(fname == '' or fine == "" or mail == "" or cont == None or dob == None or batch == "" or course == "" or passwrd == "") != False:
                messagebox.showinfo("Can't ADD", "All feilds are required!")
            elif(mail.endswith('@iiitkottayam.ac.in')) != True:
                messagebox.showinfo(
                    "Invalid Email", "Enter a valid Email ID!\nEmail ID should be of domain name '@iiitkottayam.ac.in'")
            elif(cont.isnumeric() and len(cont) == 10) != True:
                messagebox.showinfo("Invalid Contact Number",
                                    "Enter a valid Contact Number(Length 10)!")
            elif (batch.isnumeric()) != True:
                messagebox.showinfo(
                    "Invalid Batch", "Batch should be number and in format '20XX' !")
            else:
                try:
                    # addformula="INSERT INTO Student (Sname, Regno, Password, Phone, Email, Batch, DOB, Fine, Stream_id, is_restricted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    # add_student=(fname,usern,passwrd,cont,mail,batch,dob,fine,course,rest)
                    # cur.execute(addformula, add_student)
                    cur.execute("UPDATE Student SET Sname='" + fname + "',Password='" + passwrd + "',Phone='" + cont + "',Email='" + mail + "',Batch='" +
                                batch + "',DOB='" + dob + "',Fine='" + fine + "',Course='" + course + "',is_restricted='" + rest + "' WHERE Regno='" + regi + "'")
                    con.commit()
                    fullname1.delete(0, 'end')
                    fine1.delete(0, 'end')
                    email1.delete(0, 'end')
                    password1.delete(0, 'end')
                    contact1.delete(0, 'end')
                    dob1.delete(0, 'end')
                    batch1.delete(0, 'end')
                    course1.delete(0, 'end')
                    messagebox.showinfo(
                        "Student Updated", "Student Details are updated successfully!")
                    updates()
                except:
                    messagebox.showinfo(
                        "Can't Update Student", "Oops!!\nSomething went wrong!!")

        details = Label(labelFrame, text="Enter Details to Update:", bg='white', fg='black',
                        font='BOLD').place(relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        fullname = Label(labelFrame, text="Full name", bg='black', fg='white').place(
            relx=0.1, rely=0.18, relwidth=0.25, relheight=0.07)
        fine = Label(labelFrame, text="Fine", bg='black', fg='white').place(
            relx=0.1, rely=0.27, relwidth=0.25, relheight=0.07)
        email = Label(labelFrame, text="Email Id", bg='black', fg='white').place(
            relx=0.1, rely=0.36, relwidth=0.25, relheight=0.07)
        password = Label(labelFrame, text="Password", bg='black', fg='white').place(
            relx=0.1, rely=0.45, relwidth=0.25, relheight=0.07)
        contact = Label(labelFrame, text="Contact no.", bg='black', fg='white').place(
            relx=0.1, rely=0.54, relwidth=0.25, relheight=0.07)
        dob = Label(labelFrame, text="Date Of Birth", bg='black', fg='white').place(
            relx=0.1, rely=0.63, relwidth=0.25, relheight=0.07)
        batch = Label(labelFrame, text="Batch", bg='black', fg='white').place(
            relx=0.1, rely=0.72, relwidth=0.25, relheight=0.07)
        course = Label(labelFrame, text="Course", bg='black', fg='white').place(
            relx=0.1, rely=0.81, relwidth=0.25, relheight=0.07)
        restrict = Label(labelFrame, text="Is Restricted?", bg='black', fg='white').place(
            relx=0.1, rely=0.90, relwidth=0.25, relheight=0.07)

        res = IntVar()
        restricted = rows[0][9].lower()
        if restricted == 'no':
            res.set(2)
        else:
            res.set(1)

        st_birth = str(rows[0][6])
        stu_bir = st_birth.split('-')
        st_birth = ''
        st_birth = stu_bir[2]+'/'+stu_bir[1]+'/'+stu_bir[0]

        fullname1 = Entry(labelFrame, bg='#cecece', fg='black')
        fullname1.insert(0, str(rows[0][0]))
        fullname1.place(relx=0.5, rely=0.18, relwidth=0.3, relheight=0.06)
        fine1 = Entry(labelFrame, bg='#cecece', fg='black')
        fine1.insert(0, str(rows[0][7]))
        fine1.place(relx=0.5, rely=0.27, relwidth=0.3, relheight=0.06)
        email1 = Entry(labelFrame, bg='#cecece', fg='black')
        email1.insert(0, str(rows[0][4]))
        email1.place(relx=0.5, rely=0.36, relwidth=0.3, relheight=0.06)
        password1 = Entry(labelFrame, bg='#cecece', fg='black')
        password1.insert(0, str(rows[0][2]))
        password1.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.06)
        contact1 = Entry(labelFrame, bg='#cecece', fg='black')
        contact1.insert(0, str(rows[0][3]))
        contact1.place(relx=0.5, rely=0.54, relwidth=0.3, relheight=0.06)
        dob1 = DateEntry(labelFrame, date_pattern='dd/mm/yyyy',
                         bg='#cecece', fg='black')
        dob1.delete(0, 'end')
        dob1.insert(0, st_birth)
        dob1.place(relx=0.5, rely=0.63, relwidth=0.15, relheight=0.06)
        batch1 = Entry(labelFrame, bg='#cecece', fg='black')
        batch1.insert(0, str(rows[0][5]))
        batch1.place(relx=0.5, rely=0.72, relwidth=0.3, relheight=0.06)
        course1 = Entry(labelFrame, bg='#cecece', fg='black')
        course1.insert(0, str(rows[0][8]))
        course1.place(relx=0.5, rely=0.81, relwidth=0.3, relheight=0.06)
        re1 = Radiobutton(labelFrame, text="Yes", bg='#cecece', fg='black')
        re1.place(relx=0.5, rely=0.90, relwidth=0.12, relheight=0.06)
        re1.config(variable=res, val=1)
        re2 = Radiobutton(labelFrame, text="No", bg='#cecece', fg='black')
        re2.place(relx=0.65, rely=0.90, relwidth=0.12, relheight=0.06)
        re2.config(variable=res, val=2)

        update = Button(labelFrame, text='Update', bg='#7d7d7d', fg='black', command=update_stu).place(
            relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

    # restrict student

    def restricts():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        def rest_stu():
            st_res = str(st_rest.get())
            y = 'Yes'
            cur.execute("UPDATE Student SET is_restricted='" +
                        'Yes' + "' WHERE Regno='" + st_res + "'")
            con.commit()
            st_rest.delete(0, 'end')
            messagebox.showinfo("Student Restricted",
                                "Student is Restricted successfully!")

        details = Label(labelFrame, text="Restrict Student:", bg='white', fg='black', font='BOLD').place(
            relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        st_res = Label(labelFrame, text="Registration Number", bg='black', fg='white').place(
            relx=0.1, rely=0.28, relwidth=0.25, relheight=0.08)
        st_rest = Entry(labelFrame, bg='#cecece', fg='black')
        st_rest.place(relx=0.5, rely=0.28, relwidth=0.3, relheight=0.08)
        delete = Button(labelFrame, text='Restrict', bg='#7d7d7d', fg='black', command=rest_stu).place(
            relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

    # pending books at student

    def pending_stu(reg):
        x = reg
        for widget in labelFrame.winfo_children():
            widget.destroy()

        ls = Listbox(labelFrame, bg="black", relief="sunken",
                     font=("courier", 15), fg="white")
        ls.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

        # def show():
        ls.delete(0, 'end')
        # start
        h = Scrollbar(ls, orient='horizontal')
        h.pack(side=BOTTOM, fill=X)
        v = Scrollbar(ls)
        v.pack(side=RIGHT, fill=Y)
        t = Text(ls, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end
        cur.execute("select student.Sname,student.Regno,book.bname,SubBook.Sub_bid, Borrow.Approved_date,Borrow.borrow_id From student,Book,SubBook,Borrow where Book.Bid = SubBook.Bid and Student.Regno = Borrow.student_regno and SubBook.Sub_bid = Borrow.Sub_bid and Student.Regno='" + x + "' ")
        rows = list(cur.fetchall())
        reg = Label(ls, text='Reg.No.', bg='#97cee3', fg='white',
                    width=10, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_name = Label(ls, text='Name', bg='#97cee3', fg='white',
                       width=17, font='BOLD', anchor='w')
        t.window_create(END, window=s_name)
        s_bookname = Label(ls, text='book name', bg='#97cee3',
                           fg='white', width=25, font='BOLD', anchor='w')
        t.window_create(END, window=s_bookname)
        s_sub_id = Label(ls, text='sub bookid', bg='#97cee3',
                         fg='white', width=13, font='BOLD', anchor='c')
        t.window_create(END, window=s_sub_id)
        s_borrow = Label(ls, text='borrow date', bg='#97cee3',
                         fg='white', font='BOLD', width=13, anchor='c')
        t.window_create(END, window=s_borrow)
        s_borrowid = Label(ls, text='borrow id', bg='#97cee3',
                           fg='white', width=13, font='BOLD', anchor='c')
        t.window_create(END, window=s_borrowid)
        s_receive = Label(ls, text='Receive book', bg='#97cee3',
                          fg='white', font='BOLD', width=10, anchor='c')
        t.window_create(END, window=s_receive)

        t.insert(END, "\n")
        for row in rows:
            val = row
            reg = Label(ls, text=row[1], bg='yellow',
                        fg='black', width=13, anchor='w')
            t.window_create(END, window=reg)
            s_name = Label(ls, text=row[0], bg='yellow',
                           fg='black', width=22, anchor='w')
            t.window_create(END, window=s_name)
            s_bookid = Label(
                ls, text=row[2], bg='yellow', fg='black', width=35, anchor='w')
            t.window_create(END, window=s_bookid)
            s_sub_id = Label(
                ls, text=row[3], bg='yellow', fg='black', width=15, anchor='c')
            t.window_create(END, window=s_sub_id)
            s_borrow = Label(
                ls, text=row[4], bg='yellow', fg='black', width=16, anchor='c')
            t.window_create(END, window=s_borrow)
            s_borrowid = Label(
                ls, text=row[5], bg='yellow', fg='black', width=14, anchor='c')
            t.window_create(END, window=s_borrowid)
            s_receive = Button(ls, text='Recieve Book', bg='grey', fg='black', command=(
                lambda x=val: b_receive(x)), width=14, anchor='c')
            t.window_create(END, window=s_receive)
            t.insert(END, "\n")

        # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end

    # Manage Students

    lb1 = Menu(menubar, tearoff=0, bg='#525b59', fg='white')
    menubar.add_cascade(label='Manage Students', menu=lb1)
    lb1.add_command(label='Add Student', command=adds)
    lb1.add_command(label='Update Details', command=updates)
    lb1.add_command(label='View Students', command=views)
    lb1.add_separator()
    lb1.add_command(label='Delete Student', command=deletes)
    lb1.add_command(label='Restrict Student', command=restricts)

    # FUNCTION TO VIEW LIBRARY

    def view():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="black", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.02, rely=0.04, relwidth=0.94, relheight=0.91)

        # print_his()
        def print_his():
            reg_no = str(reg.get())
            print(reg_no)

        # def show():
        lboxs.delete(0, 'end')
        # start
        v = Scrollbar(labelFrame, orient='vertical')
        # v.place(relx=0.90,rely=0.04,relheight=0.91,relwidth=0.015)
        v.pack(side=RIGHT, fill=Y)
        h = Scrollbar(labelFrame, orient='horizontal')
        # h.place(relx=0.04,rely=0.90,relwidth=0.91,relheight=0.015)
        h.pack(side=BOTTOM, fill=X)
        t = Text(lboxs, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end
        cur.execute(
            "select Bid, Bname, Author, Subject_name, CName, Rating from book order by Bid")
        rows = list(cur.fetchall())

        b_id = Label(lboxs, text='Book ID', bg='#97cee3',
                     fg='white', width=10, font='BOLD', anchor='w')
        t.window_create(END, window=b_id)
        b_name = Label(lboxs, text='Book Name', bg='#97cee3',
                       fg='white', width=25, font='BOLD', anchor='w')
        t.window_create(END, window=b_name)
        author = Label(lboxs, text='Author', bg='#97cee3',
                       fg='white', width=20, font='BOLD', anchor='c')
        t.window_create(END, window=author)
        b_numb = Label(lboxs, text='Number of Books', bg='#97cee3',
                       fg='white', width=15, font='BOLD', anchor='c')
        t.window_create(END, window=b_numb)
        b_course = Label(lboxs, text='Course', bg='#97cee3',
                         fg='white', font='BOLD', width=12, anchor='c')
        t.window_create(END, window=b_course)
        b_subject = Label(lboxs, text='Subject', bg='#97cee3',
                          fg='white', width=12, font='BOLD', anchor='c')
        t.window_create(END, window=b_subject)
        b_rating = Label(lboxs, text='Rating', bg='#97cee3',
                         fg='white', width=11, font='BOLD', anchor='c')
        t.window_create(END, window=b_rating)
        t.insert(END, "\n")

        for row in rows:
            x = str(row[0])
            count_val = cur.execute(
                "select count(*) from subbook where Bid='" + x + "'")
            count_list = list(cur.fetchall())

            reg = Label(lboxs, bg='#c9ffa0', fg='black', width=13,
                        anchor='w', text=row[0])  # )#, anchor='w',text=row[0]
            # reg.delete(0,'end')
            # reg.insert(0,row[0])
            # reg.configure(state='readonly')
            t.window_create(END, window=reg)
            s_name = Label(
                lboxs, text=row[1], bg='#c9ffa0', fg='black', width=42, anchor='w')
            t.window_create(END, window=s_name)
            s_mail = Label(
                lboxs, text=row[2], bg='#c9ffa0', fg='black', width=23, anchor='w')
            t.window_create(END, window=s_mail)
            s_phone = Label(
                lboxs, text=count_list[0], bg='#c9ffa0', fg='black', width=10, anchor='w')
            t.window_create(END, window=s_phone)
            s_batch = Label(
                lboxs, text=row[3], bg='#c9ffa0', fg='black', width=17, anchor='c')
            t.window_create(END, window=s_batch)
            s_course = Label(
                lboxs, text=row[4], bg='#c9ffa0', fg='black', width=18, anchor='c')
            t.window_create(END, window=s_course)
            s_fine = Label(
                lboxs, text=row[5], bg='#c9ffa0', fg='black', width=12, anchor='c')
            t.window_create(END, window=s_fine)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end

    # Adding Books

    def add_book():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="#cecece", relief="sunken",
                        font=("courier", 15), fg="black")
        lboxs.place(relx=0.03, rely=0.59, relwidth=0.94, relheight=0.37)

        # print_his()
        '''def print_his():
            reg_no=str(reg.get())
            print(reg_no)'''

        # def show():
        # lboxs.delete(0,'end')

        def check():
            for widget in lboxs.winfo_children():
                widget.destroy()
            # def show():
            # lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
            # lboxs.place(relx=0.03, rely=0.59,relwidth=0.94,relheight=0.37)

            # lboxs.delete(0,'end')
            # start
            h = Scrollbar(lboxs, orient='horizontal')
            h.pack(side=BOTTOM, fill=X)
            v = Scrollbar(lboxs)
            v.pack(side=RIGHT, fill=Y)
            t = Text(lboxs, width=30, height=30, wrap=NONE,
                     xscrollcommand=h.set, yscrollcommand=v.set)

            Subject_name = str(e_subject.get())
            CName = str(e_category.get())
            # Bid = str(e_bid.get())
            # Bname = str(e_bname.get())
            # Author = str(e_author.get())
            Rating = '0.0'
            Thumbnail = None

            select_state = "select Book.Bid, Book.Bname, Book.Author from book where Subject_name = '" + \
                Subject_name + "' and CName = '" + CName + "' ORDER BY Bid"
            cur.execute(select_state)
            rows = list(cur.fetchall())

            reg = Label(lboxs, text='Book ID', bg='#97cee3', fg='white', width=16,
                        font='BOLD', anchor='w')  # , state='disabled')#, anchor='w')
            t.window_create(END, window=reg)
            s_name = Label(lboxs, text='Book Name', bg='#97cee3',
                           fg='white', width=32, font='BOLD', anchor='w')
            t.window_create(END, window=s_name)
            s_author = Label(lboxs, text='Author', bg='#97cee3',
                             fg='white', width=22, font='BOLD', anchor='w')
            t.window_create(END, window=s_author)
            s_num = Label(lboxs, text='Number of books', bg='#97cee3',
                          fg='white', width=16, font='BOLD', anchor='c')
            t.window_create(END, window=s_num)
            s_history = Label(lboxs, text='ADD', bg='#97cee3',
                              fg='white', font='BOLD', width=18, anchor='c')
            t.window_create(END, window=s_history)
            t.insert(END, "\n")

            def add_old(val):
                cur.execute(
                    "insert into subbook (Bid) values('" + str(val) + "')")
                cur.execute("commit")
                check()

            for row in rows:
                lboxs.delete(0, 'end')

                x = str(row[0])
                count_val = cur.execute(
                    "select count(*) from subbook where Bid='" + x + "'")
                count_list = list(cur.fetchall())

                bid = Label(lboxs, text=row[0], bg='yellow',
                            fg='black', width=20, anchor='w')
                t.window_create(END, window=bid)
                bname = Label(
                    lboxs, text=row[1], bg='yellow', fg='black', width=40, anchor='w')
                t.window_create(END, window=bname)
                author = Label(
                    lboxs, text=row[2], bg='yellow', fg='black', width=30, anchor='w')
                t.window_create(END, window=author)
                numb = Label(
                    lboxs, text=count_list[0], bg='yellow', fg='black', width=25, anchor='c')
                t.window_create(END, window=numb)
                ADD = Button(lboxs, text='ADD', bg='grey', fg='black', command=(
                    lambda x=row[0]: add_old(x)), width=18, anchor='c')
                t.window_create(END, window=ADD)
                t.insert(END, "\n")
                # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                # lboxs.insert(lboxs.size()+1, insertdata)
                # t.insert(END,insertdata)
            # start
            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)
            # end

        Subject_name = Label(labelFrame, text="SUBJECT",
                             bg="black", fg="white", anchor='w')
        Subject_name.place(relx=0.15, rely=0.12, relwidth=0.2, relheight=0.06)

        CName = Label(labelFrame, text="CATEGORY",
                      bg="black", fg="white", anchor='w')
        CName.place(relx=0.15, rely=0.20, relwidth=0.2, relheight=0.06)

        # Bid = Label(labelFrame,text="BOOK ID",bg="black",fg="white",anchor='w')
        # Bid.place(relx=0.15,rely=0.28,relwidth=0.2,relheight=0.06)

        Bname = Label(labelFrame, text="BOOK_NAME",
                      bg="black", fg="white", anchor='w')
        Bname.place(relx=0.15, rely=0.36, relwidth=0.2, relheight=0.06)

        Author = Label(labelFrame, text="AUTHOR",
                       bg="black", fg="white", anchor='w')
        Author.place(relx=0.15, rely=0.44, relwidth=0.2, relheight=0.06)

        e_subject = Entry(labelFrame, bg='#cecece', fg='black')
        e_subject.place(relx=0.48, rely=0.12, relwidth=0.3, relheight=0.06)

        e_category = Entry(labelFrame, bg='#cecece', fg='black')
        e_category.place(relx=0.48, rely=0.20, relwidth=0.3, relheight=0.06)

        # e_bid = Entry(labelFrame)
        # e_bid.place(relx=0.48,rely=0.28,relwidth=0.3,relheight=0.06)

        e_bname = Entry(labelFrame, bg='#cecece', fg='black')
        e_bname.place(relx=0.48, rely=0.36, relwidth=0.3, relheight=0.06)

        e_author = Entry(labelFrame, bg='#cecece', fg='black')
        e_author.place(relx=0.48, rely=0.44, relwidth=0.3, relheight=0.06)

        
        

        def add_new():
            
            def convertToBinaryData(filename):
                # Convert digital data to binary format
                with open(filename, 'rb') as file:
                    binaryData = file.read()
                return binaryData
        
            filename = askopenfilename()
            
            Thumbnail = convertToBinaryData(filename)
            
            Subject_name = e_subject.get()
            CName = e_category.get()
            # Bid = e_bid.get()
            Bname = e_bname.get()
            Author = e_author.get()
            Rating = '0.0'
            # Thumbnail = 'None'
            if Subject_name == '' or CName == '' or Bname == '' or Author == '':  # or Bid==''
                messagebox.showinfo(
                    "Insert Status", "All fields are required!")
            else:
                try:
                    cur.execute(
                        "insert into Subject values('" + Subject_name + "')")
                    cur.execute("insert into Category values('" +
                                CName + "','" + Subject_name + "')")
                except(mysql.connector.errors.IntegrityError):
                    pass

                add_new_book_formula = "INSERT INTO book (Bname, Author, Rating, Subject_name, CName, Thumbnail) VALUES (%s, %s, %s, %s, %s, %s)"
                add_book = (Bname, Author, Rating,
                            Subject_name, CName, Thumbnail)

                cur.execute(add_new_book_formula, add_book)
                cur.execute("commit")

                # e_bid.delete(0, 'end')
                e_bname.delete(0, 'end')
                e_author.delete(0, 'end')

                messagebox.showinfo(
                    "Insert Status", "Successfully inserted into database")

                check()

        Check = Button(labelFrame, text="Check", fg="black",
                       bg="#7d7d7d", command=check)
        Check.place(relx=0.80, rely=0.20, relwidth=0.14, relheight=0.06)

        ADD = Button(labelFrame, text="ADD NEW BOOK",
                     fg="black", bg="#7d7d7d", command=add_new)
        ADD.place(relx=0.80, rely=0.44, relwidth=0.14, relheight=0.06)
    # FUNCTION FOR DELETING BOOK

    def delete():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="#cecece", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.03, rely=0.59, relwidth=0.94, relheight=0.37)

        def check():
            for widget in lboxs.winfo_children():
                widget.destroy()
            # lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
            # lboxs.place(relx=0.03, rely=0.59,relwidth=0.94,relheight=0.37)

            # def show():
            lboxs.delete(0, 'end')
            # start
            h = Scrollbar(lboxs, orient='horizontal')
            h.pack(side=BOTTOM, fill=X)
            v = Scrollbar(lboxs)
            v.pack(side=RIGHT, fill=Y)
            t = Text(lboxs, width=30, height=30, wrap=NONE,
                     xscrollcommand=h.set, yscrollcommand=v.set)

            Subject_name = str(e_subject.get())
            CName = str(e_category.get())
            Bid = e_bid.get()

            select_state = "select Book.Bid, Book.Bname, Book.Author, Book.Rating from book where Subject_name = '" + \
                Subject_name + "' and CName = '" + CName + "' ORDER BY Bid"
            cur.execute(select_state)
            rows = list(cur.fetchall())

            reg = Label(lboxs, text='Book ID', bg='#97cee3', fg='white', width=16,
                        font='BOLD', anchor='w')  # , state='disabled')#, anchor='w')
            t.window_create(END, window=reg)
            s_name = Label(lboxs, text='Book Name', bg='#97cee3',
                           fg='white', width=32, font='BOLD', anchor='w')
            t.window_create(END, window=s_name)
            s_author = Label(lboxs, text='Author', bg='#97cee3',
                             fg='white', width=22, font='BOLD', anchor='w')
            t.window_create(END, window=s_author)
            s_num = Label(lboxs, text='Number of books', bg='#97cee3',
                          fg='white', width=16, font='BOLD', anchor='c')
            t.window_create(END, window=s_num)
            s_rating = Label(lboxs, text='Rating', bg='#97cee3',
                             fg='white', width=18, font='BOLD', anchor='c')
            t.window_create(END, window=s_rating)
            t.insert(END, "\n")

            for row in rows:
                lboxs.delete(0, 'end')
                bid = Label(lboxs, text=row[0], bg='yellow',
                            fg='black', width=20, anchor='w')
                t.window_create(END, window=bid)
                bname = Label(
                    lboxs, text=row[1], bg='yellow', fg='black', width=40, anchor='w')
                t.window_create(END, window=bname)
                author = Label(
                    lboxs, text=row[2], bg='yellow', fg='black', width=30, anchor='w')
                t.window_create(END, window=author)
                numb = Label(lboxs, text='1', bg='yellow',
                             fg='black', width=25, anchor='c')
                t.window_create(END, window=numb)
                rat = Label(lboxs, text=row[3], bg='yellow',
                            fg='black', width=19, anchor='c')
                t.window_create(END, window=rat)
                t.insert(END, "\n")

            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)

        Subject_name = Label(labelFrame, text="SUBJECT",
                             bg="black", fg="white", anchor='w')
        Subject_name.place(relx=0.15, rely=0.12, relwidth=0.2, relheight=0.06)

        CName = Label(labelFrame, text="CATEGORY",
                      bg="black", fg="white", anchor='w')
        CName.place(relx=0.15, rely=0.20, relwidth=0.2, relheight=0.06)

        Bid = Label(labelFrame, text="BOOK ID",
                    bg="black", fg="white", anchor='w')
        Bid.place(relx=0.15, rely=0.36, relwidth=0.2, relheight=0.06)

        e_subject = Entry(labelFrame, bg='#cecece', fg='black')
        e_subject.place(relx=0.48, rely=0.12, relwidth=0.3, relheight=0.06)

        e_category = Entry(labelFrame, bg='#cecece', fg='black')
        e_category.place(relx=0.48, rely=0.20, relwidth=0.3, relheight=0.06)

        e_bid = Entry(labelFrame, bg='#cecece', fg='black')
        e_bid.place(relx=0.48, rely=0.36, relwidth=0.3, relheight=0.06)

        def remove():
            Bid = e_bid.get()

            if(Bid == ""):
                messagebox.showinfo(
                    "Insert Status", "All fields are required!")
            elif(Bid.isdigit() is False):
                messagebox.showinfo(
                    "Insert Status", "BOOK ID should be an integer")
            else:
                cur.execute("delete from subbook where Bid='" + Bid + "'")
                con.commit()
                cur.execute("delete from book where Bid='" + Bid + "'")
                cur.execute("commit")
                messagebox.showinfo(
                    "Delete Status", "Successfully deleted from database")
            # e_subject.delete(0, 'end')
            # e_category.delete(0, 'end')
            e_bid.delete(0, 'end')

            check()

        Check = Button(labelFrame, text="Check", fg="black",
                       bg="#7d7d7d", command=check)
        Check.place(relx=0.80, rely=0.20, relwidth=0.14, relheight=0.06)

        DELETE = Button(labelFrame, text="DELETE BOOK",
                        fg="black", bg="#7d7d7d", command=remove)
        DELETE.place(relx=0.80, rely=0.36, relwidth=0.14, relheight=0.06)

    # Update Book Details
    def book_update():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        lboxs = Listbox(labelFrame, bg="#cecece", relief="sunken",
                        font=("courier", 15), fg="white")
        lboxs.place(relx=0.03, rely=0.55, relwidth=0.94, relheight=0.42)

        def check():
            for widget in lboxs.winfo_children():
                widget.destroy()
            # lboxs = Listbox(labelFrame, bg="black", relief="sunken",font=("courier",15),fg="white")
            # lboxs.place(relx=0.03, rely=0.55,relwidth=0.94,relheight=0.42)

            lboxs.delete(0, 'end')

            def add_old(val):
                cur.execute(
                    "insert into subbook (Bid) values('" + str(val) + "')")
                con.commit()
                check()

            # start
            h = Scrollbar(lboxs, orient='horizontal')
            h.pack(side=BOTTOM, fill=X)
            v = Scrollbar(lboxs)
            v.pack(side=RIGHT, fill=Y)
            t = Text(lboxs, width=30, height=30, wrap=NONE,
                     xscrollcommand=h.set, yscrollcommand=v.set)

            Subject_name = str(e_subject.get())
            CName = str(e_category.get())
            # Bid = str(e_bid.get())
            # Bname = str(e_bname.get())
            # Author = str(e_author.get())
            Rating = '0.0'
            Thumbnail = None

            select_state = "select Book.Bid, Book.Bname, Book.Author, book.Rating from book where Subject_name = '" + \
                Subject_name + "' and CName = '" + CName + "' ORDER BY Bid"
            cur.execute(select_state)
            rows = list(cur.fetchall())

            reg = Label(lboxs, text='Book ID', bg='#97cee3', fg='white', width=16,
                        font='BOLD', anchor='w')  # , state='disabled')#, anchor='w')
            t.window_create(END, window=reg)
            s_name = Label(lboxs, text='Book Name', bg='#97cee3',
                           fg='white', width=32, font='BOLD', anchor='w')
            t.window_create(END, window=s_name)
            s_author = Label(lboxs, text='Author', bg='#97cee3',
                             fg='white', width=16, font='BOLD', anchor='w')
            t.window_create(END, window=s_author)
            s_num = Label(lboxs, text='Number of books', bg='#97cee3',
                          fg='white', width=16, font='BOLD', anchor='c')
            t.window_create(END, window=s_num)
            s_rate = Label(lboxs, text='Rating', bg='#97cee3',
                           fg='white', width=8, font='BOLD', anchor='c')
            t.window_create(END, window=s_rate)
            s_history = Label(lboxs, text='ADD', bg='#97cee3',
                              fg='white', font='BOLD', width=16, anchor='c')
            t.window_create(END, window=s_history)
            t.insert(END, "\n")

            for row in rows:
                lboxs.delete(0, 'end')
                x = str(row[0])
                count_val = cur.execute(
                    "select count(*) from subbook where Bid='" + x + "'")
                count_list = list(cur.fetchall())
                bid = Label(lboxs, text=row[0], bg='yellow',
                            fg='black', width=20, anchor='w')
                t.window_create(END, window=bid)
                bname = Label(
                    lboxs, text=row[1], bg='yellow', fg='black', width=40, anchor='w')
                t.window_create(END, window=bname)
                author = Label(
                    lboxs, text=row[2], bg='yellow', fg='black', width=30, anchor='w')
                t.window_create(END, window=author)
                numb = Label(
                    lboxs, text=count_list[0], bg='yellow', fg='black', width=12, anchor='c')
                t.window_create(END, window=numb)
                rating = Label(
                    lboxs, text=row[3], bg='yellow', fg='black', width=13, anchor='c')
                t.window_create(END, window=rating)
                ADD = Button(lboxs, text='ADD', bg='grey', fg='black', command=(
                    lambda x=row[0]: add_old(x)), width=18, anchor='c')
                t.window_create(END, window=ADD)
                t.insert(END, "\n")
                # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
                # lboxs.insert(lboxs.size()+1, insertdata)
                # t.insert(END,insertdata)
            # start
            t.configure(state="disabled")
            t.pack(side=TOP, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)
            # end

        Subject_name = Label(labelFrame, text="SUBJECT",
                             bg="black", fg="white", anchor='w')
        Subject_name.place(relx=0.15, rely=0.06, relwidth=0.2, relheight=0.06)

        CName = Label(labelFrame, text="CATEGORY",
                      bg="black", fg="white", anchor='w')
        CName.place(relx=0.15, rely=0.14, relwidth=0.2, relheight=0.06)

        Bid = Label(labelFrame, text="BOOK ID(Not to be Updated)",
                    bg="black", fg="white", anchor='w')
        Bid.place(relx=0.15, rely=0.22, relwidth=0.2, relheight=0.06)

        Bname = Label(labelFrame, text="BOOK_NAME",
                      bg="black", fg="white", anchor='w')
        Bname.place(relx=0.15, rely=0.30, relwidth=0.2, relheight=0.06)

        Author = Label(labelFrame, text="AUTHOR",
                       bg="black", fg="white", anchor='w')
        Author.place(relx=0.15, rely=0.38, relwidth=0.2, relheight=0.06)

        Rating = Label(labelFrame, text="RATING",
                       bg="black", fg="white", anchor='w')
        Rating.place(relx=0.15, rely=0.46, relwidth=0.2, relheight=0.06)

        e_subject = Entry(labelFrame, bg='#cecece', fg='black')
        e_subject.place(relx=0.48, rely=0.06, relwidth=0.3, relheight=0.06)

        e_category = Entry(labelFrame, bg='#cecece', fg='black')
        e_category.place(relx=0.48, rely=0.14, relwidth=0.3, relheight=0.06)

        e_bid = Entry(labelFrame, bg='#cecece', fg='black')
        e_bid.place(relx=0.48, rely=0.22, relwidth=0.3, relheight=0.06)

        e_bname = Entry(labelFrame, bg='#cecece', fg='black')
        e_bname.place(relx=0.48, rely=0.30, relwidth=0.3, relheight=0.06)

        e_author = Entry(labelFrame, bg='#cecece', fg='black')
        e_author.place(relx=0.48, rely=0.38, relwidth=0.3, relheight=0.06)

        e_rating = Entry(labelFrame, bg='#cecece', fg='black')
        e_rating.place(relx=0.48, rely=0.46, relwidth=0.3, relheight=0.06)

        def b_update():
            
            def convertToBinaryData(filename):
                # Convert digital data to binary format
                with open(filename, 'rb') as file:
                    binaryData = file.read()
                return binaryData
        
            filename = askopenfilename()
            
            Thumbnail = convertToBinaryData(filename)
            
            Subject_name = e_subject.get()
            CName = e_category.get()
            Bid = e_bid.get()
            Bname = e_bname.get()
            Author = e_author.get()
            Rating = e_rating.get()
            # Thumbnail = 'None'
            if(Subject_name == '' or Bid == '' or CName == '' or Bname == '' or Author == '' or Rating == ''):  # or Bid==''
                messagebox.showinfo(
                    "Update Status", "All fields are required!")
            else:
                try:
                    cur.execute(
                        "insert into Subject values('" + Subject_name + "')")
                    cur.execute("insert into Category values('" +
                                CName + "','" + Subject_name + "')")
                except(mysql.connector.errors.IntegrityError):
                    pass

                cur.execute("UPDATE book SET Bname='" + Bname + "',Author='" + Author + "',Rating='" + Rating + "',Subject_name='" +
                            Subject_name + "',CName='" + CName + "',Thumbnail='" + "None" + "' WHERE Bid='" + str(Bid) + "'")
                
                new_formula_for_thumbnail = "UPDATE book SET Thumbnail = %s"
                
                new_data_for_thumbnail = (Thumbnail, )
                
                cur.execute(new_formula_for_thumbnail,new_data_for_thumbnail)
                cur.execute("commit")
                
                
                con.commit()

                # add_new_book_formula="INSERT INTO book (Bname, Author, Rating, Subject_name, CName, Thumbnail) VALUES (%s, %s, %s, %s, %s, %s)"
                # add_book=(Bname,Author,Rating,Subject_name,CName,Thumbnail)

                # cur.execute(add_new_book_formula,add_book)
                # cur.execute("commit")

                e_bid.delete(0, 'end')
                e_bname.delete(0, 'end')
                e_author.delete(0, 'end')
                e_rating.delete(0, 'end')

                messagebox.showinfo(
                    "Update Status", "Successfully Updated into database")

                check()

        Check = Button(labelFrame, text="Check", fg="black",
                       bg="#7d7d7d", command=check)
        Check.place(relx=0.80, rely=0.14, relwidth=0.14, relheight=0.06)

        ADD = Button(labelFrame, text="UPDATE BOOK",
                     fg="black", bg="#7d7d7d", command=b_update)
        ADD.place(relx=0.80, rely=0.46, relwidth=0.14, relheight=0.06)

    # book status

    def b_status(bid):
        x = bid
        for widget in labelFrame.winfo_children():
            widget.destroy()

        cur.execute(
            "select Bid, Bname, Author, Subject_name, CName, Rating from book where Bid='" + str(x) + "'")
        rows = list(cur.fetchall())

        details = Label(labelFrame, text="Book Status", bg='white', fg='black', font='BOLD').place(
            relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        fullname = Label(labelFrame, text="Book ID", bg='black', fg='white').place(
            relx=0.1, rely=0.18, relwidth=0.25, relheight=0.07)
        username = Label(labelFrame, text="Book Name", bg='black', fg='white').place(
            relx=0.1, rely=0.27, relwidth=0.25, relheight=0.07)
        email = Label(labelFrame, text="Author", bg='black', fg='white').place(
            relx=0.1, rely=0.36, relwidth=0.25, relheight=0.07)
        password = Label(labelFrame, text="Course", bg='black', fg='white').place(
            relx=0.1, rely=0.45, relwidth=0.25, relheight=0.07)
        contact = Label(labelFrame, text="Subject", bg='black', fg='white').place(
            relx=0.1, rely=0.54, relwidth=0.25, relheight=0.07)
        dob = Label(labelFrame, text="Sub Book ID", bg='black', fg='white').place(
            relx=0.1, rely=0.63, relwidth=0.25, relheight=0.07)
        batch = Label(labelFrame, text="Stock of Library", bg='black', fg='white').place(
            relx=0.1, rely=0.72, relwidth=0.25, relheight=0.07)
        course = Label(labelFrame, text="Currently Available", bg='black', fg='white').place(
            relx=0.1, rely=0.81, relwidth=0.25, relheight=0.07)
        rating = Label(labelFrame, text="Rating", bg='black', fg='white').place(
            relx=0.1, rely=0.90, relwidth=0.25, relheight=0.07)

        fullname1 = Label(
            labelFrame, text=rows[0][0], bg='#cecece', fg='black')
        fullname1.place(relx=0.5, rely=0.18, relwidth=0.3, relheight=0.06)
        # print('fullname1',fullname1)
        username1 = Label(
            labelFrame, text=rows[0][1], bg='#cecece', fg='black')
        username1.place(relx=0.5, rely=0.27, relwidth=0.3, relheight=0.06)
        email1 = Label(labelFrame, text=rows[0][2], bg='#cecece', fg='black')
        email1.place(relx=0.5, rely=0.36, relwidth=0.3, relheight=0.06)
        password1 = Label(
            labelFrame, text=rows[0][4], bg='#cecece', fg='black')
        password1.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.06)
        contact1 = Label(labelFrame, text=rows[0][3], bg='#cecece', fg='black')
        contact1.place(relx=0.5, rely=0.54, relwidth=0.3, relheight=0.06)
        cur.execute(
            "select distinct sub_bid from subbook where bid='" + str(x) + "'")
        sub_b = list(cur.fetchall())
        dob1 = Label(labelFrame, text=sub_b, bg='#cecece', fg='black')
        dob1.place(relx=0.5, rely=0.63, relwidth=0.3, relheight=0.06)
        cur.execute(
            "select count(distinct sub_bid) from subbook where bid='" + str(x) + "'")
        b_num = list(cur.fetchall())
        batch1 = Label(labelFrame, text=b_num[0][0], bg='#cecece', fg='black')
        batch1.place(relx=0.5, rely=0.72, relwidth=0.3, relheight=0.06)
        cur.execute(
            "select count(distinct sub_bid) from subbook where is_available='yes' and bid='" + str(x) + "'")
        stock = list(cur.fetchall())
        course1 = Label(labelFrame, text=stock[0][0], bg='#cecece', fg='black')
        course1.place(relx=0.5, rely=0.81, relwidth=0.3, relheight=0.06)
        rating1 = Label(labelFrame, text=rows[0][5], bg='#cecece', fg='black')
        rating1.place(relx=0.5, rely=0.90, relwidth=0.3, relheight=0.06)

    def update_book_all(val):
        x = val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        def all_update():
            Subject_name = e_subject.get()
            CName = e_category.get()
            # Bid = e_bid.get()
            Bname = e_bname.get()
            Author = e_author.get()
            Rating = rating1.get()
            Thumbnail = thumbnail1.get()
            if(Subject_name == '' or CName == '' or Bname == '' or Author == '' or Rating == '' or Thumbnail == ''):  # or Bid==
                messagebox.showinfo(
                    "Insert Status", "All fields are required!")
            else:
                try:
                    cur.execute(
                        "insert into Subject values('" + Subject_name + "')")
                    cur.execute("insert into Category values('" +
                                CName + "','" + Subject_name + "')")
                except(mysql.connector.errors.IntegrityError):
                    pass

            cur.execute("UPDATE book SET Bname='" + Bname + "',Author='" + Author + "',Rating='" + Rating + "',Subject_name='" +
                        Subject_name + "',CName='" + CName + "',Thumbnail='" + Thumbnail + "' WHERE Bid='" + str(x) + "'")
            con.commit()

            # e_bid.delete(0, 'end')
            e_subject.delete(0, 'end')
            e_category.delete(0, 'end')
            rating1.delete(0, 'end')
            thumbnail1.delete(0, 'end')
            e_bname.delete(0, 'end')
            e_author.delete(0, 'end')

            messagebox.showinfo(
                "Update Status", "Successfully Updated into database")

        cur.execute(
            "select Bname,Author,CName,Subject_name,Rating,Thumbnail from book where Bid='" + str(x) + "'")
        rows = list(cur.fetchall())

        details = Label(labelFrame, text="Book Update", bg='white', fg='black', font='BOLD').place(
            relx=0.08, rely=0.06, relwidth=0.3, relheight=0.1)
        fullname = Label(labelFrame, text="Book Name", bg='black', fg='white').place(
            relx=0.1, rely=0.18, relwidth=0.25, relheight=0.07)
        username = Label(labelFrame, text="Author", bg='black', fg='white').place(
            relx=0.1, rely=0.27, relwidth=0.25, relheight=0.07)
        email = Label(labelFrame, text="Course", bg='black', fg='white').place(
            relx=0.1, rely=0.36, relwidth=0.25, relheight=0.07)
        password = Label(labelFrame, text="Subject", bg='black', fg='white').place(
            relx=0.1, rely=0.45, relwidth=0.25, relheight=0.07)
        contact = Label(labelFrame, text="Rating", bg='black', fg='white').place(
            relx=0.1, rely=0.54, relwidth=0.25, relheight=0.07)
        dob = Label(labelFrame, text="Thumbnail", bg='black', fg='white').place(
            relx=0.1, rely=0.63, relwidth=0.25, relheight=0.07)

        e_bname = Entry(labelFrame, bg='#cecece', fg='black')
        e_bname.insert(0, rows[0][0])
        e_bname.place(relx=0.5, rely=0.18, relwidth=0.3, relheight=0.06)
        # print('fullname1',fullname1)
        e_author = Entry(labelFrame, bg='#cecece', fg='black')
        e_author.insert(0, rows[0][1])
        e_author.place(relx=0.5, rely=0.27, relwidth=0.3, relheight=0.06)
        e_category = Entry(labelFrame, bg='#cecece', fg='black')
        e_category.insert(0, rows[0][2])
        e_category.place(relx=0.5, rely=0.36, relwidth=0.3, relheight=0.06)
        e_subject = Entry(labelFrame, bg='#cecece', fg='black')
        e_subject.insert(0, rows[0][3])
        e_subject.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.06)
        rating1 = Entry(labelFrame, bg='#cecece', fg='black')
        rating1.insert(0, rows[0][4])
        rating1.place(relx=0.5, rely=0.54, relwidth=0.3, relheight=0.06)
        thumbnail1 = Entry(labelFrame, bg='#cecece', fg='black')
        thumbnail1.insert(0, rows[0][5])
        thumbnail1.place(relx=0.5, rely=0.63, relwidth=0.3, relheight=0.06)

        add = Button(labelFrame, text='Update', bg='#7d7d7d', fg='black', command=all_update).place(
            relx=0.7, rely=0.06, relwidth=0.25, relheight=0.1)

    # Manage Books

    lb2 = Menu(menubar, tearoff=0, bg='#525b59', fg='white')
    menubar.add_cascade(label='Manage Books', menu=lb2)
    lb2.add_command(label='View Library', command=view)
    # lb2.add_command(label='Issued Books',command=None)
    lb2.add_separator()
    lb2.add_command(label='Add Books', command=add_book)
    lb2.add_command(label='Update Book Details', command=book_update)
    lb2.add_command(label='Delete Book', command=delete)

    # Pending files
    # pending Requests

    def pending_request():
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # refresh=Button(labelFrame, bg="black",fg="white")
        # refresh.place(relx=0.01,rely=0.01,relwidth=0.03,relheight=0.05)

        ls = Listbox(labelFrame, bg="black", relief="sunken",
                     font=("courier", 15), fg="white")
        ls.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

        def r_accept(r_a_val):
            x = r_a_val
            d1 = today.strftime("%Y-%m-%d")
            cur.execute(
                "select is_available from subbook where sub_bid='" + str(x[1]) + "'")
            ch = list(cur.fetchall())
            check = str(ch[0][0])
            # print(check,x[1])
            if check.lower() == 'yes':
                addformula = "INSERT INTO borrow (Student_regno,Sub_bid, Approved_date) VALUES (%s, %s, %s)"
                add_accept = (x[0], x[1], d1)
                cur.execute(addformula, add_accept)
                con.commit()
                cur.execute(
                    "UPDATE Subbook SET is_available='no' WHERE Sub_bid='" + str(x[1]) + "'")
                con.commit()
                messagebox.showinfo(
                    "Approved", "Book is Approved to Student whose Reg.no is '" + str(x[0])+"'!!")
                cur.execute(
                    "delete from book_request where Sub_bid='" + str(x[1]) + "'")
                con.commit()
                pending_request()
            else:
                messagebox.showinfo(
                    "Failed", "Approval Failed!!!\n Book is not available!!")

        def r_deny(r_a_val):
            x = r_a_val
            cur.execute(
                "delete from book_request where Sub_bid='" + str(x[1]) + "'")
            con.commit()
            messagebox.showinfo("Denied", "Request for this book is denied!!!")
            pending_request()

            # def show():
        ls.delete(0, 'end')
        # start
        h = Scrollbar(ls, orient='horizontal')
        h.pack(side=BOTTOM, fill=X)
        v = Scrollbar(ls)
        v.pack(side=RIGHT, fill=Y)
        t = Text(ls, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end
        # where book_request.student_regno")
        cur.execute("select DISTINCT book_request.student_regno, book_request.sub_bid,book_request.date, subbook.Bid, book.BName, book.Author from book_request,book,subbook where book.Bid=Subbook.Bid AND book_request.Sub_bid=subbook.Sub_bid;")
        rows = list(cur.fetchall())
        reg = Label(ls, text='Reg.No.', bg='#97cee3', fg='white',
                    width=10, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_bookid = Label(ls, text='Bookid', bg='#97cee3',
                         fg='white', width=10, font='BOLD', anchor='w')
        t.window_create(END, window=s_bookid)
        s_sub = Label(ls, text='Sub BookID', bg='#97cee3',
                      fg='white', width=10, font='BOLD', anchor='c')
        t.window_create(END, window=s_sub)
        s_name = Label(ls, text='Book Name', bg='#97cee3',
                       fg='white', width=20, font='BOLD', anchor='c')
        t.window_create(END, window=s_name)
        s_au = Label(ls, text='Author', bg='#97cee3', fg='white',
                     width=20, font='BOLD', anchor='c')
        t.window_create(END, window=s_au)
        s_date = Label(ls, text='Date', bg='#97cee3', fg='white',
                       width=15, font='BOLD', anchor='c')
        t.window_create(END, window=s_date)
        s_accept_deny = Label(ls, text='Accept/Deny', bg='#97cee3',
                              fg='white', font='BOLD', width=14, anchor='c')
        t.window_create(END, window=s_accept_deny)

        t.insert(END, "\n")
        for row in rows:
            val = row
            reg = Label(ls, text=row[0], bg='yellow',
                        fg='black', width=13, anchor='w')
            t.window_create(END, window=reg)
            s_name = Label(ls, text=row[3], bg='yellow',
                           fg='black', width=12, anchor='c')
            t.window_create(END, window=s_name)
            s_book = Label(ls, text=row[1], bg='yellow',
                           fg='black', width=15, anchor='c')
            t.window_create(END, window=s_book)
            s_au = Label(ls, text=row[4], bg='yellow',
                         fg='black', width=30, anchor='w')
            t.window_create(END, window=s_au)
            s_sb = Label(ls, text=row[5], bg='yellow',
                         fg='black', width=27, anchor='w')
            t.window_create(END, window=s_sb)
            s_date = Label(ls, text=row[2], bg='yellow',
                           fg='black', width=12, anchor='w')
            t.window_create(END, window=s_date)
            s_accept = Button(ls, text='Accept', bg='grey', fg='black', command=(
                lambda x=val: r_accept(x)), width=8, anchor='c')
            t.window_create(END, window=s_accept)
            s_deny = Button(ls, text='Deny', bg='grey', fg='black', command=(
                lambda x=val: r_deny(x)), width=8, anchor='c')
            t.window_create(END, window=s_deny)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end

    # pending books
    def pending_books():
        # x=val
        for widget in labelFrame.winfo_children():
            widget.destroy()

        # refresh=Button(labelFrame, bg="black",fg="white")
        # refresh.place(relx=0.01,rely=0.01,relwidth=0.03,relheight=0.05)

        ls = Listbox(labelFrame, bg="black", relief="sunken",
                     font=("courier", 15), fg="white")
        ls.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.92)

        # def show():
        ls.delete(0, 'end')
        # start
        h = Scrollbar(ls, orient='horizontal')
        h.pack(side=BOTTOM, fill=X)
        v = Scrollbar(ls)
        v.pack(side=RIGHT, fill=Y)
        t = Text(ls, width=30, height=30, wrap=NONE,
                 xscrollcommand=h.set, yscrollcommand=v.set)
        # end
        cur.execute("select student.Sname,student.Regno,book.bname,SubBook.Sub_bid, Borrow.Approved_date,Borrow.borrow_id From student,Book,SubBook,Borrow where Book.Bid = SubBook.Bid and Student.Regno = Borrow.student_regno and SubBook.Sub_bid = Borrow.Sub_bid ")
        rows = list(cur.fetchall())
        reg = Label(ls, text='Reg.No.', bg='#97cee3', fg='white',
                    width=10, font='BOLD', anchor='w')
        t.window_create(END, window=reg)
        s_name = Label(ls, text='Name', bg='#97cee3', fg='white',
                       width=17, font='BOLD', anchor='w')
        t.window_create(END, window=s_name)
        s_bookname = Label(ls, text='book name', bg='#97cee3',
                           fg='white', width=25, font='BOLD', anchor='w')
        t.window_create(END, window=s_bookname)
        s_sub_id = Label(ls, text='sub bookid', bg='#97cee3',
                         fg='white', width=13, font='BOLD', anchor='c')
        t.window_create(END, window=s_sub_id)
        s_borrow = Label(ls, text='borrow date', bg='#97cee3',
                         fg='white', font='BOLD', width=13, anchor='c')
        t.window_create(END, window=s_borrow)
        s_borrowid = Label(ls, text='borrow id', bg='#97cee3',
                           fg='white', width=13, font='BOLD', anchor='c')
        t.window_create(END, window=s_borrowid)
        s_receive = Label(ls, text='Receive book', bg='#97cee3',
                          fg='white', font='BOLD', width=10, anchor='c')
        t.window_create(END, window=s_receive)

        t.insert(END, "\n")
        for row in rows:
            val = row
            reg = Label(ls, text=row[1], bg='yellow',
                        fg='black', width=13, anchor='w')
            t.window_create(END, window=reg)
            s_name = Label(ls, text=row[0], bg='yellow',
                           fg='black', width=22, anchor='w')
            t.window_create(END, window=s_name)
            s_bookid = Label(
                ls, text=row[2], bg='yellow', fg='black', width=35, anchor='w')
            t.window_create(END, window=s_bookid)
            s_sub_id = Label(
                ls, text=row[3], bg='yellow', fg='black', width=15, anchor='c')
            t.window_create(END, window=s_sub_id)
            s_borrow = Label(
                ls, text=row[4], bg='yellow', fg='black', width=16, anchor='c')
            t.window_create(END, window=s_borrow)
            s_borrowid = Label(
                ls, text=row[5], bg='yellow', fg='black', width=15, anchor='c')
            t.window_create(END, window=s_borrowid)
            s_receive = Button(ls, text='Recieve Book', bg='grey', fg='black', command=(
                lambda x=val: b_receive(x)), width=13, anchor='c')
            t.window_create(END, window=s_receive)
            t.insert(END, "\n")
            # insertdata = "%-12.5s%-10s%-20s%-10s%-10s%-12.5s\n"%(row[0],row[1],row[2],row[6],row[7],'Message')
            # lboxs.insert(lboxs.size()+1, insertdata)
            # t.insert(END,insertdata)
            # start
        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end

    # receive BOOK
    def b_receive(data):
        x = data
        d1 = today.strftime("%Y-%m-%d")
        addformula = "INSERT INTO return_book (Student_regno,Sub_bid, Approved_date,Return_date,Borrow_id) VALUES (%s, %s, %s, %s, %s)"
        add_receive = (x[1], x[3], x[4], d1, x[5])
        cur.execute(addformula, add_receive)
        con.commit()
        cur.execute(
            "UPDATE Subbook SET is_available='yes' WHERE Sub_bid='" + str(x[3]) + "'")
        con.commit()
        cur.execute("delete from borrow where Borrow_id='" + str(x[5]) + "'")
        con.commit()
        messagebox.showinfo(
            "Added Successfully", "Book is received and history is updated of Student with Reg.no '"+str(x[1])+"'!!")
        pending_books()

    lb3 = Menu(menubar, tearoff=0, bg='#525b59', fg='white')
    menubar.add_cascade(label='Pending Files', menu=lb3)
    lb3.add_command(label='Pending Requests', command=pending_request)
    lb3.add_command(label='Pending Books', command=pending_books)

    # Query/Feedback

    '''lb4 = Menu(menubar,tearoff=0,bg='#525b59', fg='white')
    menubar.add_cascade(label='Qwery/Feedback',menu=lb4)
    lb4.add_command(label='Feedback',command=None)
    lb4.add_command(label='Query',command=None)'''

    # quitBtn = Button(admin,text="Quit",bg='#f7f1e3', fg='black', command=admin.destroy)
    # quitBtn.place(relx=0.05,rely=0.92, relwidth=0.18,relheight=0.05)

    admin.config(menu=menubar)
    admin.mainloop()


if __name__ == "__main__":
    start_admin('admin@54', 'pass')
