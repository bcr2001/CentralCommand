
from tkinter import *
from database import data_sql_adder
from functions import email_valid_checker, successful_creation
from functions import something_is_wrong



class CreateAccountWindowCreator:
    def __init__(self, master):
        self.master = master

# this frame holds the label and entry field for the username

        self.MainFrame1 = Frame(self.master)
        self.MainFrame1.place(x=10,y=10)

        self.frame1 = Frame(self.MainFrame1)
        self.frame1.pack(side=RIGHT, padx=15)

        self.user_name_label = Label(
            self.MainFrame1,
            text="Username",
            font=("Arial", 12, "bold"),
        )
        self.user_name_label.place(x=0, y=0)

        self.error_display = StringVar

        self.username_entry = Entry(self.frame1, font=(
            "Arial", 12), textvariable=self.error_display)
        self.username_entry.focus()
        self.username_entry.pack(padx=90)

        self.error_display_label = Label(
            self.frame1, font=("Arial", 8, "bold"), fg="red")
        self.error_display_label.pack(side=BOTTOM)


    # this frame hold the label and entry field for password

        self.MainFrame2 = Frame(self.master)
        self.MainFrame2.place(x=350,y=10)

        self.frame2 = Frame(self.MainFrame2)
        self.frame2.pack(side=RIGHT,padx=15)


        self.password_label = Label(
            self.MainFrame2,
            text="Password",
            font=("Arial",12,"bold"))
        self.password_label.place(x=0,y=0)

        #the below contantains the password entry field attached to its StringVar
        self.password_entry_error = StringVar()

        self.password_entry = Entry(self.frame2, font=("Arial", 12), show="*",textvariable=self.password_entry_error)
        self.password_entry.focus()
        self.password_entry.pack(padx=90)
        
        #the below block contains the label to be displayed when the user commits some kind of error.
        self.password_entry_label = Label(
            self.frame2, font=("Arial", 8, "bold"), fg="red")
        self.password_entry_label.pack(side=BOTTOM)


    # this frame hold the label and entry field for first name

        self.MainFrame3 = Frame(self.master)
        self.MainFrame3.place(x=10, y=70)

        self.frame3 = Frame(self.MainFrame3)
        self.frame3.pack(side=RIGHT, padx=15)

        self.first_name = Label(
            self.MainFrame3,
            text="First Name",
            font=("Arial", 12, "bold"))
        self.first_name.place(x=0, y=0)

        #the below contantains the password entry field attached to its StringVar
        self.first_name_error = StringVar()

        self.firstName_entry = Entry(self.frame3, font=(
            "Arial", 12), textvariable=self.first_name_error)
        self.firstName_entry.focus()
        self.firstName_entry.pack(padx=90)

        #the below block contains the label to be displayed when the user commits some kind of error.
        self.firstName_entry_label = Label(
            self.frame3, font=("Arial", 8, "bold"), fg="red")
        self.firstName_entry_label.pack(side=BOTTOM)


#this frame holds the label and entry field for middle name
        self.MainFrame4 = Frame(self.master)
        self.MainFrame4.place(x=350,y = 70)


        self.frame4 = Frame(self.MainFrame4)
        self.frame4.pack(side=RIGHT, padx=15)

        self.middle_label = Label(
            self.MainFrame4,text="Middle Name",
            font=("Arial", 12, "bold"))
        self.middle_label.place(x=0, y=0)


        self.middle_entry = Entry(
            self.frame4,
            font=("Arial",12))
        self.middle_entry.focus()
        self.middle_entry.pack(padx=90)

        #this is a label is used for validation and informing the user that the middle name is an optional field
        self.optional_label = Label(self.frame4,text="(this field is optional)",font=("Arial",10,"bold",),fg="green")
        self.optional_label.pack(side=BOTTOM)

   # this frame hold the label and entry field for last name

        self.MainFrame5 = Frame(self.master)
        self.MainFrame5.place(x=10, y=140)

        self.frame5 = Frame(self.MainFrame5)
        self.frame5.pack(side=RIGHT, padx=15)

        self.last_name = Label(
            self.MainFrame5,
            text="Last Name",
            font=("Arial", 12, "bold"))
        self.last_name.place(x=0, y=0)

       
        self.last_name_error = StringVar()

        self.lastName_entry = Entry(self.frame5, font=(
            "Arial", 12), textvariable=self.last_name_error)
        self.lastName_entry.focus()
        self.lastName_entry.pack(padx=90)

       
        self.lastName_entry_label = Label(
            self.frame5, font=("Arial", 8, "bold"), fg="red")
        self.lastName_entry_label.pack(side=BOTTOM)

#     # this is the frame that holds the label and entry field for Phone Number
        self.MainFrame6 = Frame(self.master)
        self.MainFrame6.place(x=350, y=140)

        self.frame6 = Frame(self.MainFrame6)
        self.frame6.pack(side=RIGHT, padx=15)

        self.phone_label = Label(
            self.MainFrame6, text="Phone No",
            font=("Arial", 12, "bold"))
        self.phone_label.place(x=0, y=0)

        self.phone_error_label = StringVar()

        self.phone_entry = Entry(
            self.frame6,
            font=("Arial", 12),textvariable=self.phone_error_label)
        self.phone_entry.focus()
        self.phone_entry.pack(padx=95)


        self.phone_entry_label = Label(
            self.frame6, font=("Arial", 8, "bold"), fg="red")
        self.phone_entry_label.pack(side=BOTTOM)


#     # this is the frame that holds the label and entry field for email
        self.MainFrame7 = Frame(self.master)
        self.MainFrame7.place(x=10, y=210)

        self.frame7 = Frame(self.MainFrame7)
        self.frame7.pack(side=RIGHT, padx=15)

        self.email = Label(
            self.MainFrame7,
            text="Email",
            font=("Arial", 12, "bold"))
        self.email.place(x=0, y=0)

        self.email_error = StringVar()

        self.email_entry = Entry(self.frame7, font=(
            "Arial", 12), textvariable=self.email_error)
        self.email_entry.focus()
        self.email_entry.pack(padx=90)

        self.email_entry_label = Label(
        self.frame7, font=("Arial", 8, "bold"), fg="red")
        self.email_entry_label.pack(side=BOTTOM)

    # this is the frame that contains the button that summits the contents of the above form and finalizes creating an accoout
        self.frame10 = Frame(self.master)
        self.frame10.place(x=450, y=350)

        self.create_account_button = Button(
            self.frame10,
            text="Create",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            borderwidth=0,
            command=self.submission_function_handler)

        self.create_account_button.pack()




#this function is called when the create button is clicked and also handles the validation of the data provided for by the user
    def submission_function_handler(self):
        from functions import phoneNo_valid_checker
        #using the .get function, the data provided by the user is assigned to a variable
        username_get = self.username_entry.get().rstrip()
        password_get = self.password_entry.get().rstrip()
        firstname_get = self.firstName_entry.get().rstrip()
        middle_get = self.middle_entry.get().rstrip()
        last_get = self.lastName_entry.get().rstrip()
        phone_get = self.phone_entry.get().rstrip()
        email_get = self.email_entry.get().rstrip()


        empty = "" #empty string 
        counter = 0 # 1 means that their is an error while 0 means that everthing is okay
        
        email_valid_results = email_valid_checker(email_get) #this variable hold the return result of the email_valid_checker function in the functions.py file 

        # this variable will hold the results obtained from the phoneNo_valid_checker found in the function.py file
        phone_number_valid = phoneNo_valid_checker(phone_get)


# validation code
        try:
            #username validation checker
            if username_get == empty:
                self.error_display_label.config(
                    text="username cannot be left empty")
                counter = 1
            if username_get != empty and (counter == 0):
                self.error_display_label.config(text=" ")
                counter = 0

            #password validation checker
            if password_get == empty:
                self.password_entry_label.config(text="Password cannot be left empty")
                counter = 1
            if password_get != empty and (counter == 0):
                self.password_entry_label.config(text=" ")
                counter = 0
                
            
            #firstName validator checker
            if firstname_get == empty:
                self.firstName_entry_label.config(text="first name cannot be empty")
                counter = 1
            if firstname_get != empty and (counter == 0):
                self.firstName_entry_label.config(text=" ")
                counter = 0


            #lastName validator checker
            if last_get == empty:
                self.lastName_entry_label.config(text="last name cannot be empty")
                counter = 1
            if last_get != empty and (counter == 0):
                self.lastName_entry_label.config(text=" ")
                counter = 0


            #phone number validator checker   
            if phone_number_valid == False or (phone_get == empty):
                self.phone_entry_label.config(text="Invalid Phone Number")
                counter = 1
            if phone_number_valid == True and (counter==0):
                self.phone_entry_label.config(text=" ")
                counter = 0


            #Email validator checker
            if email_get == empty or (email_valid_results == False):
                self.email_entry_label.config(text="Invalid Email Address")
                counter = 1
            if email_valid_results == True and (counter==0):
                self.email_entry_label.config(text=" ")
        except:
            print("Oops! Something when wrong")
        


    #the below blocks of code check whether the counter is 0 or 1 
    # if it's 1 the the program cannot continue because the user has entered incorrect data into the entry field
    # if it's 0 the the programm continuous 
        try:
            if counter == 1:
                something_is_wrong()
                print(f"The counter is {counter} hence things are not okay")
            elif counter==0:
                successful_creation()
                
                data_sql_adder(username_get,password_get,firstname_get,middle_get,last_get,phone_get,email_get)
                # self.master.destroy()
        except:
            print("Oops! Something when wrong")



# def run_me():

#     createAccountWindow = Tk()
#     myapp = CreateAccountWindowCreator(createAccountWindow)
#     createAccountWindow.geometry("650x450")
#     createAccountWindow.title("Create Window")

#     createAccountWindow.resizable(False, False)
#     createAccountWindow.mainloop()


# run_me()
