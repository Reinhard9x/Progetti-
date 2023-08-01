from tkinter import *
import random
import time


def status_check():
    #if the square is in the first column the 3 squares to the left will be automatically considered white
    if j in first_column:
        cont = 3
    #these make sure it will consider only the same column and the one to the right
        a = -1
        b = 2
        c = 0
        d = 2
        cont = Count(a, b, c, d, cont)
        return cont
    # if the square is in the last column the 3 squares to the right will be automatically considered white
    elif j in last_column:
        cont = 3
        a = -1
        b = 2
        c = -1
        d = 1
        cont = Count(a, b, c, d, cont)
        return cont
    #same concept but for squares in the first or last row
    elif i == 0:
        cont = 3
        a = 0
        b = 2
        c = -1
        d = 2
        cont = Count(a, b, c, d, cont)
        return cont
    elif i == num-1:
        cont = 3
        a = -1
        b = 1
        c = -1
        d = 2
        cont = Count(a, b, c, d, cont)
        return cont
    else:
        cont = 0
        a = -1
        b = 2
        c = -1
        d = 2
        cont = Count(a, b, c, d, cont)
        return cont


def Count(a, b, c, d, cont):
    for n in range(a, b):
        for m in range(c, d):
            # exclude the square we are looking to change from consideration
            if m == n == 0:
                continue
            # check the color of the squares around it
            try:
                if list[i + n][j + m] == 'white':
                    cont += 1
            except IndexError:#this takes care of the 4 squares in the top left/right and bottom left/right
                cont += 1
    return cont


num = 20
#check if square is on the first or last. this is needed to make sure that it doesn't take into consideration
#squares on the opposite side of the grid in the rows above or below when checking if it needs to change color.
#it becomes clear why its needed if you remove it
first_column = []
last_column = []
for i in range(0, ((num*(num-1))+1), num):
    first_column.append(i)
for i in range(num-1, num*num, num):
   last_column.append(i)

window = Tk()
window.title('Game Of Life')
window.resizable(False, False)
#list to keep track of the square color and coords
list = [['']*num for i in range(num)]
#don't ever use list = [['']*num]*num ever >:C
status = StringVar()
#loops to randomly assign color to all the squares
for i in range(num):
    for j in range(num):
        status.set('white')
        rand = random.randint(1, 10)
        if rand in range(1, 3):
            status.set('black')
        label = Label(window, bg=status.get(), width=2, height=1)
        label.grid(row=i, column=j)
        list[i][j] = status.get()

#start the game
while True:
    # keep track of the squares whose color needs to change
    listw2 = []
    listw3 = []
    listb2 = []
    listb3 = []
    for i in range(num):
        for j in range(num):
            if list[i][j] == 'white':
                cont = status_check()
                # saves the squares that need to go from white to black
                if cont == 5:
                    listw2.append(i)
                    listw3.append(j)
            if list[i][j] == 'black':
                cont = status_check()
                # squares that need to go from black to white
                if cont != 5 and cont != 6:
                    listb2.append(i)
                    listb3.append(j)
    # change square color from white to black
    for l in range(0, len(listw2)):
        label = Label(window, bg='black', width=2, height=1)
        label.grid(row=listw2[l], column=listw3[l])
        list[listw2[l]][listw3[l]] = 'black'
    # change square color from black to white
    for l in range(0, len(listb2)):
        label = Label(window, bg='white', width=2, height=1)
        label.grid(row=listb2[l], column=listb3[l])
        list[listb2[l]][listb3[l]] = 'white'
    window.update()
    time.sleep(0.03)
