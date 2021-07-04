import pathlib
from io import BytesIO
from tkinter import *
from tkinter import font as tkFont
from tkinter.font import *
from PIL import Image
from PIL import ImageTk

from student_package import makeRequest_module, markFav_module


def displaySearchResult(bottomF, typeq, curr, connection, username, keyW, category):
    x = ""
    print("keyword = ", x, "| keywordlen =", len(x), " | type = ", typeq)

    ls = []

    if typeq == 1:
        x = keyW.get()
        querry1 = '''select * from book where Bname like '%{keyword}%';'''
        curr.execute(querry1.format(keyword=x))
        connection.commit()
    elif typeq == 2:
        x = category.get()
        querry1 = '''select * from book where subject_name = "{subject_name}";'''
        curr.execute(querry1.format(subject_name=x))
        connection.commit()

    ls = list(curr.fetchall())

    numOfRequest = len(ls)

    if numOfRequest == 0:
        filePath = pathlib.Path(__file__).parent.absolute()
        filePath = str(str(filePath) + "\\images\\no.jpg")
        img = ImageTk.PhotoImage(Image.open(
            filePath).resize((1000, 350), Image.ANTIALIAS))
        noResult = tkinter.Label(bottomF, bg="white", image=img, height=350)
        noResult.image = img
        noResult.place(relx=0, rely=1, relheight=0.7, relwidth=1, anchor=SW)
        return

    # start of list --------------------------------
    listbox = Listbox(bottomF, relief="sunken",
                      font=("courier", 15), bg="red", fg="red", height=20, width=1150)
    listbox.place(relx=0, rely=1, relheight=0.7, relwidth=1, anchor=SW)

    h = Scrollbar(bottomF, orient='horizontal')
    # h.place(relx=0.5, rely=1, anchor=S, relwidth=1)

    v = Scrollbar(bottomF, orient='vertical')
    v.place(relx=1, rely=1, anchor=SE, relheight=0.7)

    t = Text(listbox, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)

    # temporary Image object
    filePath = pathlib.Path(__file__).parent.absolute()
    filePath = str(str(filePath) + "\\images\\peng.jpg")
    img = ImageTk.PhotoImage(Image.open(
        filePath).resize((120, 150), Image.ANTIALIAS))

    # STARS IMAGE
    filePath = pathlib.Path(__file__).parent.absolute()
    filePath = str(str(filePath) + "\\images\\stars.png")
    star = ImageTk.PhotoImage(Image.open(
        filePath).resize((200, 30), Image.ANTIALIAS))

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
        thumbNail.place(relx=0 + 0.05, rely=0, anchor=NW)

        # BOOK NAME
        bookNameFont = tkFont.Font(family='product sans', size=18)
        bookName = tkinter.Label(
            f1, text=j[0], bg="white", width=1000, borderwidth=0, font=bookNameFont, anchor='w')
        bookName.place(rely=0, relx=0.134 + 0.05)

        # AUTHOR NAME
        authorFont = tkFont.Font(family='product sans', size=16)
        author = tkinter.Label(f1, text=j[2], bg="white", justify=RIGHT,
                               fg='#797979', width=60, borderwidth=0, font=authorFont, anchor='w')
        author.place(rely=0.23, relx=0.134 + 0.05)

        # RATING
        ratingFont = tkFont.Font(family='psroduct ans', size=18)
        rating = tkinter.Label(f1, image=star, justify=RIGHT, fg="#2ED334",
                               bg="white", width=j[3] * (200 // 5), borderwidth=0, font=ratingFont, anchor='w')
        rating.image = star
        rating.place(rely=0.9, anchor=SW, relx=0.134 + 0.05)

        # FAV BUTTON
        buttonFont = tkFont.Font(family='Orbitron', size=12)
        request = tkinter.Button(f1, text="FAV BOOK", font=buttonFont, justify=RIGHT, bg="orange",
                                 activebackground="#FFA500",
                                 anchor='c', width=15, cursor='hand2',
                                 command=lambda x=i: markFav_module.markFav(x, ls, curr, connection, username))
        request.place(rely=0.6, relx=0.9 + 0.05, anchor=SE)

        # REQUEST BUTTON
        buttonFont = tkFont.Font(family='Orbitron', size=12)
        request = tkinter.Button(f1, text="REQUEST BOOK", font=buttonFont, justify=RIGHT,
                                 bg="orange", activebackground="#FFA500", anchor='c', width=15, cursor='hand2',
                                 command=lambda x=i: makeRequest_module.reuqestBook(x, ls, curr, connection, username))
        request.place(rely=0.9, relx=0.9 + 0.05, anchor=SE, )

        # NEWLINE
        t.window_create(END, window=f1)
        t.insert(END, '\n')

    t.configure(state="disabled")
    t.pack(side=TOP, fill=X)

    h.config(command=t.xview)
    v.config(command=t.yview)


def search(bottomF, connection, curr, username):
    for widget in bottomF.winfo_children():
        widget.destroy()

    # SEARCH LOGO
    # filePath = pathlib.Path(__file__).parent.absolute()
    # filePath = str(str(filePath)+"\\images\\search.png")
    # img = ImageTk.PhotoImage(Image.open(
    #     filePath).resize((150, 150), Image.ANTIALIAS))
    # img = ImageTk.PhotoImage(Image.open(
    # r"C:\Users\Admin\Downloads\fol\fol\search.png").resize((150, 150), Image.ANTIALIAS))

    # tImage = tkinter.Label(bottomF, relief='flat',
    #                        width=150, image=img, height=150)
    # tImage.image = img
    # tImage.place(rely=0, relx=0, anchor=NW)

    # LABEL "KEYWORD"
    titleFont = tkFont.Font(family='product sans', size=18)
    selectS = tkinter.Label(bottomF, text='Keywords : ', bg="light yellow",
                            width=20, borderwidth=0, font=titleFont, anchor='e', )
    selectS.place(relx=0.14, rely=0)

    # LABEL "SELECT STREAM"
    titleFont = tkFont.Font(family='product sans', size=18)
    selectS = tkinter.Label(bottomF, text='Select Stream : ', bg="light yellow", width=20,
                            borderwidth=0, font=titleFont, anchor='e')
    selectS.place(relx=0.14, rely=0.1)

    # KEYWORD ENTRY BOX
    entryFont = tkFont.Font(family='product sans', size=15)
    keyW = tkinter.Entry(bottomF, font=entryFont, text="gg", width=38)
    keyW.place(relx=0.4, rely=0)

    # BUTTON "SEARCH"
    submitFont = tkFont.Font(family='product sans', size=10, weight=BOLD)
    submit_btn = Button(bottomF, text="SEARCH", bg='Orange', width=15,
                        fg='white', font=submitFont, cursor='hand2',
                        command=lambda: displaySearchResult(bottomF, 1, curr, connection, username, keyW, category))
    submit_btn.place(relx=0.97, anchor=NE, rely=0)

    # DROP DOWN
    dropDownFont = tkFont.Font(family='product sans', size=15)
    category = tkinter.ttk.Combobox(bottomF, width=38, state="readonly", font=dropDownFont)
    curr.execute('''select distinct subject_name from book''')
    connection.commit()
    category['values'] = list(curr.fetchall())

    category.place(relx=0.4, rely=0.1)
    print(category.get())

    # SEARCH BUTTON
    submitFont = tkFont.Font(family='product sans', size=10, weight=BOLD)
    submit_btn = Button(bottomF, text="SEARCH", bg='Orange', width=15,
                        fg='white', font=submitFont, cursor='hand2',
                        command=lambda: displaySearchResult(bottomF, 2, curr, connection, username, keyW, category))
    submit_btn.place(relx=0.97, anchor=E, rely=0.13)

# search(bottomF, connection, curr)
