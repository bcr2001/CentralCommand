from tkinter import *



def mainTkinterWindow():

    myMainWindow = Tk()
    myMainWindow.title("INFO")
    myMainWindow.iconphoto(True, PhotoImage(file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\password.png"))
    myMainWindow.config(bg="Black")
    myMainWindow.geometry("650x450")



    # Image positioning
    welcomeImage = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\welcomeResized.png")
    image_Label = Label(image=welcomeImage,bg="black")
    image_Label.pack()

    # Secret Username frame, Image,labal and entry

    userName_frame = Frame(myMainWindow,bg="black")
    userName_frame.place(x=0,y=150)
    secretImage = PhotoImage(file=("C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\secretResized.png")) #Image object
    userName_label = Label(userName_frame, text="Secret Username", font=(
        "Century Schoolbook", 18, "bold"), image=secretImage, compound=RIGHT, bg="black", fg="white")
    userName_label.pack(padx=20,side=LEFT) #label and it's image

    userName_entry = Entry(userName_frame, font=("Century Schoolbook",18))
    userName_entry.pack(side=RIGHT) #entry box


    # Passwordframe, Image,labal and entry

    

    password_frame = Frame(myMainWindow,bg="black")
    password_frame.place(x=0,y=250)
    passwordImage = PhotoImage(file=("C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\passwordResized.png")) #Image object
    password_label = Label(password_frame, text="Password", font=(
        "Century Schoolbook", 18, "bold"), image = passwordImage, compound=RIGHT, bg="black", fg="white")
    password_label.pack(padx=20,side=LEFT) #label and it's image

    message = Label(password_frame, text="(Password Encryption Activated)",font=("Arial",10,"bold"),fg="green",bg="black")
    message.pack(side=BOTTOM)

    password_entry = Entry(password_frame, font=("Century Schoolbook",18),show="*")
    password_entry.pack(side=RIGHT) #entry box


    #log in button and it's image 

    logIn_image = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\doorResized.png")

    logIn_Button = Button(myMainWindow,text="log in",font=("Tahoma"),bg="black",fg="white",image=logIn_image,compound=RIGHT,borderwidth=0,activebackground="black",activeforeground="white",cursor="hand2")
    logIn_Button.place(x=350,y=350)

    


    myMainWindow.resizable(False,False)
    myMainWindow.mainloop()


if __name__ == "__main__":
    mainTkinterWindow()
