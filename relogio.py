# o asteristico, significa importar all, tudo

from tkinter import *
from tkinter.ttk import *
from time import strftime #pegando do próprio python a biblioteca time, o strftime que serve para pegar a hora atual do sistema que você ta usando, hora ao vivo


#tkinter vai ser a biblioteca pra dar tela, o display bonitinho

root = Tk()
root.title("Relógio")

def relogio():
    horario = strftime("%H:%M:%S")
    label.config(text =horario)
    label.after(1000, relogio)


label = Label(root, font=("Helvetica", 80), background="#000", foreground="#00FF04")

label.pack(anchor="center")

relogio ()
mainloop ()
