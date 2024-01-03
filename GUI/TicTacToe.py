import tkinter as tk

def setzen(x,y):
    global field
    if field[x][y]!="":
        return
    global x_turn
    if x_turn == True:
        turn = "X"
        ausgabe.config(text="O ist dran")
        field[x][y] = turn
        x_turn = False
    else:
        global x_wins
        global o_wins
        turn = "O"
        ausgabe.config(text="X ist dran")
        ausgabe2.config()
        field[x][y] = turn
        x_turn = True
    reload()
    if win(x,y,turn):
        ausgabe.config(text=f"{turn} hat gewonnen")
        kachel1.config(state="disabled")
        kachel2.config(state="disabled")
        kachel3.config(state="disabled")
        kachel4.config(state="disabled")
        kachel5.config(state="disabled")
        kachel6.config(state="disabled")
        kachel7.config(state="disabled")
        kachel8.config(state="disabled")
        kachel9.config(state="disabled")
    
def reset():
    if kachel1.cget("state") == "active":
        global x_wins
        global y_wins
        x_wins = 0
        o_wins = 0
    global field
    field = [["","",""],
         ["","",""],
         ["","",""]]
    kachel1.config(state="active")
    kachel2.config(state="active")
    kachel3.config(state="active")
    kachel4.config(state="active")
    kachel5.config(state="active")
    kachel6.config(state="active")
    kachel7.config(state="active")
    kachel8.config(state="active")
    kachel9.config(state="active")
    reload()
    ausgabe.config(text="X ist dran")

def reload():
    k1.set(field[0][0])
    k2.set(field[0][1])
    k3.set(field[0][2])
    k4.set(field[1][0])
    k5.set(field[1][1])
    k6.set(field[1][2])
    k7.set(field[2][0])
    k8.set(field[2][1])
    k9.set(field[2][2])

def win(x,y,turn):
    win = False
    if field[x].count(turn) == 3:
        win = True
    vertical = []
    for i in range(3):
        vertical.append(field[i-1][y])
    if vertical.count(turn) == 3:
        win = True
    if (field[0][0] == turn and field[1][1] == turn and field[2][2] == turn) or (field[0][2] == turn and field[1][1] == turn and field[2][0] == turn):
        win = True
    return win

window = tk.Tk()
window.title("TicTacToe")
window.geometry("450x535")

spielbrett = tk.Frame(master=window,height=401,width=401,background="lightgrey")
infoscreen = tk.Frame(master=window,height=60,width=401,background="lightgrey")

global field
field = [["","",""],
         ["","",""],
         ["","",""]]

global x_turn
x_turn = True

global x_wins
global y_wins
x_wins = 0
o_wins = 0

k1 = tk.StringVar(value=field[0][0])
k2 = tk.StringVar(value=field[0][1])
k3 = tk.StringVar(value=field[0][2])
k4 = tk.StringVar(value=field[1][0])
k5 = tk.StringVar(value=field[1][1])
k6 = tk.StringVar(value=field[1][2])
k7 = tk.StringVar(value=field[2][0])
k8 = tk.StringVar(value=field[2][1])
k9 = tk.StringVar(value=field[2][2])


kachel1=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(0,0),textvariable=k1)         #1
kachel1.place(x=5,y=5,width=127,height=126)
kachel2=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(0,1),textvariable=k2)
kachel2.place(x=137,y=5,width=127,height=126)
kachel3=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(0,2),textvariable=k3)
kachel3.place(x=269,y=5,width=127,height=126)
kachel4=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(1,0),textvariable=k4)
kachel4.place(x=5,y=137,width=127,height=126)           #2
kachel5=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(1,1),textvariable=k5)
kachel5.place(x=137,y=137,width=127,height=126)
kachel6=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(1,2),textvariable=k6)
kachel6.place(x=269,y=137,width=127,height=126)
kachel7=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(2,0),textvariable=k7)
kachel7.place(x=5,y=269,width=127,height=126)           #3
kachel8=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(2,1),textvariable=k8)
kachel8.place(x=137,y=269,width=127,height=126)
kachel9=tk.Button(master=spielbrett,bg="white",command=lambda:setzen(2,2),textvariable=k9)
kachel9.place(x=269,y=269,width=127,height=126)

resetbutton=tk.Button(master=infoscreen,bg="grey",text="reset",command=reset)
resetbutton.place(x=260,y=5,height=50,width=136)

ausgabe=tk.Label(master=infoscreen,bg="grey",text="X ist dran")
ausgabe.place(x=5,y=5,height=50,width=136)

ausgabe2=tk.Label(master=infoscreen,bg="grey",text="X:0  O:0")
ausgabe2.place(x=150,y=5,height=50,width=100)

spielbrett.pack(pady=25,side="bottom")
infoscreen.pack(side="bottom")
if __name__ == "__main__":
    tk.mainloop()