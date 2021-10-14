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
