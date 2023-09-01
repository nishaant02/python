from tkinter import *
root = Tk()
root.title("Area and Perimeter calculator")

def calculate():
    var2 = var1.get()
    var3 = 3.142*var2*var2
    var4= 2*3.142*var2
    e2.insert(0, var3)
    e3.insert(0, var4)

def delete():
    e1.delete(0 , END)
    e2.delete(0 , END)


var1 = IntVar()
label1 = Label(text = "radius" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 0 , column = 0 )
e1 = Entry(width = 30 , font = ('arial' , 30 , 'bold') , textvariable= var1)
e1.grid(row = 0 , column  = 1)

label2 = Label(text = "Area" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 1 , column = 0 )
e2 = Entry(width = 30 , font = ('arial' , 30 , 'bold') )
e2.grid(row = 1 , column  = 1)

label3 = Label(text = "Perimeter" , width = 20 , font = ('arial' , 30 , 'bold')).grid(row = 2 , column = 0 )
e3 = Entry(width = 30 , font = ('arial' , 30 , 'bold') )
e3.grid(row = 2 , column  = 1)

btn1= Button(text = 'calculate' , font = ('arial' , 30 , 'bold') , width = 30 ,command = calculate).grid(row =3 ,column = 0 , sticky = W)
btn2= Button(text = 'clear' , font = ('arial' , 30 , 'bold') , width = 30 ,command = delete).grid(row =3 ,column = 1 , sticky = E)


root.mainloop()
