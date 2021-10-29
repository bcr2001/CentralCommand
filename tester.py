
# TEXT AREA CODE


from tkinter import *

# def submit():
#     input = text.get("1.0", END)
#     print(input)


# window = Tk()
# text = Text(window, bg="light yellow", font=("Ink Free", 25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=10)
# text.pack()
# button = Button(window, text="submit", command=submit)
# button.pack()
# window.mainloop()

task = 0
def submit():
    global task
    task+=1
    text_me.set(str(task))


window = Tk()

text_me = StringVar()

string_label = Label(window,textvariable=text_me)
string_label.pack()

button = Button(window, text="submit", command=submit)
button.pack()
window.mainloop()


# TKINTER SCROLL BAR CODE

# from tkinter import *
# from tkinter import ttk

# window = Tk()
# window.geometry("500x400")

# #create a main frame 
# main_frame = Frame(window)
# main_frame.pack(fill=BOTH,expand=1)

# #create a canvas 
# my_canvas = Canvas(main_frame)
# my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

# # add a scroll bar to the canvas 
# my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
# my_scrollbar.pack(side=RIGHT,fill=Y)


# #Configure canvas 
# my_canvas.configure(yscrollcommand=my_scrollbar.set)
# my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))


# # create another frame inside the canvas 
# second_frame = Frame(my_canvas)

# #add that New frame to a window in the canvas 
# my_canvas.create_window((0,0),window=second_frame,anchor="nw")


# for thing in range(1,100):
#     Button(second_frame,text=f"Button{thing}").grid(row=thing,column=0,pady=10,padx=10)



# window.mainloop()


#CREATING TABLES IN TKINTER

# Python program to create a table

# from tkinter import *


# class Table:

#     def __init__(self, root):

#         # code for creating table
#         for i in range(total_rows):
#             for j in range(total_columns):

#                 self.e = Entry(root, width=20, fg='blue',
#                                font=('Arial', 16, 'bold'))

#                 self.e.grid(row=i, column=j)
#                 self.e.insert(END, lst[i][j])


# # take the data
# lst = [(1, 'Raj', 'Mumbai', 19),
#        (2, 'Aaryan', 'Pune', 18),
#        (3, 'Vaishnavi', 'Mumbai', 20),
#        (4, 'Rachna', 'Mumbai', 21),
#        (5, 'Shubham', 'Delhi', 21)]

# # find total number of rows and
# # columns in list
# total_rows = len(lst)
# total_columns = len(lst[0])

# # create root window
# root = Tk()
# t = Table(root)
# root.mainloop()

# 905shooter.get_info()