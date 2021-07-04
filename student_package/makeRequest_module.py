from tkinter import messagebox
# 'X' HERE IS THE SERIAL NUMBER WITHIN THE LIST
from urllib.request import urlopen


def reuqestBook(x, ls, curr, connection, username):
    print("hi",username)
    # GETTING DATE ONLINE
    timeInfo = urlopen('http://just-the-time.appspot.com/')
    dateToday = timeInfo.read().strip()
    dateToday = dateToday.decode(
        'utf-8').split()[0].replace('-', '/')  # STORED DATE

    print("datetoday : ", dateToday)
    bid = ls[x][1]
    print("bid : ", bid)

    # GETTING SUB_BID
    querry2 = '''SELECT *  FROM SubBook where (is_available = "yes" and bid = {bid:})'''
    curr.execute(querry2.format(bid=bid))
    connection.commit()
    list2 = curr.fetchall()

    # Checking if book copy is AVAILABLE or NOT
    if len(list2) < 1:
        # popup "Book copy currently not available"
        def bNOTAvail():
            messagebox.showinfo("Book copy currently not available")
        bNOTAvail()

        # PROCESSING REUQEST
    else:
        sub_bid = list2[0][1]  # GETTING THE LEAST SUB_BID
        querr3 = '''INSERT book_request(sub_bid, student_regno, date) values({sub_bid}, \"{username}\", \"{date}\");'''
        curr.execute(querr3.format(sub_bid=sub_bid,
                                   username=username, date=dateToday))
        connection.commit()

        def succ():  # SUCCESS POPUP
            messagebox.showinfo(
                "Request sent successfully"," You can collect the book once your request is accepted by the librarian")
        succ()
