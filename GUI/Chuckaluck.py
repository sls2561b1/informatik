from tkinter import *
import random

def würfeln():
    einsatz = scale.get()
    kontoinhalt = int(kontostand.cget("text"))
    try:
        eingabefeld_wert = radio.get()
    except:
        return
    if kontoinhalt <=0:
        ausgabe.config(text="Game Over")
        return 
    elif einsatz>kontoinhalt:
        ausgabe.config(text="zu hoher Einsatz")
        return 

    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    number3 = random.randint(1,6)

    gleich = False
    kontoinhalt_zwischenspeicher = kontoinhalt
    if number1==eingabefeld_wert:
        kontoinhalt=kontoinhalt+einsatz
        gleich = True
    if number2==eingabefeld_wert:
        kontoinhalt=kontoinhalt+einsatz
        gleich = True
    if number3==eingabefeld_wert:
        kontoinhalt=kontoinhalt+einsatz
        gleich = True
    if not gleich:
        kontoinhalt = kontoinhalt-einsatz
    
    if kontoinhalt-kontoinhalt_zwischenspeicher > 0:
        ausgabe.config(text=f"Gewinn: {kontoinhalt-kontoinhalt_zwischenspeicher}")
    else:
        ausgabe.config(text=f"Verlust: {kontoinhalt_zwischenspeicher-kontoinhalt}")

    kontostand.config(text=f"{kontoinhalt}")
    rundenanzahl = int(runden.cget("text"))+1
    runden.config(text=f"{rundenanzahl}")

    würfel1.config(text=f"{number1}")
    würfel2.config(text=f"{number2}")
    würfel3.config(text=f"{number3}")

def reset():
    scale.set(1)
    kontostand.config(text="100")
    runden.config(text="0")
    würfel1.config(text="")
    würfel2.config(text="")
    würfel3.config(text="")
    würfelzahl.set(10)
    zufall.set(True)
    reload_menu()
    auswahl1.select()
    ausgabe.config(text="output")

def automatischeswürfeln():
    rundenzahl = würfelzahl.get()
    rundenstart = int(runden.cget("text"))
    while int(kontostand.cget("text"))>=scale.get() and int(runden.cget("text"))-rundenstart<rundenzahl:
        if zufall.get():
            radio.set(random.randint(1,6))
        würfeln()
        einsatz = scale.get()
        kontoinhalt = int(kontostand.cget("text"))
        if kontoinhalt <=0:
            ausgabe.config(text="Game Over")
            return 
        elif einsatz>kontoinhalt:
            ausgabe.config(text="zu hoher Einsatz")
            return 

def reload_menu():
    auswahlbutton.config(text=f"{würfelzahl.get()}x")
    if zufall.get():
        auswahlbutton2.config(text="random")
        return
    auswahlbutton2.config(text="set")

fenster = Tk()
fenster.config(background="#2f4f4f")
fenster.title("Suckaluck")
fenster.geometry("400x300")

würfel_titel = Label(master=fenster,text="würfel",background="#97FFFF")
würfel_titel.place(x=10, y=10, width=100, height=25)

würfel1 = Label(master=fenster,text="",background="#97FFFF")
würfel1.place(x=10, y=40, width=30, height=30)
würfel2 = Label(master=fenster,text="",background="#97FFFF")
würfel2.place(x=45, y=40, width=30, height=30)
würfel3 = Label(master=fenster,text="",background="#97FFFF")
würfel3.place(x=80, y=40, width=30, height=30)

kontostand_titel = Label(master=fenster,text="Kontostand:", background="#2f4f4f", fg="#97FFFF")
kontostand_titel.place(x=120,y=10, width=100, height=25)
kontostand = Label(master=fenster,text="100", background="#2f4f4f", fg="#97FFFF")
kontostand.place(x=200,y=10, width=42, height=25)

runden_titel = Label(master=fenster,text="Runden:", background="#2f4f4f", fg="#97FFFF")
runden_titel.place(x=120,y=30, width=100, height=25)
runden = Label(master=fenster,text="0", background="#2f4f4f", fg="#97FFFF")
runden.place(x=200,y=30, width=42, height=25)

radio = IntVar()
auswahl1 = Radiobutton(master=fenster,text='1',value=1,variable=radio, background="#2f4f4f", fg="#97FFFF",selectcolor="black")
auswahl1.place(x=300,y=100, width=42, height=20)
auswahl2 = Radiobutton(master=fenster,text='2',value=2,variable=radio, background="#2f4f4f", fg="#97FFFF",selectcolor="black")
auswahl2.place(x=300,y=120, width=42, height=20)
auswahl3 = Radiobutton(master=fenster,text='3',value=3,variable=radio, background="#2f4f4f", fg="#97FFFF",selectcolor="black")
auswahl3.place(x=300,y=140, width=42, height=20)
auswahl4 = Radiobutton(master=fenster,text='4',value=4,variable=radio, background="#2f4f4f", fg="#97FFFF",selectcolor="black")
auswahl4.place(x=300,y=160, width=42, height=20)
auswahl5 = Radiobutton(master=fenster,text='5',value=5,variable=radio, background="#2f4f4f", fg="#97FFFF",selectcolor="black")
auswahl5.place(x=300,y=180, width=42, height=20)
auswahl6 = Radiobutton(master=fenster,text='6',value=6,variable=radio, background="#2f4f4f", fg="#97FFFF",selectcolor="black")
auswahl6.place(x=300,y=200, width=42, height=20)
auswahl1.select()

wuerfelbutton = Button(master=fenster, command=würfeln, background="#97FFFF")
wuerfelbutton.config(text="würfeln")
wuerfelbutton.place(x=10, y=75, width=100, height=20)

würfelzahl=IntVar()
zufall = BooleanVar()
kill_button = Button(master=fenster,text="Mehrfach Würfeln",command=automatischeswürfeln,background="#97FFFF")
kill_button.place(x=250,y=10, width=110, height=25)

auswahlbutton = Menubutton(master=fenster, text="10x",relief=RAISED,background="#97FFFF")
auswahlbutton.place(x=250,y=40, width=52, height=25)
auswahloptions = Menu(auswahlbutton)
auswahlbutton.config(menu=auswahloptions)
auswahloptions.add_radiobutton(label="10",value=10,variable=würfelzahl,command=reload_menu)
auswahloptions.add_radiobutton(label="100",value=100,variable=würfelzahl,command=reload_menu)
würfelzahl.set(10)

auswahlbutton2 = Menubutton(master=fenster, text="random",relief=RAISED,background="#97FFFF")
auswahlbutton2.place(x=250,y=70, width=52, height=25)
auswahloptions2 = Menu(auswahlbutton2)
auswahlbutton2.config(menu=auswahloptions2)
auswahloptions2.add_radiobutton(label="random",value=True,variable=zufall,command=reload_menu)
auswahloptions2.add_radiobutton(label="set",value=False,variable=zufall,command=reload_menu)
zufall.set(True)

schieber = IntVar()
scale = Scale(master=fenster,variable=schieber,orient=HORIZONTAL,from_=1,to=100,relief=RAISED, background="#2f4f4f", fg="#97FFFF")
scale.place(x=120,y=55, width=120, height=55)
schieber_beschreibung = Label(master=fenster,text="Einsatzhöhe", background="#2f4f4f", fg="#97FFFF")
schieber_beschreibung.place(x=120,y=92, width=120, height=25)

ausgabe = Label(master=fenster,text="output",background="#2f4f4f",font=("",25), fg="#97FFFF")
ausgabe.place(x=10, y=120, width=250 , height=60)

resetbutton = Button(master=fenster,text="reset",command=reset,background="#97FFFF")
resetbutton.place(x=318,y=40, width=42, height=25)

fenster.mainloop()
