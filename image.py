from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.iconbitmap('C:/Users/DEVIS/Desktop')

my_image=ImageTk.PhotoImage(Image.open("C:/Users/DEVIS/Desktop/PYTHO/MY PROJECTS/search.png"))

my_label=Label(image=my_image)
my_image.pack()




button_quite=Button(root, text="Exit Program", command=root.quit)
button_quite.pack()

root.mainloop()
