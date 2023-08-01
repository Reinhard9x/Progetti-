from tkinter import *
import random
import time

num = 30

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
                cont = 0
                for n in range(-1, 2):
                    for m in range(-1, 2):
                        # exclude the square we are looking to change from consideration
                        if m == n == 0:
                            continue
                        # check the color of the squares around it
                        try:
                            if list[i + n][j + m] == 'white':
                                cont += 1
                        except IndexError:
                            cont += 1
                # saves the squares that need to go from white to black
                if cont == 5:
                    listw2.append(i)
                    listw3.append(j)
            if list[i][j] == 'black':
                cont = 0
                for n in range(-1, 2):
                    for m in range(-1, 2):
                        if m == n == 0:
                            continue
                        try:
                            if list[i + n][j + m] == 'white':
                                cont += 1
                        except IndexError:
                            cont += 1
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
