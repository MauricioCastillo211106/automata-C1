import urllib.request
from bs4 import BeautifulSoup
import re
import sys
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import numpy as np

# iniciamos interfaz


def interfaz():

    # iniciamos ventana
    ventana = tk.Tk()
    ventana.title("Automata")
    ventana.geometry("700x400")
    ventana.iconbitmap("assets/imgs/icon.ico")

   # ventana.config(bg="assets/imgs/Polygon Luminary.png")
    ventana.resizable(width=False, height=False)

    usuario = tk.StringVar()
    # colores
    fondoBtn = "#00c2cb"
    textColor = "#FFFFFF"
    # Fondo
    fondoEntrar = PhotoImage(file="assets/imgs/Polygon_Luminary.png")
    background = Label(image=fondoEntrar)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    # Label
    entrada = tk.Entry(ventana, textvar=usuario, width=75,
                       relief="flat", bg=textColor)

    entrada.place(x=125, y=230)

    def sacarvalor():
        print(f"esto trae usuario {usuario.get()}")
        urlvalo = usuario.get()
        usuario.set('')
        lecturaPaginaWeb(urlvalo)
        # Botones
    boton = tk.Button(ventana, text="lectura", cursor="hand2", command=sacarvalor,
                      bg=fondoBtn, width=12, relief="flat", font=("Comic Sans MS", 12, "bold"))
    boton.place(x=300, y=300)

    ventana.mainloop()

# AFD


# Lista de los telefonos encontrados
telefonosEncontrados = []

# creacion de la funcion para leer la web


def lecturaPaginaWeb(urlObtenido):
    urlObtenido = urlObtenido

    with urllib.request.urlopen(urlObtenido) as url:
        s = url.read()
        try:
            soup = BeautifulSoup(s)
        except:
            print("esta mal")

    for script in soup(["script", "styles"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    # escritura en el txt
    try:
        with open('recopilacion.txt', 'w') as f:
            f.write(text)
            f.close()

    except:
        valordeverdad = False

    with open('recopilacion.txt') as archivo:
        print(type(archivo))
        for linea in archivo:
            # print(linea)
            if "@" in linea:
                telefonosEncontrados.append(linea)
                print(telefonosEncontrados.append(linea))
  ##  borardatosdeltxt()

    def borardatosdeltxt():
        with open('telefonosObtenidos.txt', 'w'):
            pass


# inicia la interfaz
if __name__ == '__main__':
    interfaz()
