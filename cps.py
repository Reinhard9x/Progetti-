from tkinter import *
import time
import threading


def count():
    global cont
    global start
    cont += 1
    if cont == 1:
        start = time.perf_counter()
    click = Label(text='numero click:'+str(cont)).grid(row=1, column=0)
    window.update_idletasks()


def fine():
    while True:
        try:
            end = time.perf_counter()
            diff = end - start
            if diff == 10:
                timer = Label(text='secondi passati:' + str(diff)).grid(row=2, column=0)
                button.config(state=DISABLED)
                cps = cont / diff
                clickps = Label(text='click al secondo:' + str(cps)).grid(row=3, column=0)
                break
        except NameError:
            continue


cont = 0

window = Tk()


button = Button(window,
                text='ciao',
                command=count,
                state=ACTIVE)
button.grid(row=0, column=0, padx=30)

x = threading.Thread(target=fine, args=())
x.start()


window.mainloop()

