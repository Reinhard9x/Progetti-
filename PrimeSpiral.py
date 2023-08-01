from tkinter import *
import math


#check if the number is prime
def prime(num):
    val = int(math.sqrt(num))
    for i in range(2, val+1):
        result = num % i
        if result == 0:
            return False
    else:
        return True

window_height = 1070
window_width = 1020
height = 51
width = 51

window = Tk()
window.title('Prime spiral')

#window.resizable(False, False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
num = 0
#store info
list = []
color = StringVar()

#give a color to all squares
for i in range(height):
    for j in range(width):
        num += 1
        if num > 1 and prime(num) is True:
            color.set('red')
        else:
            color.set('black')
        list.append(color.get())
#direction and rate of direction change
dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]#right -> up -> left -> down
val = 0
num = 0 #number of colors to assign
rate = 0
#start from the center
i = int(height//2)
j = int(width//2)
label = Label(window, bg='#00ff00', width=2, height=1)#made it green for clarity
label.grid(row=i, column=j)
#rearrange in a spiral
while num in range(len(list)):
    for k in range(1 + rate): #rate decides how many times the program goes in the same direction (val)
        try:
            num += 1
            i += dir[val][0]
            j += dir[val][1]
            label = Label(window, bg=list[num], width=2, height=1) #text=num+1, fg='yellow')
            label.grid(row=i, column=j)
        except IndexError:#have no clue why it gives an indexerror on the last list[num], something wierd is going on
                          #but the spiral is correct. Add fg color and text to check for yourself
            break
    val += 1
    if val == 4:#once it goes to 3 it resets
        val = 0
    if num == (pow(rate+1, 2) + rate+1):# 2, 6, 12, 20, 30...n=n^2+n
        rate += 1

window.mainloop()
