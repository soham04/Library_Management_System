import tkinter
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
from tkinter import ttk


def send_book_request(cur, Regno, con, bookid):
    # global cur, win, topF, bottomF, tabF, Regno, con
    try:
        # command='select subbook.sub_bid from book, subbook where book.bid=subbook.bid and book.bid=%s and subbook.is_available="yes" and subbook.sub_bid not in(select sub_bid from book_request) and (subbook.sub_bid,%s) not in(select subbook.sub_bid, book_request.student_regno from subbook,book_request where )'
        command = 'select subbook.sub_bid from subbook where subbook.bid=%s and subbook.is_available="yes" and subbook.sub_bid not in(select sub_bid from book_request) and %s not in(select book_request.student_regno from subbook,book_request where subbook.sub_bid=book_request.sub_bid and subbook.bid=%s)'
        var = [bookid, Regno, bookid]
        cur.execute(command, var)
        result = cur.fetchall()

        if len(result) == 0:
            messagebox.showinfo("Message", "Try after some time.")
            return
        command = 'insert into book_request values(%s,%s,CURDATE())'
        var = [result[0][0], Regno]
        cur.execute(command, var)
        con.commit()
        messagebox.showinfo("Sucess", "Request added")
    except Exception as e:
        print(e)


def mybooks(bottomF, cur, Regno, con, arg='Favorite Book'):
    # global regno, cur, win, topF, bottomF, tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    # start
    listbox = tkinter.Listbox(bottomF, relief="sunken", font=("courier", 15), fg="white")
    listbox.place(relx=0, rely=0, relwidth=0.9848, relheight=0.959)
    h = tkinter.Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

    # end

    # start 22/10
    def decide_mybook(event):
        if str(mybook_combo.get()) == 'Favorite Book':
            mybooks(bottomF, cur, Regno, con, 'Favorite Book')
        elif str(mybook_combo.get()) == 'Borrowed Book':
            mybooks(bottomF, cur, Regno, con, 'Borrowed Book')
        else:
            messagebox.showinfo("Error!", "Something went wrong")
            return

            # creating Combobox

    mybook_combo = ttk.Combobox(listbox, width=15, state="readonly", font="arial 12 bold")
    val = ['Favorite Book', 'Borrowed Book']
    mybook_combo['values'] = val
    if arg == 'Favorite Book':
        mybook_combo.current(0)
    elif arg == 'Borrowed Book':
        mybook_combo.current(1)
    else:
        messagebox.showinfo("Error!", "Something went wrong")

    mybook_combo.bind("<<ComboboxSelected>>", decide_mybook)
    mybook_combo.place(relx=0.22 + 0.25, rely=0.03)

    # end 22/10

    def borrowed_book():
        result = []
        try:
            command = 'select book.bname,book.author,borrow.approved_date,borrow.borrow_id,ADDDATE(borrow.approved_date,14),book.bid,subbook.sub_bid from borrow,subbook,book where borrow.sub_bid=subbook.sub_bid and subbook.bid=book.bid and borrow.student_regno=%s'
            var = [Regno]
            cur.execute(command, var)
            result = cur.fetchall()
        except Exception as e:
            messagebox.showinfo("Error!", "Something went worng")
            print(e)

        if len(result) == 0:
            messageFont = tkFont.Font(family='product sans', size=18)
            message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0,
                            font=messageFont, anchor='c')
            message.place(relx=0.4, rely=0.4)
            return

        t.insert(END, "\n")
        t.insert(END, "\n")
        t.insert(END, "\n")
        bookNameFont = tkFont.Font(family='product sans', size=12)
        bookName = Label(listbox, text='Book Name', bg="black", fg='white', width=55, borderwidth=0, font=bookNameFont,
                         anchor='w')
        t.window_create(END, window=bookName)

        authorFont = tkFont.Font(family='product sans', size=12)
        author = Label(listbox, text='Author', bg="black", fg='white', width=35, borderwidth=0, font=authorFont,
                       anchor='w')
        t.window_create(END, window=author)

        approveddateFont = tkFont.Font(family='product sans', size=12)
        approveddate = Label(listbox, text='Approved Date', bg="black", fg='white', width=15, borderwidth=0,
                             font=approveddateFont, anchor='c')
        t.window_create(END, window=approveddate)

        borrowIDFont = tkFont.Font(family='product sans', size=12)
        borrowID = Label(listbox, text='Borrow ID', bg="black", fg='white', width=10, borderwidth=0, font=borrowIDFont,
                         anchor='c')
        t.window_create(END, window=borrowID)

        exp_returnFont = tkFont.Font(family='product sans', size=12)
        exp_return = Label(listbox, text='Expected return date', bg="black", fg='white', width=18, borderwidth=0,
                           font=exp_returnFont, anchor='c')
        t.window_create(END, window=exp_return)

        bidFont = tkFont.Font(family='product sans', size=12)
        bid = Label(listbox, text='Book ID', bg="black", fg='white', width=10, borderwidth=0, font=bidFont, anchor='c')
        t.window_create(END, window=bid)

        sub_bidFont = tkFont.Font(family='product sans', size=12)
        sub_bid = Label(listbox, text='Sub BookID', bg="black", fg='white', width=12, borderwidth=0, font=sub_bidFont,
                        anchor='c')
        t.window_create(END, window=sub_bid)

        t.insert(END, "\n")

        for r in result:
            bookNameFont = tkFont.Font(family='product sans', size=12)
            bookName = Label(listbox, text=r[0], bg="green", fg='white', width=55, borderwidth=0, font=bookNameFont,
                             anchor='w')
            t.window_create(END, window=bookName)

            authorFont = tkFont.Font(family='product sans', size=12)
            author = Label(listbox, text=r[1], bg="yellow", width=35, borderwidth=0, font=authorFont, anchor='w')
            t.window_create(END, window=author)

            approveddateFont = tkFont.Font(family='product sans', size=12)
            approveddate = Label(listbox, text=r[2], bg="gray", width=15, borderwidth=0, font=approveddateFont,
                                 anchor='c')
            t.window_create(END, window=approveddate)

            borrowIDFont = tkFont.Font(family='product sans', size=12)
            borrowID = Label(listbox, text=r[3], bg="green", fg='white', width=10, borderwidth=0, font=borrowIDFont,
                             anchor='c')
            t.window_create(END, window=borrowID)

            exp_returnFont = tkFont.Font(family='product sans', size=12)
            exp_return = Label(listbox, text=r[4], bg="yellow", width=18, borderwidth=0, font=exp_returnFont,
                               anchor='c')
            t.window_create(END, window=exp_return)

            bidFont = tkFont.Font(family='product sans', size=12)
            bid = Label(listbox, text=r[5], bg="gray", width=10, borderwidth=0, font=bidFont, anchor='c')
            t.window_create(END, window=bid)

            sub_bidFont = tkFont.Font(family='product sans', size=12)
            sub_bid = Label(listbox, text=r[6], bg="green", fg='white', width=12, borderwidth=0, font=sub_bidFont,
                            anchor='c')
            t.window_create(END, window=sub_bid)

            t.insert(END, "\n")

        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end borrowed_book()

    # start favorite_book()
    def favorite_book():
        result = []
        try:
            command = 'select Book.Bname, Book.Author, Book.bid from Book, favorite_book where book.bid=favorite_book.Bid and favorite_book.student_regno=%s'
            var = [Regno]
            cur.execute(command, var)
            result = cur.fetchall()
        except Exception as e:
            messagebox.showinfo("Error!", "Something went worng")
            print(e)

        if len(result) == 0:
            messageFont = tkFont.Font(family='product sans', size=18)
            message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0,
                            font=messageFont, anchor='c')
            message.place(relx=0.4, rely=0.4)
            return

        t.insert(END, "\n")
        t.insert(END, "\n")
        t.insert(END, "\n")
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox, text='Book Name', bg="black", fg='white', width=55, borderwidth=0, font=bookNameFont,
                         anchor='w')
        t.window_create(END, window=bookName)

        authorFont = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text='Author', bg="black", fg='white', width=35, borderwidth=0, font=authorFont,
                       anchor='w')
        t.window_create(END, window=author)

        requestFont = tkFont.Font(family='product sans', size=12)
        reuqest = Label(listbox, text='Request Book', bg="black", fg='white', width=15, borderwidth=0, font=requestFont,
                        anchor='c')
        t.window_create(END, window=reuqest)

        removeFont = tkFont.Font(family='product sans', size=12)
        remove = Label(listbox, text='Remove from favorite', bg="black", fg='white', width=19, borderwidth=0,
                       font=removeFont, anchor='c')
        t.window_create(END, window=remove)

        # favorite  = Label(listbox, text='Request Button', bg="black", fg='white', width=17, borderwidth=0, font=requestFont, anchor='c')
        # t.window_create(END,window=favorite)
        t.insert(END, "\n")
        for r in result:
            bookNameFont = tkFont.Font(family='product sans', size=13)
            bookName = Label(listbox, text=r[0], bg="green", fg='white', width=55, borderwidth=0, font=bookNameFont,
                             anchor='w')
            t.window_create(END, window=bookName)

            authorFont = tkFont.Font(family='product sans', size=13)
            author = Label(listbox, text=r[1], bg="yellow", fg='black', width=35, borderwidth=0, font=authorFont,
                           anchor='w')
            t.window_create(END, window=author)

            requestFont = tkFont.Font(family='product sans', size=12)
            reuqest = Button(listbox, text="Request", command=(lambda x=r[2]: send_book_request(cur, Regno, con, x)),
                             font=requestFont,
                             bg="#F4B400", activebackground="#FFD666", anchor='c', width=14, cursor='hand2')
            t.window_create(END, window=reuqest)

            removeFont = tkFont.Font(family='product sans', size=12)
            remove = Button(listbox, text="Remove", command=(lambda x=r[2], y=r[0]: remove_favorite(x, y)),
                            font=removeFont, bg="#FFD666", activebackground="#FFD666", anchor='c', width=19,
                            cursor='hand2')
            t.window_create(END, window=remove)

            # favFont = tkFont.Font(family='product sans', size=12)
            # favorite = Button(listbox, text="Add to favorite", command=lambda x=r[2]:remove_favorite(x),font=favFont, bg="#FFD666", activebackground="#FFD666", anchor='c', width=16, cursor='hand2')
            # t.window_create(END,window=favorite)

            t.insert(END, "\n")
            # t.insert(END,"\n")

        t.configure(state="disabled")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        # end favorite_book()

    # calling function based on the value of combobox
    if arg == 'Favorite Book':
        favorite_book()
    elif arg == 'Borrowed Book':
        borrowed_book()
    else:
        messagebox.showinfo("Error!", "Something went wrong")
        return

        # start remove_favorite()

    def remove_favorite(book_id, bname):
        try:
            command = 'delete from favorite_book where bid=%s'
            var = [book_id]
            cur.execute(command, var)
            con.commit()
            messagebox.showinfo("Message", str(bname) + " has been removed from your favorite book list.")
            mybooks(bottomF, cur, Regno, con)
        except Exception as e:
            messagebox.showinfo("Error!", "Something went worng")
            print(e)
