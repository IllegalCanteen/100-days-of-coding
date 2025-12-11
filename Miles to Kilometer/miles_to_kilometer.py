from tkinter import *

FONT=("Arial",24,"bold")
def button_clicked():
    try:
        miles=float(input.get())
        km= round(miles * 1.609344)
        my_label_3.config(text=km)
    except ValueError:
        pass

window=Tk()
window.title("Miles to Kilometer calculator")
window.minsize(width=500,height=300)
window.config(padx=100,pady=150)

my_label1=Label(text="Miles",font=FONT)
my_label1.grid(row=0,column=2)
my_label1.config(padx=20,pady=20)

my_label2=Label(text="is equal to",font=FONT)
my_label2.grid(row=1,column=0)
my_label2.config(padx=20,pady=20)

my_label_3=Label(text=0,font=FONT)
my_label_3.grid(row=1,column=1)
my_label_3.config(padx=20,pady=20)

my_label_4=Label(text="Km",font=FONT)
my_label_4.grid(row=1,column=2)
my_label_4.config(padx=20,pady=20)

button=Button(text="Calculate",command=button_clicked,height=3,width=15)
button.grid(row=2,column=1)

input=Entry(width=20)
input.grid(row=0,column=1)
window.mainloop()