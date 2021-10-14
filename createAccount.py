
from tkinter import *
from tkinter import font




class CreateAccountWindowCreator:
    def __init__(self,master):
        self.master = master
        self.frame1 = Frame(self.master)

    # this frame holds the label and entry field for the username
        self.frame1.grid(row=1,column=1,pady=20,padx=10)

        self.user_name_label = Label(
            self.frame1,
            text="Username",
            font=("Arial",12,"bold"),
        )

        self.user_name_label.pack(side=LEFT)
        self.username = Entry(self.frame1,font=("Arial",12))
        self.username.pack(side=RIGHT)

    # this frame hold the label and entry field for password
        self.frame2 = Frame(self.master)
        self.frame2.grid(row=1,column=2,padx=55)

        self.password_label = Label(
            self.frame2,
            text="Password",
            font=("Arial",12,"bold"))
        self.password_label.pack(side=LEFT)

        self.password_entry = Entry(self.frame2,font=("Arial",12),show="*")
        self.password_entry.pack(side=LEFT)
    
    # this frame holds the label and entry field for first name
        self.frame3 = Frame(self.master)
        self.frame3.grid(row=2, column=1, pady=20, padx=10)

        self.fname_label = Label(
            self.frame3,
            text="First Name",
            font=("Arial",12,"bold"))
        self.fname_label.pack(side=LEFT)

        self.fname_entry = Entry(
            self.frame3,
            font=("Arial",12))
        self.fname_entry.pack(side=RIGHT)

    #this frame holds the label and entry field for middle name 
        self.frame4 = Frame(self.master)
        self.frame4.grid(row=2, column=2,pady=20, padx=10)

        self.middle_label = Label(
            self.frame4,text="Middle Name",
            font=("Arial", 12, "bold"))
        self.middle_label.pack(side=LEFT)

        self.middle_entry = Entry(
            self.frame4,
            font=("Arial",12))
        self.middle_entry.pack(side=RIGHT)
    
    #this frame holds the label and entry field for last name
        self.frame5 = Frame(self.master)
        self.frame5.grid(row=3, column=1, pady=20, padx=10)

        self.last_label = Label(
            self.frame5,
            text="Last Name",
            font=("Arial",12,"bold"))
        self.last_label.pack(side=LEFT)

        self.last_entry = Entry(
            self.frame5,
            font=("Arial",12))
        self.last_entry.pack(side=RIGHT)
    
    # this is the frame that holds the label and entry field for Phone Number
        self.frame6 = Frame(self.master)
        self.frame6.grid(row=3,column=2,padx=10,pady=20)

        self.phone_label = Label(
            self.frame6,
            text="Phone Number",
            font = ("Arial",12,"bold"))
        self.phone_label.pack(side=LEFT)

        self.phone_entry = Entry(
            self.frame6,
            font = ("Arial",12))
        self.phone_entry.pack(side=RIGHT)

    # this is the frame that holds the label and entry field for Phone Number
        self.frame7 = Frame(self.master)
        self.frame7.grid(row=4,column=1,padx=10,pady=20)

        self.phone_label = Label(
            self.frame7,
            text="ID Number",
            font = ("Arial",12,"bold"))
        self.phone_label.pack(side=LEFT)

        self.phone_entry = Entry(
            self.frame7,
            font = ("Arial",12))
        self.phone_entry.pack(side=RIGHT)

    # this is the frame that holds the label and entry field for id number
        self.frame7 = Frame(self.master)
        self.frame7.grid(row=4,column=1,padx=10,pady=20)

        self.id_label = Label(
            self.frame7,
            text="ID Number",
            font = ("Arial",12,"bold"))
        self.id_label.pack(side=LEFT)

        self.id_entry = Entry(
            self.frame7,
            font = ("Arial",12))
        self.id_entry.pack(side=RIGHT)

    # this is the frame that holds the label and entry field for kra pin
        self.frame8 = Frame(self.master)
        self.frame8.grid(row=4,column=2,padx=10,pady=20)

        self.kra_label = Label(
            self.frame8,
            text="KRA pin",
            font = ("Arial",12,"bold"))
        self.kra_label.pack(side=LEFT)

        self.kra_entry = Entry(
            self.frame8,
            font = ("Arial",12))
        self.kra_entry.pack(side=RIGHT, padx=10)

    # this is the frame that holds the label and entry field for email
        self.frame9 = Frame(self.master)
        self.frame9.grid(row=5,column=1,padx=10,pady=20)

        self.email_label = Label(
            self.frame9,
            text="Email",
            font = ("Arial",12,"bold"))
        self.email_label.pack(side=LEFT)

        self.email_entry = Entry(
            self.frame9,
            font = ("Arial",12))
        self.email_entry.pack(side=RIGHT,padx=10)

    # this is the frame that contains the button that summits the contents of the above form and finalizes creating an accoout 
        self.frame10 = Frame(self.master)
        self.frame10.place(x=450, y=350)

        self.create_account_button = Button(
            self.frame10,
            text="Create",
            font=("Arial",12,"bold"),
            cursor="hand2",
            borderwidth=0,
            command=self.submission_function_handler)

        self.create_account_button.pack()

    def submission_function_handler(self):
        print("I just happened and worked")



# def run_me():

#     createAccountWindow = Tk()
#     myapp = WindowCreator(createAccountWindow)
#     createAccountWindow.geometry("650x450")
#     createAccountWindow.title("Create Window")
#     myapp.submission_function_handler()
#     createAccountWindow.resizable(False, False)
#     createAccountWindow.mainloop()

# run_me()
