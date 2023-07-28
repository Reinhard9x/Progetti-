from tkinter import *
from tkinter import filedialog, colorchooser
from tkinter.messagebox import *
from tkinter.simpledialog import *


def open_file():
    try:
        text.delete('1.0', END)
        file_path = filedialog.askopenfilename(initialdir='Desktop')
        mod_file = open(file_path)
        text.insert('1.0', mod_file.read())
    except Exception:
        showwarning('Error', 'You can only open text files')


def save_file():
    save_place = filedialog.asksaveasfile(defaultextension='.txt')
    file_save = str(text.get('1.0', END))
    save_place.write(file_save)


def Help():
    showinfo('About this program', 'You are on your own, sorry, no help is coming')


def Fontcolor():
    color = colorchooser.askcolor()
    text.config(fg=color[1])


def Fontsize():
    global font_name
    global font_size
    try:
        size = askinteger('Font', 'Choose font size')
        font_size.set(size)
        text.config(font=(font_name.get(), font_size.get()))
    except Exception:
        pass


def Fonttype():
    global font_name
    global font_size
    try:
        type = askstring('Font', 'Choose font type')
        font_name.set(type)
        text.config(font=(font_name.get(), font_size.get()))
    except Exception:
        pass


def Fontlist():
    showinfo('Font list', 'Look it up on google')


window = Tk()
#center the window
window_height = 1000
window_width = 1000
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


#allow text area to expand if sticky is used
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


window.title('Text editor')
menu = Menu(window)
window.config(menu=menu)


#variables for font and size. Allows choice later on.
font_name = StringVar(window)
font_name.set('Helvetica')
font_size = IntVar(window)
font_size.set(15)


text = Text(window, bg='beige', font=(font_name.get(), font_size.get()))
text.grid(sticky=NSEW)


#scroll bar
scroll_bar = Scrollbar(text, jump=True, command=text.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll_bar.set)


file = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file)
file.add_command(label='Open', command=open_file)
file.add_command(label='Save', command=save_file)
file.add_separator()
file.add_command(label='Exit', command=quit)


edit = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Font Color', command=Fontcolor)
edit.add_command(label='Font Size', command=Fontsize)
edit.add_command(label='Font Type', command=Fonttype)


about = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=about)
about.add_command(label='About', command=Help)
about.add_command(label='Fonts', command=Fontlist)


window.mainloop()
