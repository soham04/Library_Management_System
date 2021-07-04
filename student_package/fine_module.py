from tkinter import font as tkFont
import tkinter
from tkinter import *


def fine(bottomF, cur, Regno):
    # global Regno, cur, win, topF, bottomF, tabF
    for widget in bottomF.winfo_children():
        widget.destroy()

    # start
    listbox = Listbox(bottomF, relief="sunken",
                      font=("courier", 15), fg="white")
    listbox.place(relx=0, rely=0, relwidth=0.9848, relheight=0.959)
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)
    v = Scrollbar(bottomF, orient='vertical')
    v.pack(side=RIGHT, fill=Y)
    v.place(relx=1, rely=0.48, anchor=E, relheight=0.96)
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
    # end
    command = 'select Book.Bname,Book.Author,Borrow.Approved_date,ADDDATE(Borrow.Approved_date, 14),DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14))*1 from Borrow, SubBook, Book where Student_regno=%s and Borrow.sub_bid=SubBook.sub_bid and SubBook.bid=Book.bid and DATEDIFF(CURDATE(),ADDDATE(Borrow.Approved_date, 14)) > 0'
    # bookname-0,author-1,approved_date-2,expexted_return_date-3,fine-4
    var = [Regno]
    cur.execute(command, var)
    rows = cur.fetchall()
    if len(rows) == 0:
        messageFont = tkFont.Font(family='product sans', size=18)
        message = Label(listbox, text='nothing to show!', bg="yellow",
                        fg='black', width=20, borderwidth=0, font=messageFont, anchor='c')
        message.place(relx=0.4, rely=0.4)
        return

    Font0 = tkFont.Font(family='product sans', size=13)
    Bname = Label(listbox, text='Book Name', bg="black", fg='white',
                  width=38, borderwidth=0, font=Font0, anchor='c')
    t.window_create(END, window=Bname)

    Font1 = tkFont.Font(family='product sans', size=13)
    author = Label(listbox, text='Author', bg="black", fg='white',
                   width=38, borderwidth=0, font=Font1, anchor='c')
    t.window_create(END, window=author)

    Font2 = tkFont.Font(family='product sans', size=13)
    approveddate = Label(listbox, text='Approved Date', bg="black",
                         fg='white', width=13, borderwidth=0, font=Font2, anchor='c')
    t.window_create(END, window=approveddate)

    Font3 = tkFont.Font(family='product sans', size=13)
    returndate = Label(listbox, text='Expected Return date', bg="black",
                       fg='white', width=23, borderwidth=0, font=Font3, anchor='c')
    t.window_create(END, window=returndate)

    Font4 = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Fine', bg="black", fg='white',
                width=13, borderwidth=0, font=Font4, anchor='c')
    t.window_create(END, window=bid)
    '''
    Font4 = tkFont.Font(family='product sans', size=13)
    bid = Label(listbox, text='Return Button', bg="black", fg='white', width=17, borderwidth=0, font=Font4, anchor='c') 
    t.window_create(END,window=bid)
    '''
    t.insert(END, "\n")
    t.insert(END, "\n")

    for a in rows:
        # bookname-0,author-1,approved_date-2,expexted_return_date-3,fine-4
        Font0 = tkFont.Font(family='product sans', size=13)
        Bname = Label(listbox, text=a[0], bg="white",
                      width=38, borderwidth=0, font=Font0, anchor='w')
        t.window_create(END, window=Bname)

        Font1 = tkFont.Font(family='product sans', size=13)
        author = Label(listbox, text=a[1], bg="white",
                       width=38, borderwidth=0, font=Font1, anchor='w')
        t.window_create(END, window=author)

        Font2 = tkFont.Font(family='product sans', size=13)
        approveddate = Label(
            listbox, text=a[2], bg="yellow", width=13, borderwidth=0, font=Font2, anchor='c')
        t.window_create(END, window=approveddate)

        Font3 = tkFont.Font(family='product sans', size=13)
        returndate = Label(
            listbox, text=a[3], bg="white", width=23, borderwidth=0, font=Font3, anchor='c')
        t.window_create(END, window=returndate)

        Font4 = tkFont.Font(family='product sans', size=13)
        bid = Label(listbox, text=a[4], bg="yellow",
                    width=13, borderwidth=0, font=Font4, anchor='c')
        t.window_create(END, window=bid)

        '''
        Font5 = tkFont.Font(family='product sans', size=12)
        return_btn = Button(listbox, text="Return",command="", font=Font5, bg="#F4B400", activebackground="#FFD666", anchor='c', width=16,cursor='hand2') 
        t.window_create(END,window=return_btn)
        '''
        t.insert(END, "\n")
        t.insert(END, "\n")
    # start
    t.configure(state="disabled")
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    # end


# def fine(bottomF):
#     for widget in bottomF.winfo_children():
#         widget.destroy()

#     numOfRequest = 20

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

#     for i in range(numOfRequest):
#         bookNameFont = tkFont.Font(family='product sans', size=13)
#         bookName = tkinter.Label(listbox, text='Requested_Book_Name : ' + str(
#             i), bg="black", fg="white", width=60, borderwidth=0, font=bookNameFont, anchor='w')
#         t.window_create(END, window=bookName)

#         dateFont = tkFont.Font(family='product sans', size=13)
#         date = tkinter.Label(listbox, text='issue_date', bg="blue",
#                              width=40, borderwidth=0, font=dateFont, anchor='c')
#         t.window_create(END, window=date)

#         statusFont = tkFont.Font(family='product sans', size=13)
#         status = tkinter.Label(listbox, text='fine', bg="red",
#                                width=13, borderwidth=0, font=statusFont, anchor='c')
#         t.window_create(END, window=status)

#         buttonsFont = tkFont.Font(family='product sans', size=12)
#         cancel = tkinter.Button(listbox, text="Cancel/Return early", font=buttonsFont,
#                                 bg="#F4B400", activebackground="#FFD666", anchor='c', width=16, cursor='hand2')
#         t.window_create(END, window=cancel)
#         t.insert(END, "\n")

#     t.configure(state="disabled")
#     t.pack(side=TOP, fill=X)
#     h.config(command=t.xview)
#     v.config(command=t.yview)
