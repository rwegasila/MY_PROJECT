from tkinter import *

root=Tk()

e=Entry(root, width=20, bg="Green")
e.pack()
e.insert(0, "Enter your Name:")

def myclic():
    hello="Hello!"+e.get()
    myLabel=Label(root, text=hello)
    myLabel.pack()

myButton=Button(root, text="Enter Your Name", command=myclic, fg="green", bg="Black" ,padx=20, pady=10)
myButton.pack()


root.mainloop()