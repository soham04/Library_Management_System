import webbrowser
from tkinter import font as tkFont
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter.ttk import *
from tkinter import *
import pymysql
# from login import *
import orig
# from orig import *
# user_defined module imports

from student_package import tabs_module, topF_module, search_module, home_module, tabs_module, request_modules, \
    history_module

# ENTER YOUR MACHINE DB DETAILS
mypass = "soham"
mydatabase = "library"
username = "root"

con = pymysql.connect(host="localhost", user=username, password=mypass, database=mydatabase)
cur = con.cursor()


def start_student(reg, password2, win1="default"):
    # global cur, con, Regno, win, topF, bottomF, tabF
    if __name__ != "__main__":
        win1.destroy()

    Regno = reg

    # start
    # fetching data of user after login
    command = 'select Book.Bname,Book.Author,Borrow.Approved_date,ADDDATE(Borrow.Approved_date, 14),DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14))*1 from Borrow, SubBook, Book where Student_regno=%s and Borrow.sub_bid=SubBook.sub_bid and SubBook.bid=Book.bid and DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14)) > 0'
    var = [Regno]
    cur.execute(command, var)
    var = cur.fetchall()
    fine = 0
    for i in range(len(var)):
        fine += float(var[i][4])

    command = 'update student set fine=%s where Regno=%s'
    var = [fine, Regno]
    cur.execute(command, var)
    con.commit()

    command = "select Sname, Fine from student where Regno=%s and Password=%s"
    var = [reg, password2]
    cur.execute(command, var)
    user_details = cur.fetchall()
    # end

    # Making the window -------------------------------------
    win = Tk()
    win.title(str("Hii, " + user_details[0][0]) + "  |   Welcome to IIIT Kottayam Library   |   Student Section")
    h = (win.winfo_screenheight() * 4.4) // 5
    win.geometry('%sx%s+%s+%s' % (1150, int(h), 50, 6))
    win.config(bg='red')
    win.resizable(False, False)

    # FRAMES -------------------------------------------------------------------------

    # start
    topF = Frame(win, borderwidth=-1, bg='white')
    topF.place(relx=0, rely=0, relwidth=1, relheight=0.2206)

    tabF = Frame(win, relief=SUNKEN, bg="white")
    tabF.place(relx=0, rely=0.2206, relwidth=1, relheight=0.08)

    bottomF = Frame(win, relief=SUNKEN, bg="white")
    bottomF.place(relx=0, rely=0.2206 + 0.08, relwidth=1, relheight=1 - 0.2206 - 0.08)
    # end

    # FINE FRAME CONTENT ------------------------------------------------------
    listbox1 = Listbox(topF, relief="flat", borderwidth=0, font=("courier", 15), bg='white')
    listbox1.place(relx=0.8, rely=0, relwidth=1, relheight=1)

    # function to display message of PayFine button
    def message():
        messagebox.showinfo("Sorry, This option is not available!\n", "Kindly contact to your Admin")

    fineFont = tkFont.Font(size=15, weight=BOLD, family="product sans")
    user = Label(listbox1, text='User : ' + str(user_details[0][0]), fg="green", font=fineFont)
    user.place(relx=0, rely=0)
    Fine = Label(listbox1, text='Fine  : ' + str(user_details[0][1]), fg="red", font=fineFont)
    Fine.place(relx=0, rely=0.25 + 0.05)

    def payFine():
        try:
            webbrowser.open("https://www.onlinesbi.com/sbicollect/icollecthome.htm")
        except:
            messagebox.showinfo("Error!", "Something went wrong")

    if fine > 0:
        pay_fine = Button(listbox1, text='Pay Fine', bg='green', fg='white', activeforeground='black', command=payFine,
                          bd='2', cursor='hand2', font=fineFont)
        pay_fine.place(relx=0.125, rely=0.23 + 0.05)

    logout = Button(listbox1, text='Logout', bg='Red', fg='Black', activeforeground='black',
                    command=lambda x=win: orig.start_login(x), bd='2', font=fineFont)
    logout.place(relx=0.125 - 0.05, rely=0.23 + 0.51)
    # end of Fine frame

    tabs_module.tabs(tabF, bottomF, con, cur, reg)
    topF_module.titleBar(topF)
    home_module.home(bottomF, cur, con, Regno)
    win.mainloop()


if __name__ == "__main__":
    start_student('2019bcs008', 'kunalpassword')
