from tkinter import *
from tkinter import font as tkFont, messagebox


# common_request() wil be used for inset sub book id into boo_request table
def send_book_request(bookid, cur, Regno, con):
    # global cur, win, topF, bottomF, tabF, Regno, con
    try:
        # command='select subbook.sub_bid from book, subbook where book.bid=subbook.bid and book.bid=%s and subbook.is_available="yes" and subbook.sub_bid not in(select sub_bid from book_request) and (subbook.sub_bid,%s) not in(select subbook.sub_bid, book_request.student_regno from subbook,book_request where )'
        command = 'select subbook.sub_bid from subbook where subbook.bid=%s and subbook.is_available="yes" and subbook.sub_bid not in(select sub_bid from book_request) and %s not in(select book_request.student_regno from subbook,book_request where subbook.sub_bid=book_request.sub_bid and subbook.bid=%s)'
        var = [bookid, Regno, bookid]
        cur.execute(command, var)
        result = cur.fetchall()

        if len(result) == 0:
            messagebox.showinfo("ALERT", "SOME ERROR OCCURED \n TRY AFTER SOMETIME")
            return
        command = 'insert into book_request values(%s,%s,CURDATE())'
        var = [result[0][0], Regno]
        cur.execute(command, var)
        con.commit()
        messagebox.showinfo("SUCCESS", "REQUEST ADDED")
    except Exception as e:
        print(e)


# display book that you have currently requested(i.e, Book from Book_request table)
def display_book_reuqests(bottomF, Regno, cur, con):
    # global con, cur, win, topF, bottomF, tabF, Regno
    for widget in bottomF.winfo_children():
        widget.destroy()

    # function to cancle book request
    def cancel_request(subid):
        try:
            command = 'delete from book_request where sub_bid=%s and student_regno=%s'
            var = [subid, Regno]
            cur.execute(command, var)
            con.commit()
            messagebox.showinfo("SUCCESS", "CANCELLED SUCCESSFULLY")
        except Exception as e:
            print(e)

            # start

    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15), fg="white")
    listbox.place(relx=0, rely=0, relwidth=0.9848, relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
    # end
    command = "select Book.Bname,Book_request.Date,Book_request.sub_bid from book_request,subbook,book where book_request.sub_bid=subbook.sub_bid and subbook.bid=book.bid and Book_request.student_regno=%s"
    var = [Regno]
    cur.execute(command, var)
    result1 = cur.fetchall()

    if len(result1) == 0:
        messageFont = tkFont.Font(family='product sans', size=18)
        message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0,
                        font=messageFont, anchor='c')
        message.place(relx=0.4, rely=0.4)
        return

    bookNameFont = tkFont.Font(family='product sans', size=13)
    bookName = Label(listbox, text='Book Name', bg="black", fg='white', width=55, borderwidth=0, font=bookNameFont,
                     anchor='w')
    t.window_create(END, window=bookName)

    dateFont = tkFont.Font(family='product sans', size=13)
    date = Label(listbox, text='Request Date', bg="black", fg='white', width=40, borderwidth=0, font=dateFont,
                 anchor='c')
    t.window_create(END, window=date)

    statusFont = tkFont.Font(family='product sans', size=13)
    status = Label(listbox, text='Id', bg="black", fg='white', width=13, borderwidth=0, font=statusFont, anchor='c')
    t.window_create(END, window=status)

    cancelFont = tkFont.Font(family='product sans', size=14)
    cancelbtn = Label(listbox, text='Cancel Request', bg="black", fg='white', width=13, borderwidth=0, font=cancelFont,
                      anchor='c')
    t.window_create(END, window=cancelbtn)

    t.insert(END, "\n")

    for r in result1:
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox, text=r[0], bg="yellow", width=55, borderwidth=0, font=bookNameFont, anchor='w')
        t.window_create(END, window=bookName)

        dateFont = tkFont.Font(family='product sans', size=13)
        date = Label(listbox, text=r[1], bg="white", width=40, borderwidth=0, font=dateFont, anchor='c')
        t.window_create(END, window=date)

        statusFont = tkFont.Font(family='product sans', size=13)
        status = Label(listbox, text=r[2], bg="yellow", fg='black', width=13, borderwidth=0, font=statusFont,
                       anchor='c')
        t.window_create(END, window=status)

        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = Button(listbox, text="Cancel Request", command=(lambda x=r[2]: cancel_request(x)), font=buttonsFont,
                        bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2')
        t.window_create(END, window=cancel)
        t.insert(END, "\n")
    # start
    t.configure(state="disabled")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    # end

# def reuqests(bottomF):
#     for widget in bottomF.winfo_children():
#         widget.destroy()
#
#     numOfRequest = 20
#
#     # start
#     listbox = Listbox(bottomF, relief="sunken",
#                       font=("courier", 15), fg="white")
#     listbox.place(relx=0.5, rely=0.43, relwidth=0.92,
#                   relheight=0.85, anchor=CENTER)
#     h = Scrollbar(bottomF, orient='horizontal')
#     h.place(relx=0.5, rely=0.9, anchor=S, relwidth=0.92)
#     v = Scrollbar(bottomF, orient='vertical')
#     v.pack(side=RIGHT, fill=Y)
#     v.place(relx=0.98, rely=0.43, anchor=E, relheight=0.92)
#     t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
#     # end
#
#     filePath = pathlib.Path(__file__).parent.absolute()
#     filePath = str(str(filePath) + "\\images\\peng.jpg")
#     img = ImageTk.PhotoImage(Image.open(filePath).resize((120, 150), Image.ANTIALIAS))
#
#     for i in range(numOfRequest):
#         thumbNail = tkinter.Label(
#             listbox, image=img, height=150, width=120, borderwidth=1, anchor='w')
#         thumbNail.image = img
#         t.window_create(END, window=thumbNail)
#
#         bookNameFont = tkFont.Font(family='product sans', size=13)
#         bookName = tkinter.Label(listbox, text='C programming vol : ' + str(
#             i), bg="pink", width=60, borderwidth=0, font=bookNameFont, anchor='w')
#         t.window_create(END, window=bookName)
#
#         dateFont = tkFont.Font(family='product sans', size=13)
#         date = tkinter.Label(listbox, text='issueDate_returnDate',
#                              bg="blue", width=40, borderwidth=0, font=dateFont, anchor='c')
#         t.window_create(END, window=date)
#
#         statusFont = tkFont.Font(family='product sans', size=13)
#         status = tkinter.Label(listbox, text='status', bg="light yellow",
#                                fg='black', width=13, borderwidth=0, font=statusFont, anchor='c')
#         t.window_create(END, window=status)
#
#         buttonsFont = tkFont.Font(family='product sans', size=12)
#         cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont,
#                                 bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2')
#         t.window_create(END, window=cancel)
#
#         t.insert(END, "\n")
#     # start
#     t.configure(state="disabled")
#     t.pack(side=TOP, fill=X)
#     h.config(command=t.xview)
#     v.config(command=t.yview)
#     # end
