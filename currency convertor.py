from tkinter import *
from tkinter import ttk

def convert():
    var2 = var1.get()
    var3 = indicator.get()
    if(var3=="india"):
        e3.delete(0,END)
        var4 = ((var2*83.16) ,"Rupees")
        e3.insert(0,var4)

    elif (var3 == "china"):
        e3.delete(0, END)
        var4 = ((var2 * 7.28), "yuan")
        e3.insert(0, var4)

    elif (var3 == "usd"):
        e3.delete(0, END)
        var4 = ((var2 * 1), "usd")
        e3.insert(0, var4)

    elif (var3 == "united kingdom"):
        e3.delete(0, END)
        var4 = ((var2 * 0.79), "pound")
        e3.insert(0, var4)

    else:
        e3.delete(0, END)
        var4 = ( "please select a country!")
        e3.insert(0, var4)

'''def clear():
    e1.delete(0,END)
    e3.delete(0,END)'''

root = Tk()
root.title("Currency Converter")

var1 = IntVar()
indicator = StringVar(value="choose a country")
Label(text = 'Currency Converter' , padx = 10 , font= ('arial' , 30 , 'bold')).grid(row = 0 ,column = 1)

Label(text = "Amount (in $)" , padx = 10 , font= ('arial' , 30 , 'bold')).grid(row = 1 ,sticky = W)
e1 = Entry(width = 20 , font = ('arial' , 30 , 'bold'),textvariable=var1)
e1.grid(row=1 , column  = 1)

Label(text = "Country" , padx = 10 , font= ('arial' , 30 , 'bold')).grid(row = 2 ,sticky = W)
e2 = ttk.Combobox(width = 19 , font = ('arial' , 30 , 'bold'),textvariable=indicator)
e2["values"] = ('india' , 'china' , 'usd' , 'united kingdom')
e2.grid(row=2 , column  = 1)

Label(text = "Total Amount" , padx = 10 , font= ('arial' , 30 , 'bold')).grid(row = 3 ,sticky = W)
e3 = Entry(width = 20 , font = ('arial' , 30 , 'bold'))
e3.grid(row=3 , column  = 1)

Button(text = 'Convert' ,font = ('arial' , 30 , 'bold') , width  = 9 ,command = convert).grid(row = 4 , column = 1 , sticky = W)
#Button(text = 'Clear' ,font = ('arial' , 30 , 'bold') , width  = 9 , command=clear).grid(row = 4 , column = 1 , sticky = E)
root.mainloop()
