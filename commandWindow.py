from tkinter import *



class CommandWindow:

    def __init__(self,master,username):
        self.master = master 
        self.username = username #this variable holds the username of the authenticated user.

        #this label diplays the username it the top right corner of the window 
        self.username_display_label = Label(self.master,text=f"Welcome {self.username}",font=("Arial",15,"bold"),bg="black",fg="orange")
        self.username_display_label.place(x=5,y=10)

    


    

        


# def run_me():

#     createAccountWindow = Tk()
#     myapp = CommandWindow(createAccountWindow)
#     createAccountWindow.geometry("650x450")
#     createAccountWindow.title("Create Window")

#     createAccountWindow.resizable(False, False)
#     createAccountWindow.mainloop()


# run_me()
