# importing everything from tkinter
from tkinter import *

# creating the tkinter window
Main_window = Tk()

# variable
my_text = "GeeksforGeeks updated !!!"

# function define for
# updating the my_label
# widget content
def counter():

    # use global variable
    global my_text
    
    # configure
    my_label.config(text = my_text)
    sngn.config(text=sng_name[sn-1])

sng_name=["Star Boy","SunFlower","Holiday","Calling"]
sngn=Label(Main_window,text="starboy")
sngn.place(relx=0.5,rely=0.1,anchor=CENTER)
print(type(sngn))


# create a button widget and attached
# with counter function
my_button = Button(Main_window,
                text = "Please update",
                command = counter)

# create a Label widget
my_label = Label(Main_window,
                text = "geeksforgeeks")
print(type(my_label))
# place the widgets
# in the gui window
my_label.place(relx=0.5,rely=0.1,anchor=CENTER)
my_button.place(relx=0.7,rely=0.4,anchor=CENTER)

# Start the GUI
Main_window.mainloop()
                                                         