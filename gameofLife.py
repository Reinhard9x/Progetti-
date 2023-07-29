from tkinter import *
import random
import time


window = Tk()
window.title('Game Of Life')
window.resizable(False, False)
#list to keep track of the square color and coords
list = []
status = StringVar()
#loops to randomly assign color to all the squares
for i in range(20):
    for j in range(20):
        cont = 0
        status.set('white')
        rand = random.randint(1, 11)
        if rand in range(1, 3):
            status.set('black')
            cont = 1
        label = Label(window, bg=status.get(), width=2, height=1)
        label.grid(row=i, column=j)
        if cont == 1:
            list.append([i, j, 'black'])
        else:
            list.append([i, j, 'white'])
num = 0
#check if square is on column 0 or 19. this is needed to make sure that it doesn't take into consideration
#squares on the opposite side of the grid in the rows above or below when checking if it needs to change color.
#it becomes clear why its needed if you remove it
first_column = []
last_column = []
for i in range(0, 381, 20):
    first_column.append(i)
for i in range(19, 400, 20):
    last_column.append(i)
#start the game
while True:
    # keep track of the squares whoose color needs to change
    listw1 = []
    listw2 = []
    listw3 = []
    listb1 = []
    listb2 = []
    listb3 = []
    for i in range(20):
        for j in range(20):
            for k in range(400):

                if list[k] == [i, j, 'white']:
                    cont = 0
                    if k not in last_column:
                        if list[k + 1][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k not in first_column:
                        if list[k - 1][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k < 381:
                        if list[k + 19][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k > 18:
                        if list[k - 19][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k < 380:
                        if list[k + 20][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k > 19:
                        if list[k - 20][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k < 379:
                        if list[k + 21][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k > 20:
                        if list[k - 21][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    #saves the squares that need to go from white to black
                    if cont == 5:
                        listw1.append(k)
                        listw2.append(i)
                        listw3.append(j)

                if list[k] == [i, j, 'black']:
                    cont = 0
                    if k not in last_column:
                        if list[k + 1][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k not in first_column:
                        if list[k - 1][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k < 381:
                        if list[k + 19][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k > 18:
                        if list[k - 19][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k < 380:
                        if list[k + 20][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k > 19:
                        if list[k - 20][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k < 379:
                        if list[k + 21][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    if k > 20:
                        if list[k - 21][2] == 'white':
                            cont += 1
                    else:
                        cont += 1
                    #squares that need to go from black to white
                    if cont != 5 and cont != 6:
                        listb1.append(k)
                        listb2.append(i)
                        listb3.append(j)
    #change square color from white to black
    for l in range(0, len(listw1)):
        label = Label(window, bg='black', width=2, height=1)
        label.grid(row=listw2[l], column=listw3[l])
        list[listw1[l]] = [listw2[l], listw3[l], 'black']
    # change square color from black to white
    for l in range(0, len(listb1)):
        label = Label(window, bg='white', width=2, height=1)
        label.grid(row=listb2[l], column=listb3[l])
        list[listb1[l]] = [listb2[l], listb3[l], 'white']


    window.update()
    time.sleep(0.03)


window.mainloop()
