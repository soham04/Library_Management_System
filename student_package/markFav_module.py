def markFav(x, ls, curr, connection, username):
    bid = ls[x][1]
    querry2 = '''SELECT *  FROM SubBook where (is_available = "yes" and bid = {bid:})'''
    curr.execute(querry2.format(bid=bid))
    connection.commit()
    list2 = list(curr.fetchall())
    print(list2)
    # sub_bid = list2[0][1]  # GETTING THE LEAST SUB_BID
    querry = '''insert into favorite_book values({bid},'{username}')'''
    curr.execute(querry.format(bid=bid, username=username))
    connection.commit()
