
from tkinter import *
from tkinter import ttk
from database import retrive_users_data


number_of_clicks = 0
y_place = 100


class CommandWindow:

    def __init__(self, master, username):
        self.master = master

        self.master.iconphoto(False, PhotoImage(
            file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\password.png"))


        # giving the master geometry and screen position to oen
        w = 650
        h = 450

        width_screen = self.master.winfo_screenwidth()
        heigh_screen = self.master.winfo_screenheight()

        x = (width_screen/2) - (w/2)
        y = (heigh_screen/2) - (h/2)
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.master.resizable(False, False)

        self.username = username

    # Creating Main Frame
        self.main_frame = Frame(self.master)
        self.main_frame.pack(fill=BOTH, expand=1)

    # Create a canvas
        self.my_canvas = Canvas(
            self.main_frame, bg="black", highlightcolor="black", borderwidth=0)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # adding a scroll bar to the canvas
        self.my_scrollbar = ttk.Scrollbar(self.main_frame,
                                          orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configuring the Canvas
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind("<Configure>", lambda e: self.my_canvas.configure(
            scrollregion=self.my_canvas.bbox("all")))

    # Creating another frame inside the canvas
        self.my_frame_2 = Frame(self.my_canvas, bg="black")

    # Adding the new frame to a window in the canvas
        self.my_canvas.create_window(
            (0, 0), window=self.my_frame_2, anchor="nw")

    # my_frame_2 code
        self.main_frame.config(bg="black")

    def _create_new_field(self):

        # this label diplays the username it the top right corner of the window
        self.username_display_label = Label(self.my_frame_2, text=f"Welcome {self.username}", font=(
            "Arial", 15, "bold"), bg="black", fg="orange")
        self.username_display_label.grid(row=1, column=0)


# this part of the code is the frame that is used to house the input label, the entry/text box and the play button
        # the frame that gonna house all the items
        self.MainFrame_1 = Frame(self.my_frame_2, bg="black")
        self.MainFrame_1.grid(row=2, column=0, pady=15, padx=10)

        # input label
        self.input_label = Label(self.MainFrame_1, text="Input[0]", font=(
            "Arial", 10, "bold"), fg="white", bg="black")
        self.input_label.grid(row=0, column=0, padx=10)

        # text area code
        self.mytext_area = Text(self.MainFrame_1, font=(
            "Arial", 15), height=3, width=35, padx=5, highlightthickness=0.5, highlightcolor="orange")
        self.mytext_area.grid(row=0, column=1)

        # cental disply label which handles the display of the type of information to present to the user.
        self.central_value = StringVar()
        self.central_label = Label(self.my_frame_2,
                                   textvariable=self.central_value, fg="red", bg="black",
                                   font=("Arial", 10, "bold"))
        self.central_label.grid(row=3, column=0)


        # run button code
        self.run_image = PhotoImage(file="Images\\play2Resized.png")

        self.run_button = Button(self.MainFrame_1, image=self.run_image,
                                 borderwidth=0, cursor="hand2", bg="black", activebackground="black",
                                 command=self.run_function_handler)
        self.run_button.grid(row=0, column=2, padx=10)

    #handles the operations that are run when the user clicks the run button
    def run_function_handler(self):
        # this is a list of valid code that can be entered into the text area
        list_of_codes = [f"{self.username}.get_info()",
                         f"{self.username}.get_info(username)", f"{self.username}.get_info(password)", f"{self.username}.get_info(fullname)", f"{self.username}.get_info(phone)", f"{self.username}.get_info(email)"]

        self.text_code = self.mytext_area.get("1.0", END).strip() 

        command_error_display = f"Traceback (most recent entry):\nfield Input[0]\n{self.text_code}\n Command error: {self.text_code}is not a command\ntype help_ to get recommanded/existing commands".rjust(
            10)

        # message displyed if the command is <35 characters in lenght.
        # essentially created because long characters tend por out of the label widget
        length_error_display = f"Traceback (most recent entry): field Input[0] Length error: {self.text_code[0:3]}...\ndoes not satisfy the length requirements\ntype help_ to get recommanded/existing commands"

        if len(self.text_code) > 40:
            self.central_label.config(font=("Arial", 10, "bold"), fg="red")
            self.central_value.set(length_error_display)

        elif self.text_code not in list_of_codes:
            self.central_label.config(font=("Arial", 10, "bold"), fg="red")
            self.central_value.set(command_error_display)

        elif self.text_code == f"{self.username}.get_info()":
            self.general_code_function()

        else:
            self.specific_parameter()

            
    def general_code_function(self):
        self.central_label.config(font=("Arial", 15, "bold"), fg="white")
        data_list = retrive_users_data(self.username)

        peronal_text_format_WM = f"Username: {data_list[0]}\n\nPassword: {data_list[1]}\n\nFull Name: {data_list[2]} {data_list[3]} {data_list[4]}\n\nPhone Number: {data_list[5]}\n\nEmail Address: {data_list[6]}"

        peronal_text_format_WTM = f"Username: {data_list[0]}\nPassword:    {data_list[1]}\nFull Name: {data_list[2]} {data_list[4]}\nPhone Number: {data_list[5]}\nEmail Address: {data_list[6]}"

        if data_list[3] == " ":
            self.central_value.set(peronal_text_format_WTM)
        else:
            self.central_value.set(peronal_text_format_WM)


    def specific_parameter(self):
        data_list_specific = retrive_users_data(self.username)
        self.central_label.config(font=("Arial", 15, "bold"), fg="white")

        if self.text_code == f"{self.username}.get_info(username)":
            self.central_value.set(f"Username: {data_list_specific[0]}")
        elif self.text_code == f"{self.username}.get_info(password)":
            self.central_value.set(f"Password: {data_list_specific[1]}")
        elif self.text_code == f"{self.username}.get_info(fullname)":
            self.central_value.set(f"Full Name: {data_list_specific[2]} {data_list_specific[3]} {data_list_specific[4]}")
        elif self.text_code == f"{self.username}.get_info(phone)":
            self.central_value.set(f"Phone Number: {data_list_specific[5]}")
        elif self.text_code == f"{self.username}.get_info(email)":
            self.central_value.set(f"Email: {data_list_specific[6]}")


def run_me():

    my_window = Tk()
    my_window.title("TestUnit")
    central = CommandWindow(my_window, "905shooter")

    central._create_new_field()

    my_window.mainloop()


# run_me()
