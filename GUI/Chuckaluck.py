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
        ausgabe2.config(text="Game Over")
        return 
    elif einsatz>kontoinhalt:
        ausgabe2.config(text="zu hoher Einsatz")
        return 
    ausgabe2.config(text="")

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
    
    kontoinhalt = int(kontostand.cget("text"))
    if kontoinhalt <=0:
        ausgabe2.config(text="Game Over")

    würfel1.config(text=f"{number1}")
    würfel2.config(text=f"{number2}")
    würfel3.config(text=f"{number3}")

def lightmode():

    if fenster.cget("bg")!="white":
        bg_color_l="white"
        fg_color_l="black"
        sel_color_l="lightgrey"
        scale_bg_color_l="lightgrey"
        bg_color2="black"
        modebutton.config(text="darkmode")
        colorchange(bg_color_l,fg_color_l,sel_color_l,scale_bg_color_l,bg_color2)
    else:
        bg_color_d="#2f4f4f"
        fg_color_d="black"
        sel_color_d="black"
        scale_bg_color_d="#97FFFF"
        bg_color2="#97FFFF"
        modebutton.config(text="lightmode")
        colorchange(bg_color_d,fg_color_d,sel_color_d,scale_bg_color_d,bg_color2)

def colorchange(bg_color,fg_color,sel_color,scale_bg_color,bg_color2):
    scale.config(background=bg_color, fg=bg_color2,troughcolor=scale_bg_color)
    fenster.config(bg=bg_color)
    würfel1.config(bg=scale_bg_color)
    würfel2.config(bg=scale_bg_color)
    würfel3.config(bg=scale_bg_color)
    ausgabe.config(bg=bg_color,fg=bg_color2)
    ausgabe2.config(bg=bg_color,fg=bg_color2)
    resetbutton.config(fg=fg_color)
    würfel_titel.config(fg=fg_color,background=scale_bg_color)
    wuerfelbutton.config(fg=fg_color,bg=scale_bg_color)
    kontostand_titel.config(fg=bg_color2,bg=bg_color)
    kontostand.config(fg=bg_color2,bg=bg_color)
    runden.config(fg=bg_color2,bg=bg_color)
    runden_titel.config(fg=bg_color2,bg=bg_color)
    schieber_beschreibung.config(fg=bg_color2,bg=bg_color)
    mehrfach_button.config(fg=fg_color,bg=scale_bg_color)
    auswahlbutton.config(fg=fg_color,bg=scale_bg_color)
    auswahlbutton2.config(fg=fg_color,bg=scale_bg_color)
    resetbutton.config(fg=fg_color,bg=scale_bg_color)
    auswahloptions.config(background=bg_color,fg=bg_color2)
    auswahloptions2.config(background=bg_color,fg=bg_color2)
    auswahl1.config(bg=bg_color,fg=bg_color2,selectcolor=sel_color)
    auswahl2.config(bg=bg_color,fg=bg_color2,selectcolor=sel_color)
    auswahl3.config(bg=bg_color,fg=bg_color2,selectcolor=sel_color)
    auswahl4.config(bg=bg_color,fg=bg_color2,selectcolor=sel_color)
    auswahl5.config(bg=bg_color,fg=bg_color2,selectcolor=sel_color)
    auswahl6.config(bg=bg_color,fg=bg_color2,selectcolor=sel_color)
    modebutton.config(bg=scale_bg_color,fg=fg_color)
    ausgabefenster.config(bg=scale_bg_color)

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
    ausgabe.config(text="von Silas")
    ausgabe2.config(text="und Jan")
    resetbutton.config(text="reset")

def automatischeswürfeln():
    rundenzahl = würfelzahl.get()
    rundenstart = int(runden.cget("text"))
    kontoinhalt1 = int(kontostand.cget("text"))
    while int(kontostand.cget("text"))>=scale.get() and int(runden.cget("text"))-rundenstart<rundenzahl:
        if zufall.get():
            radio.set(random.randint(1,6))
        würfeln()
        einsatz = scale.get()
        kontoinhalt = int(kontostand.cget("text"))
        if kontoinhalt <=0:
            ausgabe2.config(text="Game Over")
            resetbutton.config(text="restart")
            kontoinhalt2 = int(kontostand.cget("text"))
            if kontoinhalt2-kontoinhalt1 >= 0:
                ausgabe.config(text=f"Gewonnen: {kontoinhalt2-kontoinhalt1}")
            else:
                ausgabe.config(text=f"Verlust: {kontoinhalt1-kontoinhalt2}")
            return 
        elif einsatz>kontoinhalt:
            ausgabe2.config(text="zu hoher Einsatz")
            kontoinhalt2 = int(kontostand.cget("text"))
            if kontoinhalt2-kontoinhalt1 >= 0:
                ausgabe.config(text=f"Gewonnen: {kontoinhalt2-kontoinhalt1}")
            else:
                ausgabe.config(text=f"Verlust: {kontoinhalt1-kontoinhalt2}")
            return 
    einsatz = scale.get()
    kontoinhalt = int(kontostand.cget("text"))
    if kontoinhalt <=0:
        ausgabe2.config(text="Game Over")
        resetbutton.config(text="restart")
        kontoinhalt2 = int(kontostand.cget("text"))
        return 
    elif einsatz>kontoinhalt:
        ausgabe2.config(text="zu hoher Einsatz")
        kontoinhalt2 = int(kontostand.cget("text"))
        return 
    kontoinhalt2 = int(kontostand.cget("text"))
    if kontoinhalt2-kontoinhalt1 >= 0:
        ausgabe.config(text=f"Gewonnen: {kontoinhalt2-kontoinhalt1}")
    else:
        ausgabe.config(text=f"Verlust: {kontoinhalt1-kontoinhalt2}")


def reload_menu():
    auswahlbutton.config(text=f"{würfelzahl.get()}x")
    if zufall.get():
        auswahlbutton2.config(text="random")
        return
    auswahlbutton2.config(text="set")


bg_color="#2f4f4f"
fg_color="#97FFFF"
sel_color="black"
scale_bg_color="#90E0F0"
bg_color2="#97FFFF"

fenster = Tk()
fenster.config(background=bg_color)
fenster.title("Chuckaluck")
fenster.geometry("400x270")

würfel_titel = Label(master=fenster,text="würfel",background=fg_color)
würfel_titel.place(x=10, y=10, width=100, height=25)

modebutton = Button(text="darkmode", command=lightmode)
modebutton.place(x=300, y=220, width=70 , height=25)

würfel1 = Label(master=fenster,text="",background=fg_color)
würfel1.place(x=10, y=40, width=30, height=30)
würfel2 = Label(master=fenster,text="",background=fg_color)
würfel2.place(x=45, y=40, width=30, height=30)
würfel3 = Label(master=fenster,text="",background=fg_color)
würfel3.place(x=80, y=40, width=30, height=30)

kontostand_titel = Label(master=fenster,text="Kontostand:", background=bg_color, fg=fg_color)
kontostand_titel.place(x=120,y=10, width=100, height=25)
kontostand = Label(master=fenster,text="100", background=bg_color, fg=fg_color)
kontostand.place(x=200,y=10, width=42, height=25)

runden_titel = Label(master=fenster,text="Runden:", background=bg_color, fg=fg_color)
runden_titel.place(x=120,y=30, width=100, height=25)
runden = Label(master=fenster,text="0", background=bg_color, fg=fg_color)
runden.place(x=200,y=30, width=42, height=25)

radio = IntVar()
auswahl1 = Radiobutton(master=fenster,text='1',value=1,variable=radio, background=bg_color, fg=fg_color,selectcolor=sel_color)
auswahl1.place(x=300,y=100, width=42, height=20)
auswahl2 = Radiobutton(master=fenster,text='2',value=2,variable=radio, background=bg_color, fg=fg_color,selectcolor=sel_color)
auswahl2.place(x=300,y=120, width=42, height=20)
auswahl3 = Radiobutton(master=fenster,text='3',value=3,variable=radio, background=bg_color, fg=fg_color,selectcolor=sel_color)
auswahl3.place(x=300,y=140, width=42, height=20)
auswahl4 = Radiobutton(master=fenster,text='4',value=4,variable=radio, background=bg_color, fg=fg_color,selectcolor=sel_color)
auswahl4.place(x=300,y=160, width=42, height=20)
auswahl5 = Radiobutton(master=fenster,text='5',value=5,variable=radio, background=bg_color, fg=fg_color,selectcolor=sel_color)
auswahl5.place(x=300,y=180, width=42, height=20)
auswahl6 = Radiobutton(master=fenster,text='6',value=6,variable=radio, background=bg_color, fg=fg_color,selectcolor=sel_color)
auswahl6.place(x=300,y=200, width=42, height=20)
auswahl1.select()

wuerfelbutton = Button(master=fenster, command=würfeln, background=fg_color)
wuerfelbutton.config(text="würfeln")
wuerfelbutton.place(x=10, y=75, width=100, height=20)

würfelzahl=IntVar()
zufall = BooleanVar()
mehrfach_button = Button(master=fenster,text="Mehrfach Würfeln",command=automatischeswürfeln,background=fg_color)
mehrfach_button.place(x=250,y=10, width=110, height=25)

auswahlbutton = Menubutton(master=fenster, text="10x",relief=RAISED,background=fg_color)
auswahlbutton.place(x=250,y=40, width=52, height=25)
auswahloptions = Menu(auswahlbutton,background="#2f4f4f",foreground=fg_color)
auswahlbutton.config(menu=auswahloptions)
auswahloptions.add_radiobutton(label="10",value=10,variable=würfelzahl,command=reload_menu)
auswahloptions.add_radiobutton(label="100",value=100,variable=würfelzahl,command=reload_menu)
würfelzahl.set(10)

auswahlbutton2 = Menubutton(master=fenster, text="random",relief=RAISED,background=fg_color)
auswahlbutton2.place(x=250,y=70, width=52, height=25)
auswahloptions2 = Menu(auswahlbutton2,background="#2f4f4f",foreground=fg_color)
auswahlbutton2.config(menu=auswahloptions2)
auswahloptions2.add_radiobutton(label="random",value=True,variable=zufall,command=reload_menu)
auswahloptions2.add_radiobutton(label="set",value=False,variable=zufall,command=reload_menu)
zufall.set(True)

schieber = IntVar()
scale = Scale(master=fenster,variable=schieber,orient=HORIZONTAL,from_=1,to=100,relief=RAISED, background=bg_color, fg=fg_color,troughcolor=fg_color)
scale.place(x=120,y=55, width=120, height=55)
schieber_beschreibung = Label(master=fenster,text="Einsatzhöhe", background=bg_color, fg=fg_color)
schieber_beschreibung.place(x=120,y=92, width=120, height=25)


ausgabefenster = Frame(master=fenster,bg = bg_color)
ausgabefenster.place(x=5,y=115,width=260,height=130)

ausgabe = Label(master=fenster,text="von Silas",background=bg_color,font=("",25), fg=fg_color)
ausgabe.place(x=10, y=120, width=250 , height=60)
ausgabe2 = Label(master=fenster,text="und Jan",background=bg_color,font=("",25), fg=fg_color)
ausgabe2.place(x=10, y=180, width=250 , height=60)

resetbutton = Button(master=fenster,text="reset",command=reset,background=fg_color)
resetbutton.place(x=318,y=40, width=42, height=25)

lightmode()
fenster.mainloop()
