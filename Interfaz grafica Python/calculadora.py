import tkinter as tk
from tkinter import *

calculadora = Tk()
calculadora.geometry("300x370")
calculadora.resizable(0, 0)

resultado = ""
texto_pantalla = StringVar()

def clear():
    global resultado
    resultado = ""
    texto_pantalla.set("0")

def mostrar(a):
    global resultado
    resultado += str(a)
    texto_pantalla.set(resultado)

def resul():
    global resutado
    try:
        d = str(eval(resultado))
    except:
        d = "Sintax ERROR"
    texto_pantalla.set(d)

resultadov = Entry(calculadora, textvariable=texto_pantalla)
resultadov.pack()
resultadov.place(x=0, y=0, width=300, height=70)

num7 = Button(calculadora, text="7", font=30, command=lambda: mostrar(7))
num7.pack()
num7.place(x=0, y=70, width=75, height=75)

num8 = Button(calculadora, text="8", font=30, command=lambda: mostrar(8))
num8.pack()
num8.place(x=75, y=70, width=75, height=75)

num9 = Button(calculadora, text="9", font=30, command=lambda: mostrar(9))
num9.pack()
num9.place(x=150, y=70, width=75, height=75)

multi = Button(calculadora, text="*", font=30, command=lambda: mostrar("*"))
multi.pack()
multi.place(x=225, y=70, width=75, height=75)

num4 = Button(calculadora, text="4", font=30, command=lambda: mostrar(4))
num4.pack()
num4.place(x=0, y=145, width=75, height=75)

num5 = Button(calculadora, text="5", font=30, command=lambda: mostrar(5))
num5.pack()
num5.place(x=75, y=145, width=75, height=75)

num6 = Button(calculadora, text="6", font=30, command=lambda: mostrar(6))
num6.pack()
num6.place(x=150, y=145, width=75, height=75)

resta = Button(calculadora, text="-", font=30, command=lambda: mostrar("-"))
resta.pack()
resta.place(x=225, y=145, width=75, height=75)

num1 = Button(calculadora, text="1", font=30, command=lambda: mostrar(1))
num1.pack()
num1.place(x=0, y=220, width=75, height=75)

num2 = Button(calculadora, text="2", font=30, command=lambda: mostrar(2))
num2.pack()
num2.place(x=75, y=220, width=75, height=75)

num3 = Button(calculadora, text="3", font=30, command=lambda: mostrar(3))
num3.pack()
num3.place(x=150, y=220, width=75, height=75)

suma = Button(calculadora, text="+", font=30, command=lambda: mostrar("+"))
suma.pack()
suma.place(x=225, y=220, width=75, height=75)

punto = Button(calculadora, text=".", font=30, command=lambda: mostrar("."))
punto.pack()
punto.place(x=0, y=295, width=75, height=75)

num0 = Button(calculadora, text="0", font=30, command=lambda: mostrar(0))
num0.pack()
num0.place(x=75, y=295, width=75, height=75)

division = Button(calculadora, text="/", font=30, command=lambda: mostrar("/"))
division.pack()
division.place(x=150, y=295, width=75, height=75)

igual = Button(calculadora, text="=", font=30, command=resul)
igual.pack()
igual.place(x=225, y=295, width=75, height=75)

borrar = Button(calculadora, text="C", font=30, command=clear)
borrar.pack()
borrar.place(x=225, y=0, width=75, height=70)








calculadora.mainloop()