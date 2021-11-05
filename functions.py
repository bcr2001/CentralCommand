from tkinter import *
from tkinter import messagebox


# This fucntion is executed if the username and password are correct
def popuperrorHandler():
    # messagebox.askretrycancel(title="Error",message="entry boxes cannot be left empty!!!")
    messagebox.showerror(
        title="Entry box error", message="entry box cannot be left empty!!!")


def wrongUserName_Password():
    messagebox.showinfo(title="Authentication Error",
                        message="your username or password is wrong")


#this function is validates emails using regular expressions and return True if email is valid otherwise it returns False
def email_valid_checker(email):
    import re
    patterMatcher = re.compile(r"\b[a-z].+@[a-z]+\.[a-z]{2,}\b")
    mi = re.search(patterMatcher, email)
    if mi:
        return True
    else:
        return False



def something_is_wrong():
    #this message box will bob up if the user clicks the create buttons and his form contains errors
    messagebox.showerror(title="Invalid Input", message="Invalid data or some entry fields are empty")

def successful_creation():
    #this message box informs the user that their account has been suceessfully created
    messagebox.showinfo(title="Account Created",message="Your account has been successfully created\nthis window will be closed. Please Log In after the closure")


#this function checks whether an phone number is valid or not using regular expression.
#if the phone number is valid then it returns True else False.
def phoneNo_valid_checker(phoneNumber):
    import re
    patternMatcher = re.compile(r"^0(7(?:(?:[129][0-9])|(?: 0[0-8])|(4[0-1]))[0-9]{6})$")
    mi = re.search(patternMatcher,phoneNumber)
    if mi:
        return True 
    else:
        return False