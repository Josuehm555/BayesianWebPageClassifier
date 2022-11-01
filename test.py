import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import Tk, Frame, Button, Label, ttk, StringVar, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana=Tk()
ventana.geometry('655x505')
ventana.wm_title("URLs result")
ventana.minsize(width=655, height=505)
urlsGUI=[1,2,3]

var = StringVar()
cmb=ttk.Combobox(ventana,textvariable=var,value=urlsGUI,width=10)
cmb.grid(row=1,column=3)
cmb.place(x=500, y=0)
def showResults():
    messagebox.showinfo(message="Cant be determined", title=cmb.get())
btn = Button(ventana, text="Ok", command=showResults)
btn.grid(row=0, column=0)
btn.place(x=500, y=40)
ventana.mainloop()
ventana.mainloop()