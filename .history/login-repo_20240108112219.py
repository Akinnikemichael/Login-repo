import re

#database = {"Michael" :  "12345",  "Tobi": "5667"}


username = input("what is your username? ")
email = input("what is your email?  ")
password = input("what is your password? ")
Confirm_password = input("confirm your password")
def signup():
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):

     #return True
     #return False

     if (len(password) <= 8) and password == Confirm_password:
        print("valid password")
     elif (len(password) > 8) and password != Confirm_password:
        print("invalid password")
       # database.append = ([username, password])
        #print(database)

signup()