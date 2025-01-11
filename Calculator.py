from tkinter import *
root=Tk()

e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

#Creating the functions that can enable the buttons to operate

#(i)Creating the unction that can opearte between the all number buttons(0-9) and Entry
def  myclic(number):
       myinput=e.get()
       e.delete(0, END)
       e.insert(0, str(myinput)+str(number))
       
#(ii) Creating the fuction for clear button
def clear_button() :
    e.delete(0, END)  
    
#(iii)Creating the function for add button
def add_button():
    first_number=e.get()
    global f_num
    global math 
    math="Addtion"
    f_num=int(first_number)
    e.delete(0, END)
    
#Creating the function for Equal button
def Equal_button():
    second_number=e.get()
    e.delete(0, END)
    
    if math=="Addtion":
     e.insert(0, f_num+int(second_number))
     
    if math=="Subtraction":
     e.insert(0, f_num-int(second_number))
         
    if math=="Multiplication":
     e.insert(0, f_num * int(second_number))
         
    if math=="Division":
     e.insert(0, f_num/int(second_number))

    
        
#(iv)Creating the function for subtraction button
def sub_button():
    first_number=e.get()
    global f_num
    global math 
    math="Subtraction"
    f_num=int(first_number)
    e.delete(0, END)
    
        
#(v)Creating the function for multiplicatin button
def multplication_button():
    first_number=e.get()
    global f_num
    global math 
    math="Multiplication"
    f_num=int(first_number)
    e.delete(0, END)
    
        
#(vi)Creating the function for division button
def div_button():
    first_number=e.get()
    global f_num
    global math 
    math="Division"
    f_num=int(first_number)
    e.delete(0, END)
       
    #Definng the buttons
button_1=Button(root, text="1", padx=40, pady=20, command=lambda:myclic(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda:myclic(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda:myclic(3)) 
button_4=Button(root, text="4", padx=40, pady=20, command=lambda:myclic(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda:myclic(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda:myclic(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda:myclic(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda:myclic(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda:myclic(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda:myclic(0))
    
button_clear=Button(root, text="clear", padx=78, pady=20, command=clear_button)
button_add=Button(root, text="+", padx=40, pady=20, command=add_button)
button_equal=Button(root, text="=", padx=86, pady=20, command=Equal_button)
button_subtract=Button(root, text="-", padx=40, pady=20, command=sub_button)
button_multiplication=Button(root, text="*", padx=40, pady=20, command=multplication_button)
button_division=Button(root, text="/", padx=40, pady=20, command=div_button)


#setting the buttons into the screen
button_1.grid(row=3 , column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=2)
button_4.grid(row= 2, column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row= 2, column=2 )
button_7.grid(row= 1, column=0)
button_8.grid(row= 1, column=1)
button_9.grid(row= 1, column=2)
button_0.grid(row= 4, column=0)
button_clear.grid(row= 4, column=1, columnspan=2)
button_add.grid(row= 5, column=0) 
button_equal.grid(row= 5, column=1, columnspan=2)
button_subtract.grid(row=6 , column=0)
button_multiplication.grid(row= 6, column=1)
button_division.grid(row= 6, column=2)





root.mainloop()

