from login import Login

lg = Login()

username = lg.getUsername()
password = lg.getPassword()
userType = lg.getUserType()

del lg

if userType:
    pass # admin
else:
    pass # student