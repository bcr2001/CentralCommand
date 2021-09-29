from tkinter import *
import time
from tkinter import messagebox



# This fucntion is executed if the username and password are correct

def popuperrorHandler():
    # messagebox.askretrycancel(title="Error",message="entry boxes cannot be left empty!!!")
    messagebox.showerror(
        title="Entry box error", message="entry box cannot be left empty!!!")

def wrongUserName_Password():
    messagebox.showinfo(title="Authentication Error",message="your username or password is wrong")
    



def time_function():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    date_string = time.strftime("%A")
    date_label.config(text=date_string)


    myCommandWindow.after(1000,time_function)
    


def commandWindow():
    global authentication_image


    global myCommandWindow
    myCommandWindow = Toplevel()

    global time_label
    time_label = Label(myCommandWindow,bg="black",fg="green",font=("Arial",15,"bold"))
    time_label.place(x=0,y=0)

    global date_label
    date_label = Label(myCommandWindow,bg="black",fg="green",font=("Arial",15,"bold"))
    date_label.place(x=530,y=0)

    
    myCommandWindow.title("Central Command")
    myCommandWindow.geometry("650x450")
    myCommandWindow.config(bg="black")
    myCommandWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\password.png"))

    authentication_image = PhotoImage(file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\checkmeResized.png")
    authentication_label = Label(myCommandWindow,text="Welcome To the Authentication Window",font=("Dubai",20),image=authentication_image,compound=LEFT,fg="white",bg="black")
    authentication_label.place(x=35,y=50)

    time_function()



    myCommandWindow.resizable(False,False)
    myCommandWindow.mainloop()

x = 0 
def logInHandler1(event):
        global x
        x+=1

        # getting entry field data
        entered_username = userName_entry.get()
        entered_password = password_entry.get()

        infoFileOpener = open(
            "C:\\Users\\Hx101X\\Desktop\\informationFile\\user1.txt", "r")
        readInfo = infoFileOpener.read()
        infoList = readInfo.split(",")
        realUserName = infoList[0]
        realpassword = infoList[1]

        empty = ""

        if (entered_username.lstrip()== empty) or (entered_password == empty):
            popuperrorHandler()
           
        elif (entered_username != realUserName or entered_password != realpassword):
            # rejection()
            wrongUserName_Password()
            
        elif (entered_username == realUserName and entered_password == realpassword):
            commandWindow()
        
        if x==3:
            myMainWindow.destroy()
      
def logInHandler():
        global x
        x+=1

        # getting entry field data
        entered_username = userName_entry.get()
        entered_password = password_entry.get()

        infoFileOpener = open(
            "C:\\Users\\Hx101X\\Desktop\\informationFile\\user1.txt", "r")
        readInfo = infoFileOpener.read()
        infoList = readInfo.split(",")
        realUserName = infoList[0]
        realpassword = infoList[1]

        empty = ""

        if (entered_username.lstrip()== empty) or (entered_password == empty):
            popuperrorHandler()
           
        elif (entered_username != realUserName or entered_password != realpassword):
            # rejection()
            wrongUserName_Password()
            
        elif (entered_username == realUserName and entered_password == realpassword):
            commandWindow()
        
        if x==3:
            myMainWindow.destroy()
      
     


def mainTkinterWindow():
    global myMainWindow
   

    myMainWindow = Tk()
    myMainWindow.title("INFO")
    myMainWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\lockResized.png"))
    myMainWindow.config(bg="Black")
    myMainWindow.geometry("650x450")

    # Image positioning
    welcomeImage = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\welcomeResized.png")
    image_Label = Label(image=welcomeImage, bg="black")
    image_Label.pack()

    # Secret Username frame, Image,labal and entry

    userName_frame = Frame(myMainWindow, bg="black")
    userName_frame.place(x=0, y=150)
    secretImage = PhotoImage(file=(
        "C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\secretResized.png"))  # Image object
    userName_label = Label(userName_frame, text="Secret Username", font=(
        "Century Schoolbook", 18, "bold"), image=secretImage, compound=RIGHT, bg="black", fg="white")
    userName_label.pack(padx=20, side=LEFT)  # label and it's image
    global userName_entry
    userName_entry = Entry(userName_frame, font=("Century Schoolbook", 18))
    userName_entry.pack(side=RIGHT)  # entry box

    # Passwordframe, Image,labal and entry

    password_frame = Frame(myMainWindow, bg="black")
    password_frame.place(x=0, y=250)
    passwordImage = PhotoImage(file=(
        "C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\passwordResized.png"))  # Image object
    password_label = Label(password_frame, text="Password", font=(
        "Century Schoolbook", 18, "bold"), image=passwordImage, compound=RIGHT, bg="black", fg="white")
    password_label.pack(padx=20, side=LEFT)  # label and it's image

    message = Label(password_frame, text="(Password Encryption Activated)", font=(
        "Arial", 10, "bold"), fg="green", bg="black")
    message.pack(side=BOTTOM)

    global password_entry
    password_entry = Entry(password_frame, font=(
        "Century Schoolbook", 18), show="*")
    password_entry.pack(side=RIGHT)  # entry box

    # log in button and it's image

    logIn_image = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\doorResized.png")

    logIn_Button = Button(myMainWindow, text="log in", font=("Tahoma"), bg="black", fg="white", image=logIn_image, compound=RIGHT,
                          borderwidth=0, activebackground="black", activeforeground="white", cursor="hand2", command=logInHandler)
    logIn_Button.place(x=350, y=350)


    myMainWindow.bind("<Return>",logInHandler1)

    myMainWindow.resizable(False, False)
    myMainWindow.mainloop()


if __name__ == "__main__":
    mainTkinterWindow()
