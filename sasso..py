import random

def e(m, p):
    g = o
    k = i
    if m == h[0] and p == h[2]:
        print("Hai vinto!")
        g = g+1
    elif m == h[2] and p == h[1]:
       print("Hai vinto!")
       g = g+1
    elif m == h[1] and p == h[0]:
       print("Hai vinto!")
       g = g+1
    else:
       print("Hai perso. :C")
       k = k+1
    return [g, k]
def w():
    m = input("Inserire mossa del giocatore: ").lower()
    while m not in h:
        m = input("Inserire mossa valida({}, {} o {}): ".format(h[0], h[1], h[2])).lower()
    print("hai scelto: {}".format(m))
    p = random.choice(h)
    print("il computer ha scelto: {}".format(p))
    return [m, p]
print("Gioco carta forbice sasso contro il pc.")
print()
i = 0
o = 0
while True:
    h = ["carta", "forbice", "sasso"]
    z = w()
    m = z[0]
    p = z[1]
    if p == m:
        print("pareggio, riprova: ")
        print()
        while p == m:
            z = w()
            m = z[0]
            p = z[1]
            if p == m:
                print("pareggio, riprova: ")
                print()
            else:
                f = e(m, p)
    else:
        f = e(m, p)
    v = ["si", "no"]
    a = input("vuoi giocare di nuovo?: ").lower()
    while a not in v:
        a = input("Rispondi correttamente(si, no): ").lower()
    if a in v[1]:
        print("Ciao ciao!")
        break
    else:
        o = f[0]
        i = f[1]
        print("\nPunteggio:\n"
              "Giocatore:{}\n"
              "Computer:{}\n".format(o, i))