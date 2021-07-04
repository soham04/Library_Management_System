from tkinter import *
from tkinter import font as tkFont

def history(bottomF, Regno, cur):
    # global Regno,cur,win,topF,bottomF,tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    #start
    listbox = Listbox(bottomF, relief="sunken", font=("courier", 15),fg="white")
    listbox.place(relx=0, rely=0,relwidth=0.9848,relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
    #end
    command='select DISTINCT Book.Bname,Book.Author,Return_book.Approved_date,Return_book.Return_date,Book.Bid,SubBook.Sub_bid,Return_book.Borrow_ID from Book,Student,SubBook,Return_book WHERE Book.Bid=SubBook.Bid and SubBook.Sub_bid=Return_book.Sub_bid and Return_book.Student_regno=%s'
    var=[Regno]
    cur.execute(command,var)
    rows=cur.fetchall()

    if len(rows)==0:
        messageFont = tkFont.Font(family='product sans', size=18)
        message = Label(listbox, text='nothing to show!', bg="yellow", fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
        message.place(relx=0.4,rely=0.4)
        return

    bookNameFont = tkFont.Font(family='product sans', size=13)
    bookName = Label(listbox,text='Book Name', bg="black", fg='white',width=40, borderwidth=0,font=bookNameFont, anchor='c')
    t.window_create(END,window=bookName)

    authorFont = tkFont.Font(family='product sans', size=13)
    author = Label(listbox, text='Author', bg="black", fg='white', width=40, borderwidth=0, font=authorFont, anchor='c')
    t.window_create(END,window=author)

    approveddateFont = tkFont.Font(family='product sans', size=13)
    approveddate = Label(listbox, text='Approved Date', bg="black", fg='white', width=13, borderwidth=0, font=approveddateFont, anchor='c')
    t.window_create(END,window=approveddate)

    returndateFont = tkFont.Font(family='product sans', size=13)
    returndate = Label(listbox, text='Return date', bg="black", fg='white', width=13, borderwidth=0, font=returndateFont, anchor='c')
    t.window_create(END,window=returndate)

    bidFont = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Book ID', bg="black", fg='white', width=13, borderwidth=0, font=bidFont, anchor='c')
    t.window_create(END,window=bid)

    subbidFont = tkFont.Font(family='product sans', size=13)
    subbid = Label(listbox, text='Sub Book ID', bg="black", fg='white', width=13, borderwidth=0, font=subbidFont, anchor='c')
    t.window_create(END,window=subbid)

    borrowidFont = tkFont.Font(family='product sans', size=13)
    borrowid = Label(listbox, text='Borrow ID', bg="black", fg='white', width=13, borderwidth=0, font=borrowidFont, anchor='c')
    t.window_create(END,window=borrowid)
    t.insert(END,"\n")
    t.insert(END,"\n")

    for a in rows:
        bookNameFont = tkFont.Font(family='product sans', size=13)
        bookName = Label(listbox,text=str(a[0]), bg="yellow",width=40, borderwidth=0,font=bookNameFont, anchor='w')
        t.window_create(END,window=bookName)

        authorFont = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text=str(a[1]), bg="white", width=40, borderwidth=0, font=authorFont, anchor='w')
        t.window_create(END,window=author)

        approveddateFont = tkFont.Font(family='product sans', size=13)
        approveddate = Label(listbox, text=str(a[2]), bg="yellow", width=13, borderwidth=0, font=approveddateFont, anchor='c')
        t.window_create(END,window=approveddate)

        returndateFont = tkFont.Font(family='product sans', size=13)
        returndate = Label(listbox, text=str(a[3]), bg="white", width=13, borderwidth=0, font=returndateFont, anchor='c')
        t.window_create(END,window=returndate)

        bidFont = tkFont.Font(family='product sans', size=13)
        bid = Label(listbox, text=str(a[4]), bg="white", width=13, borderwidth=0, font=bidFont, anchor='c')
        t.window_create(END,window=bid)

        subbidFont = tkFont.Font(family='product sans', size=13)
        subbid = Label(listbox, text=str(a[5]), bg="yellow", width=13, borderwidth=0, font=subbidFont, anchor='c')
        t.window_create(END,window=subbid)

        borrowidFont = tkFont.Font(family='product sans', size=13)
        borrowid = Label(listbox, text=str(a[6]), bg="white", width=13, borderwidth=0, font=borrowidFont, anchor='c')
        t.window_create(END,window=borrowid)

        '''
        buttonsFont = tkFont.Font(family='product sans', size=12)
        cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2') 
        t.window_create(END,window=cancel)
        '''
        t.insert(END,"\n")
        t.insert(END,"\n")
    #start
    t.configure(state="disabled")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    #end

# def history(bottomF):
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
#     for i in range(numOfRequest):
#         bookNameFont = tkFont.Font(family='product sans', size=13)
#         bookName = tkinter.Label(listbox, text='Requested_Book_Name : ' + str(
#             i), bg="gray", width=60, borderwidth=0, font=bookNameFont, anchor='w')
#         t.window_create(END, window=bookName)
#
#         dateFont = tkFont.Font(family='product sans', size=13)
#         date = tkinter.Label(listbox, text='rating', bg="blue",
#                              width=40, borderwidth=0, font=dateFont, anchor='w')
#         t.window_create(END, window=date)
#
#         statusFont = tkFont.Font(family='product sans', size=13)
#         status = tkinter.Label(listbox, text='status', bg="yellow",
#                                width=13, borderwidth=0, font=statusFont, anchor='c')
#         t.window_create(END, window=status)
#
#         buttonsFont = tkFont.Font(family='product sans', size=12)
#         cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont,
#                                 bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2')
#         t.window_create(END, window=cancel)
#         t.insert(END, "\n")
#     # start
#     t.configure(state="disabled")
#     t.pack(side=TOP, fill=X)
#     h.config(command=t.xview)
#     v.config(command=t.yview)
#     # end
