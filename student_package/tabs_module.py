import tkinter
from tkinter import font as tkFont, N

from student_package import search_module, fine_module, request_modules, mybooks_module, history_module, home_module


def tabs(tabF, bottomF, connection, curr, regno):
    # Functional buttons ----------------------------------------------

    btFont = tkFont.Font(family='product sans', size=15, weight=tkFont.BOLD)
    home_bt = tkinter.Button(tabF, highlightthickness=0, justify="center", activebackground='#356AC3',
                             activeforeground="white", bd=2, cursor='hand2',
                             text='HOME', width=10, foreground='white', background='#4285F4', font=btFont,
                             command=lambda: home_module.home(bottomF, curr, connection, regno))
    home_bt.place(relx=0.14285714, rely=0.1, anchor=N)
    # home_bt.grid(column = 1)

    # btFont = tkFont.Font(family='product sans', size=15, weight=tkFont.BOLD)
    library_bt = tkinter.Button(tabF, highlightthickness=0, justify="center", activebackground='#356AC3',
                                activeforeground="white", bd=2, cursor='hand2',
                                text='SEARCH', width=10, foreground='white', background='#4285F4', font=btFont,
                                command=lambda: search_module.search(bottomF, connection, curr, regno))
    library_bt.place(relx=0.14285714 * 2, rely=0.1, anchor=N)

    fines_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white",
                              cursor='hand2',
                              text='FINES', width=10, foreground='white', background='#4285F4', font=btFont,
                              command=lambda: fine_module.fine(bottomF, curr, regno))
    fines_bt.place(relx=0.14285714 * 3, rely=0.1, anchor=N)

    history_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2,
                                cursor='hand2',
                                text='HISTORY', width=10, foreground='white', background='#4285F4', font=btFont,
                                command=lambda: history_module.history(bottomF, regno, curr))
    history_bt.place(relx=0.14285714 * 4, rely=0.1, anchor=N)

    request_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2,
                                cursor='hand2',
                                text='REQUESTS', width=10, foreground='white', background='#4285F4', font=btFont,
                                command=lambda: request_modules.display_book_reuqests(bottomF, regno, curr, connection))
    request_bt.place(relx=0.14285714 * 5, rely=0.1, anchor=N)

    mybooks_bt = tkinter.Button(tabF, justify="center", activebackground='#356AC3', activeforeground="white", bd=2,
                                cursor='hand2',
                                text='MY BOOKS', width=10, foreground='white', background='#4285F4', font=btFont,
                                command=lambda: mybooks_module.mybooks(bottomF, curr, regno, connection))
    mybooks_bt.place(relx=0.14285714 * 6, rely=0.1, anchor=N)
