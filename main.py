from tkinter import *

################ Creating GUI Window #######################
window = Tk()
window.title("This is my first python GUI")
window.minsize(width=500, height=300)
window.config(padx= 50, pady=50)


############ Button Action Class #######################
def button_clicked():
    string = input.get()
    my_text.config(text=string, font=("Arial", 24, "bold"))

#-------------- Text Label ------------------#
my_text = Label()
my_text.config(text="Aakash", font=("Arial", 24, "bold"))
my_text.grid(row=0,column=0)
#------------------------ Button Class -----------------------#

my_button = Button(text="Click me", command=button_clicked)
my_button.grid(row= 1, column=1)

# -------------------- Input Class -----------------#

input = Entry(width = 10)
input.grid(row=3, column=3)

# --------------- New Button ------------#

new_button = Button(text= "New Waala")
new_button.grid(row= 0, column=2)




window.mainloop()
