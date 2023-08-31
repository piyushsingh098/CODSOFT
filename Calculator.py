from tkinter import *

def button_click(number):
    current=display.get()
    display.delete(0,END)
    display.insert(END, current+str(number))
def button_Clear():
    display.delete(0,END)
def button_Equal():
    try:
        expression = display.get()
        result=eval(expression)
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0,END)
        display.insert(END, "Error")
window = Tk()
window.title("Calculator")

display=Entry(window, width=25, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)

button_1 = Button(window, text="1", command=lambda:button_click(1))
button_1.grid(row=1, column=0)

button_2 = Button(window, text="2", command=lambda:button_click(2))
button_2.grid(row=1, column=1)

button_3 = Button(window, text="3", command=lambda:button_click(3))
button_3.grid(row=1, column=2)

button_4 = Button(window, text="4", command=lambda:button_click(4))
button_4.grid(row=2, column=0)

button_5 = Button(window, text="5", command=lambda:button_click(5))
button_5.grid(row=2, column=1)

button_6 = Button(window, text="6", command=lambda:button_click(6))
button_6.grid(row=2, column=2)

button_7 = Button(window, text="7", command=lambda:button_click(7))
button_7.grid(row=3, column=0)

button_8 = Button(window, text="8", command=lambda:button_click(8))
button_8.grid(row=3, column=1)

button_9 = Button(window, text="9", command=lambda:button_click(9))
button_9.grid(row=3, column=2)

button_0 = Button(window, text="0", command=lambda:button_click(0))
button_0.grid(row=4, column=1)

button_clear=Button(window, text='clear', command=button_Clear)
button_clear.grid(row=4, column=0)

button_plus=Button(window, text="+", command=lambda:button_click("+"))
button_plus.grid(row=1, column=3)

button_minus=Button(window, text='-', command=lambda:button_click('-'))
button_minus.grid(row=2, column=3)

button_multiply=Button(window, text='*', command=lambda:button_click('*'))
button_multiply.grid(row=3, column=3)

button_divide=Button(window, text="/", command=lambda:button_click("/"))
button_divide.grid(row=4, column=3)

button_equal=Button(window, text='=', command=button_Equal)
button_equal.grid(row=4, column=2)

window.mainloop()