import random
def scommessa():
    conteggio = 0
    while conteggio in range(1):
        try:
            if type(risRich) is tuple and len(risRich) == 3:
                val = int(soldi_fine / 3)
                scommessa = int(input("Quanto vuoi scommettere?(max " + str(val) + " ): "))
                conteggio = 1
                while scommessa not in range(int(soldi_fine / 3) + 1):
                    scommessa = int(input("Scommetti una somma valida. "))
                    conteggio = 1
            elif type(risRich) is tuple and len(risRich) == 2:
                val = int(soldi_fine / 2)
                scommessa = int(input("Quanto vuoi scommettere?(max " + str(val) + " ): "))
                conteggio = 1
                while scommessa not in range(int(soldi_fine / 2) + 1):
                    scommessa = int(input("Scommetti una somma valida. "))
                    conteggio = 1
            else:
                val = soldi_fine
                scommessa = int(input("Quanto vuoi scommettere?(max " + str(val) + " ): "))
                conteggio = 1
                while scommessa not in range(soldi_fine + 1):
                    scommessa = int(input("Scommetti una somma valida. "))
                    conteggio = 1
        except ValueError:
            print("Devi inserire un valore numerico intero, riprova.")
            conteggio = 0
    if type(risRich) is tuple and len(risRich) == 3:
        scommessa *= 3
    elif type(risRich) is tuple and len(risRich) == 2:
        scommessa *= 2
    else:
        pass
    print("Valore scommessa: {}".format(scommessa))
    return scommessa
def richiesta():
    controllo = ["file", "diagonali"]
    scelta = input("Vuoi scommettere su file o diagonali? ").lower()
    while scelta not in controllo:
        scelta = input("Inserisci una scelta valida(file o diagonali): ").lower()
    if scelta in controllo[0]:
        conteggio = 0
        while conteggio in range(1):
            try:
                nfile = int(input("Su quante file vuoi scommettere? Si molteplicherà il valore scommesso per il numero "
                                  "di file. "))
                conteggio = 1
                while nfile not in range(1, 4):
                    nfile = int(input("Inserisci un valore valido(1, 2 o 3): "))
                    conteggio = 1
            except ValueError:
                print("Devi inserire un valore numerico, riprova.")
                conteggio = 0
        if nfile == 1:
            print("Le file sono contate dal basso verso l'alto. ")
            conteggio = 0
            while conteggio in range(1):
                try:
                    sfila = int(input("Scegli una delle 3 file: "))
                    conteggio = 1
                    while sfila not in range(1, 4):
                        sfila = int(input("Fai una scelta valida(1, 2 o 3). "))
                        conteggio = 1
                except ValueError:
                    print("Devi inserire un valore numerico, riprova.")
                    conteggio = 0
            diz = {1: 6,
                   2: 5,
                   3: 4}
            return diz.get(sfila)
        elif nfile == 2:
            print("Le file sono contate dal basso verso l'alto. ")
            conteggio = 0
            while conteggio in range(1):
                try:
                    sfila = int(input("Scegli la prima fila: "))
                    sfila2 = int(input("Scegli la seconda fila: "))
                    if sfila == sfila2:
                        print("Inserire due valori diversi.")
                        conteggio = 0
                    else:
                        conteggio = 1
                    while sfila and sfila2 not in range(1, 4):
                        sfila = int(input("Fai una scelta valida(1, 2 o 3) per la prima fila. "))
                        sfila2 = int(input("Fai una scelta valida(1, 2 o 3) per la seconda fila. "))
                        conteggio = 1
                except ValueError:
                    print("Devi inserire un valore numerico, riprova.")
                    conteggio = 0
            diz = {1: 6,
                   2: 5,
                   3: 4}
            return diz.get(sfila), diz.get(sfila2)
        else:
           return 4, 5, 6
    else:
        conDia = ["prima", "seconda"]
        print("Prima diagonale: \ \nSeconda diagonale: /")
        diagonale = input("Su quale diagonale vuoi scommettere?: ").lower()
        while diagonale not in conDia:
            diagonale = input("Inserisci una scelta valida(prima o seconda): ").lower()
        if diagonale in conDia[0]:
            return [[4], [5], [6]]
        else:
            return [[6], [5], [4]]
def slot():
    base = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    random.shuffle(base)
    col1 = base
    base = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    random.shuffle(base)
    col2 = base
    base = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    random.shuffle(base)
    col3 = base
    for j in range(4, 7):
        print("|", col1[j], "|", col2[j], "|", col3[j], "|")
    r = col1, col2, col3
    return r
def soldi():
    diz = {"hai perso": 0,
           "hai vinto": 2,
           "rimborso": 1,
           "rimborso su due file": 1,
           "rimborso su due file e perso su una": 2/3,
           "rimborso su una fila e perso nell'altra": 1/2,
           "rimborso su una file e perso sulle altre due": 1/3,
           "hai vinto su due file e perso su una": 4/3,
           "hai vinto su due file e rimborso su una": 5/3,
           "rimborso su tutte le file": 1,
           "hai vinto su una fila e rimborso sull altra": 3/2,
           "hai vinto su una fila e perso sull'altra": 1,
           "hai vinto su una fila e rimborso delle altre due": 4/3,
           "jackpot": 10}
    val = diz[risRis]
    vincite = int(risScom*val)
    soldiRimasti = soldi_fine + vincite
    return soldiRimasti
def risultato():
    conteggio = 0
    if type(risRich) == int:
        if risSlot[0][risRich] == risSlot[1][risRich] == risSlot[2][risRich]:
            return "hai vinto"
        elif all(x != risSlot[0][risRich] for x in (risSlot[1][risRich], risSlot[2][risRich])) and risSlot[1][risRich] != risSlot[2][risRich]:
            return "hai perso"
        else:
            return "rimborso"
    elif type(risRich) == tuple:
        try:
            for j in range(0, 3):
                if risSlot[0][risRich[j]] == risSlot[1][risRich[j]] == risSlot[2][risRich[j]]:
                    conteggio += 2
                elif all(x != risSlot[0][risRich[j]] for x in (risSlot[1][risRich[j]], risSlot[2][risRich[j]])) and risSlot[1][risRich[j]] != risSlot[2][risRich[j]]:
                    conteggio -= 2
                else:
                    conteggio += 1
            diz = {-6: "hai perso",
                   -3: "rimborso su una file e perso sulle altre due",
                   -2: "hai vinto",
                   0: "rimborso su due file e perso su una",
                   2: "hai vinto su due file e perso su una",
                   3: "rimborso su tutte le file",
                   4: "hai vinto su una fila e rimborso delle altre due",
                   5: "hai vinto su due file e rimborso su una",
                   6: "jackpot"}
            return diz.get(conteggio)
        except IndexError:
            conteggio = 0
            for j in range(0, 2):
                if risSlot[0][risRich[j]] == risSlot[1][risRich[j]] == risSlot[2][risRich[j]]:
                    conteggio += 2
                elif all(x != risSlot[0][risRich[j]] for x in (risSlot[1][risRich[j]], risSlot[2][risRich[j]])) and risSlot[1][risRich[j]] != risSlot[2][risRich[j]]:
                    conteggio -= 2
                else:
                    conteggio += 1
            diz = {-4: "hai perso",
                   -1: "rimborso su una fila e perso nell'altra",
                   0: "hai vinto su una fila e perso sull'altra",
                   2: "rimborso su due file",
                   3: "hai vinto su una fila e rimborso sull altra",
                   4: "hai vinto"}
            return diz.get(conteggio)
    else:
        a = int(risRich[0][0])
        b = int(risRich[1][0])
        c = int(risRich[2][0])
        conteggio = 0
        if risSlot[0][a] == risSlot[1][b] == risSlot[2][c]:
            conteggio += 2
        elif all(x != risSlot[0][a] for x in (risSlot[1][b], risSlot[2][c])) and risSlot[1][b] != risSlot[2][c]:
            conteggio -= 2
        else:
            conteggio += 1
        diz = {-2: "hai perso",
               1: "rimborso",
               2: "hai vinto"}
        return diz.get(conteggio)
print("Benvenuto!\n"
      "Regole:\n"
      "Puoi scegliere se scommettere sulle file o sulle diagonali.\n"
      "Scommessa minima per ogni fila o diagonale: 1$\n"
      "Se desideri è possibile scommettere su più file, il costo viene moltiplicato per il numero di file "
      "cosi come le vincite.\n"
      "Se nella fila o diagonale scelta appaiono 2 simboli uguali ti verrà restituito il valore scommesso.\n"
      "Se tutti i simboli sono uguali guadagnerai 100% del valore scommesso.\n"
      "Nel caso tu abbia scommesso su due file e i 3 simboli di ciascuna fila sono uguali il guadagno sarà del 200%.\n"
      "Se hai scommesso su tutte le file è possibile fare jackpot e guadagnare 10x la somma scommessa.\n"
      "Perdi se finisci tutti i soldi.\n"
      "Buona fortuna!")
while True:
    soldi_fine = 1000
    while soldi_fine >= 3:
        print("Possiedi: {}$".format(soldi_fine))
        risRich = richiesta()
        risScom = scommessa()
        soldi_fine = soldi_fine - risScom
        risSlot = slot()
        risRis = risultato()
        risSoldi = soldi()
        if risSoldi >= 3:
            print("Il nuovo saldo e' di: {}".format(risSoldi))
        if risSoldi < 3:
            print("Hai perso.")
        controllo = ["si", "no"]
        fine = 0
        while True:
            Verifica = input("Vuoi giocare ancora?:").lower()
            while Verifica not in controllo:
                Verifica = input("Inserisci una scelta valida(si o no): ").lower()
            if Verifica in controllo[1]:
                risSoldi = 0
                soldi_fine = risSoldi
                fine += 1
                break
            else:
                soldi_fine = risSoldi
                break
    if fine == 1:
        break
    if risSoldi < 3:
        controllo = ["si", "no"]
        Verifica = input("Vuoi giocare di nuovo?:").lower()
        while Verifica not in controllo:
            Verifica = input("Inserisci una scelta valida(si o no): ").lower()
        if Verifica in controllo[1]:
            break