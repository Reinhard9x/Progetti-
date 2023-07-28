from tkinter import *
#write numbers and symbols
def num(var):
    global text

    text = text + str(var)
    equation.set(text)


#clear everything
def clear():
    global text

    text = ''
    equation.set(text)


#backspace
def back():
    global text

    text = text[0: len(equation.get())-1]
    equation.set(text)


#results
def results():
    global text

    try:
        result = str(eval(text))
        equation.set(result)
        text = result
    except SyntaxError:
        equation.set('Syntax error')
        text = ''
    except ZeroDivisionError:
        equation.set('Error, cant divide by 0')
        text = ''

#window
window = Tk()
window.title('Calculator')
window.resizable(0,0)
#delete or change the name/path of the photo
photo = PhotoImage(file='calc.png')
window.iconphoto(True, photo)
#this will be used to easily keep track of what is written in the entry
#text will keep track of everything and equation will add it in the entry
text = ''
equation = StringVar()
entry = Entry(window, textvariable=equation, font=('Arial', 15), justify=RIGHT)
entry.grid(row=0, column=0, columnspan=5, sticky=EW)
#disable keyboard inputs inside entry
entry.bind('<Key>', lambda e: 'break')
#buttons from 0 to 9

b_number = Button(window, text='1', width=6, height=3, command=lambda :num(1)).grid(row=1, column=0)
b_number = Button(window, text='2', width=6, height=3, command=lambda :num(2)).grid(row=1, column=1)
b_number = Button(window, text='3', width=6, height=3, command=lambda :num(3)).grid(row=1, column=2)
b_number = Button(window, text='4', width=6, height=3, command=lambda :num(4)).grid(row=2, column=0)
b_number = Button(window, text='5', width=6, height=3, command=lambda :num(5)).grid(row=2, column=1)
b_number = Button(window, text='6', width=6, height=3, command=lambda :num(6)).grid(row=2, column=2)
b_number = Button(window, text='7', width=6, height=3, command=lambda :num(7)).grid(row=3, column=0)
b_number = Button(window, text='8', width=6, height=3, command=lambda :num(8)).grid(row=3, column=1)
b_number = Button(window, text='9', width=6, height=3, command=lambda :num(9)).grid(row=3, column=2)
b_zero = Button(window, command=lambda :num('0'), text='0', width=6, height=3).grid(row=4, column=1)
#other buttons
b_dot = Button(window, command=lambda :num('.'), text='.', width=6, height=3,).grid(row=4, column=0)
b_equal = Button(window,command=results, text='=', width=6, height=3,).grid(row=4, column=2)
b_del = Button(window, command=back, text='DEL', width=6, height=3, bg='red', activebackground='red').grid(row=1, column=3)
b_clear = Button(window, command=clear, text='AC', width=6, height=3, bg='red', activebackground='red').grid(row=1, column=4)
b_per = Button(window, command=lambda :num('*'), text='x', width=6, height=3, bg='orange', activebackground='orange').grid(row=2, column=3)
b_div = Button(window, command=lambda :num('/'), text=':', width=6, height=3, bg='orange', activebackground='orange').grid(row=2, column=4)
b_plus = Button(window, command=lambda :num('+'), text='+', width=6, height=3, bg='orange', activebackground='orange').grid(row=3, column=3)
b_minus = Button(window, command=lambda :num('-'), text='-', width=6, height=3, bg='orange', activebackground='orange').grid(row=3, column=4)
b_exit = Button(window, command=lambda :exit(), text='Exit', width=6, height=3, bg='red', activebackground='red').grid(row=4, column=3, columnspan=2, sticky=EW)
window.mainloop()
