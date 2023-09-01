from tkinter import *
root = Tk()
root.title("Area and Perimeter calculator")

def calculate():
    var3 = var1.get()
    var4 = var2.get()
    var5 = 2*(var3 + var4)
    var6= var3*var4
    e3.insert(0, var5)
    e4.insert(0, var6)

def delete():
    e3.delete(0 , END)
    e4.delete(0 , END)


var1 = IntVar()
var2 = IntVar()
label1 = Label(text = "Length" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 0 , column = 0 )
e1 = Entry(width = 30 , font = ('arial' , 30 , 'bold') , textvariable= var1)
e1.grid(row = 0 , column  = 1)

label2 = Label(text = "Breadth" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 1 , column = 0 )
e2 = Entry(width = 30 , font = ('arial' , 30 , 'bold') , textvariable= var2 )
e2.grid(row = 1 , column  = 1)

label3 = Label(text = "Perimeter" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 2 , column = 0 )
e3 = Entry(width = 30 , font = ('arial' , 30 , 'bold') )
e3.grid(row = 2 , column  = 1)

label4 = Label(text = "Area" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 3 , column = 0 )
e4 = Entry(width = 30 , font = ('arial' , 30 , 'bold') )
e4.grid(row = 3 , column  = 1)

btn1= Button(text = 'calculate' , font = ('arial' , 30 , 'bold') , width = 30 ,command = calculate).grid(row =4 ,column = 0 , sticky = W)
btn2= Button(text = 'clear' , font = ('arial' , 30 , 'bold') , width = 30 ,command = delete).grid(row =4 ,column = 1 , sticky = E)


root.mainloop()
