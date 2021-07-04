import pathlib
import tkinter
from io import BytesIO
from tkinter import Listbox, Scrollbar, Text
from tkinter import font as tkFont
from tkinter.constants import *

from PIL import ImageTk, Image

from student_package import makeRequest_module, markFav_module

#
# def markFav(x, ls, curr, connection, username):
#     bid = ls[x][1]
#     querry2 = '''SELECT *  FROM SubBook where (is_available = "yes" and bid = {bid:})'''
#     curr.execute(querry2.format(bid=bid))
#     connection.commit()
#     list2 = list(curr.fetchall())
#     print(list2)
#     # sub_bid = list2[0][1]  # GETTING THE LEAST SUB_BID
#     querry = '''insert into favorite_book values({bid},'{username}')'''
#     curr.execute(querry.format(bid=bid, username=username))
#     connection.commit()


def home(bottomF, curr, connection, username):
    for widget in bottomF.winfo_children():
        widget.destroy()

    # TRENDING TITLE
    titleFont = tkFont.Font(family='Bowlby One SC', size=20, weight="bold")
    title = tkinter.Label(bottomF, font=titleFont,
                          text="Trending Books📈", justify=LEFT, fg="#12492f", bg="#FFF1BF")
    title.place(anchor=N, relx=0.5, rely=0, relwidth=1, relheight=0.1)

    # LISTBOX
    listbox = Listbox(bottomF, relief="sunken",
                      font=("courier", 15), fg="white")
    listbox.place(relx=0.5, rely=1, relwidth=1,
                  relheight=0.9, anchor=S)

    # SCROLLBAR 
    h = Scrollbar(bottomF, orient='horizontal')
    h.place(relx=0.5, rely=1, anchor=S, relwidth=1)  # horizontal
    v = Scrollbar(bottomF, orient='vertical')
    v.place(relx=1, rely=1, anchor=SE, relheight=0.9)  # vertical

    # TEXTBOX IN LISTBOX
    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

    # TEMPORARY IMAGE OBJECT FOR TESTING PURPOSE
    filePath = pathlib.Path(__file__).parent.absolute()
    filePath = str(str(filePath)+"\\images\\peng.jpg")
    img = ImageTk.PhotoImage(Image.open(
        filePath).resize((150, 180), Image.ANTIALIAS))

    # NUMBER OF REUQEST
    numOfRequest = 10

    # STARS IMAGE
    filePath = pathlib.Path(__file__).parent.absolute()
    filePath = str(str(filePath)+"\\images\\stars.png")
    star = ImageTk.PhotoImage(Image.open(
        filePath).resize((200, 30), Image.ANTIALIAS))

    # RETRIEVING LIST FROM DB
    querry = '''SELECT * FROM book ORDER BY RATING DESC LIMIT {num}'''
    curr.execute(querry.format(num=numOfRequest))
    connection.commit()
    ls = list(curr.fetchall())  # LIST

    # REQUEST FUNCTION

    for i, j in zip(range(numOfRequest), ls):

        # UNIT FRAME
        f1 = tkinter.Frame(listbox, height=182,
                           width=1140, borderwidth=1, background="white")

        # THUMBNAIL RETREIVAL
        # file =  ""
        file = j[6]
        img = Image.open(BytesIO(file)).resize((150, 180), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        # THUMBNAIL PLACEMENT
        thumbNail = tkinter.Label(
            f1, image=img, height=180, justify=LEFT, width=150, borderwidth=1, anchor='w')
        thumbNail.image = img
        thumbNail.place(relx=0+0.05, rely=0, anchor=NW)

        # BOOK NAME
        bookNameFont = tkFont.Font(family='product sans', size=18)
        bookName = tkinter.Label(
            f1, text=j[0], bg="white", width=1000, borderwidth=0, font=bookNameFont, anchor='w')
        bookName.place(rely=0, relx=0.134+0.05)

        # AUTHOR NAME
        authorFont = tkFont.Font(family='product sans', size=16)
        author = tkinter.Label(f1, text=j[2], bg="white", justify=RIGHT,
                               fg='#797979', width=60, borderwidth=0, font=authorFont, anchor='w')
        author.place(rely=0.23, relx=0.134+0.05)

        # RATING
        ratingFont = tkFont.Font(family='psroduct ans', size=18)
        rating = tkinter.Label(f1, image=star, justify=RIGHT, fg="#2ED334",
                               bg="white", width=j[3]*(200//5), borderwidth=0, font=ratingFont, anchor='w')
        rating.image = star
        rating.place(rely=0.9, anchor=SW, relx=0.134+0.05)

        # FAV BUTTON
        buttonFont = tkFont.Font(family='Orbitron', size=12)
        request = tkinter.Button(f1, text="FAV BOOK", font=buttonFont, justify=RIGHT, bg="orange", activebackground="#FFA500",
                                 anchor='c', width=15, cursor='hand2', command=lambda x=i: markFav_module.markFav(x, ls, curr, connection, username))
        request.place(rely=0.6, relx=0.9+0.05, anchor=SE)

        # REQUEST BUTTON
        buttonFont = tkFont.Font(family='Orbitron', size=12)
        request = tkinter.Button(f1, text="REQUEST BOOK", font=buttonFont, justify=RIGHT,
                                 bg="orange", activebackground="#FFA500", anchor='c', width=15, cursor='hand2', command=lambda x=i: makeRequest_module.reuqestBook(x, ls, curr, connection, username))
        request.place(rely=0.9, relx=0.9+0.05, anchor=SE)

        # NEWLINE
        t.window_create(END, window=f1)
        t.insert(END, '\n')

    t.configure(state="disabled")
    t.pack(side=TOP, fill=X)

    h.config(command=t.xview)
    v.config(command=t.yview)
