import tkinter as tk
from tkinter import *
import secrets
import pyperclip as pc

# VENTANA #
ventana = tk.Tk()
ventana.title('Generador de contraseñas')
ventana.geometry('640x480+300+100')
ventana.resizable(False, False)
ventana.config(bg='light sky blue')

# VARIABLES #
senha = ''
letras_down = 'abcdefghijklmnopqrstuvwxyz'
letras_up = letras_down.upper()
num = '1234567890'
caracteres = '#$%&()*+,-./:;<=>?@[]^_`{|}~'
vs_letra_up = IntVar()
vs_letra_down = IntVar()
vs_num = IntVar()
vs_caracteres = IntVar()
longitudes = StringVar()


# FUNCIONES #


def validar_check():
    if vs_letra_up.get() == 1 and vs_letra_down.get() == 1 and vs_caracteres.get() == 1 and vs_num.get() == 1:
        todo = letras_up + letras_down + num + caracteres
    elif vs_letra_up.get() == 1 and vs_letra_down.get() == 1 and vs_caracteres.get() == 1:
        todo = letras_up + letras_down + caracteres
    elif vs_letra_up.get() == 1 and vs_letra_down.get() == 1 and vs_num.get() == 1:
        todo = letras_up + letras_down + num
    elif vs_letra_up.get() == 1 and vs_caracteres.get() == 1 and vs_num.get() == 1:
        todo = letras_up + num + caracteres
    elif vs_letra_up.get() == 1 and vs_num.get() == 1:
        todo = letras_up + num
    elif vs_letra_up.get() == 1 and vs_caracteres.get() == 1:
        todo = letras_up + caracteres
    elif vs_letra_down.get() == 1 and vs_caracteres.get() == 1 and vs_num.get() == 1:
        todo = letras_down + num + caracteres
    elif vs_letra_down.get() == 1 and vs_caracteres.get() == 1:
        todo = letras_down + caracteres
    elif vs_letra_down.get() == 1 and vs_num.get() == 1:
        todo = letras_down + num
    elif vs_num.get() == 1 and vs_caracteres.get() == 1:
        todo = num + caracteres
    elif vs_letra_up.get() == 1 and vs_letra_down.get() == 1:
        todo = letras_up + letras_down
    elif vs_letra_up.get() == 1:
        todo = letras_up
    elif vs_letra_down.get() == 1:
        todo = letras_down
    elif vs_caracteres.get() == 1:
        todo = caracteres
    elif vs_num.get() == 1:
        todo = num
    elif vs_letra_up.get() == 0 and vs_letra_down.get() == 0 and vs_caracteres.get() == 0 and vs_num.get() == 0:
        todo = letras_up + letras_down + num + caracteres
    return todo


def generar_senhas():
    todo = validar_check()
    if int(longitudes.get()) < 8:
        longitudes.set('8')
    global senha
    senhas = ''.join(secrets.choice(todo) for i in range(int(longitudes.get())))
    senha = senhas
    rotulo_senha.config(text=senhas)


def copiar_senha():
    global senha
    pc.copy(senha)


# WIDGETS #
frame_titulo = tk.LabelFrame(ventana, bg='light sky blue')
frame_titulo.pack(pady=4, padx=5, ipadx=50)

rotulo_titulo = tk.Label(frame_titulo, text='GENERADOR\nDE\nCONTRASEÑAS SEGURAS',
                         font='arial 20 bold', bg='light sky blue')
rotulo_titulo.pack(pady=10, padx=110)

frame_senha = tk.LabelFrame(ventana, bg='light sky blue')
frame_senha.pack(padx=5, ipady=5, ipadx=157)

rotulo_senha = tk.Label(frame_senha, text='GENERAR PASSWORD', font='consolas 24 bold', bg='light sky blue', fg='green')
rotulo_senha.pack(padx=20, pady=20, side='left')

boton_copiar = tk.Button(frame_senha, text='Copiar', font='consoles 12 bold', command=copiar_senha)
boton_copiar.pack(pady=20, padx=10, side='right')

boton_generar = tk.Button(frame_senha, text='Generar', font='consoles 12 bold', command=generar_senhas)
boton_generar.pack(side='right', pady=20)

frame_opcion = tk.LabelFrame(ventana, bg='light sky blue')
frame_opcion.pack(pady=5, padx=5, ipadx=500, ipady=100)

rotulo_opciones = tk.Label(frame_opcion, text='PERSONALICE SU CONTRASEÑA', font='consolas 24 bold', bg='light sky blue')
rotulo_opciones.pack(padx=5, pady=5)

frame_opcion1 = tk.Frame(frame_opcion, bg='light sky blue')
frame_opcion1.pack(side='left', ipadx=100)

vs_letra_up.set(1)
opcion_letra_up = tk.Checkbutton(frame_opcion1, text='Letras Mayúsculas', bg='light sky blue', variable=vs_letra_up)
opcion_letra_up.pack(padx=5, pady=5, anchor='w')

vs_letra_down.set(1)
opcion_letra_down = tk.Checkbutton(frame_opcion1, text='Letras Minusculas', bg='light sky blue', variable=vs_letra_down)
opcion_letra_down.pack(padx=5, pady=5, anchor='w')

vs_num.set(1)
opcion_numeros = tk.Checkbutton(frame_opcion1, text='Números', bg='light sky blue', variable=vs_num)
opcion_numeros.pack(padx=5, pady=5, anchor='w')

vs_caracteres.set(1)
opcion_caracteres = tk.Checkbutton(frame_opcion1, text='Caracteres', bg='light sky blue', variable=vs_caracteres)
opcion_caracteres.pack(padx=5, pady=5, anchor='w')

frame_opcion2 = tk.Frame(frame_opcion, bg='light sky blue')
frame_opcion2.pack(side='left', ipady=50)

rotulo_longitud = tk.Label(frame_opcion2, text='Longitud de la contraseña', font='consolas 12 bold', bg='light sky blue')
rotulo_longitud.pack(pady=5, padx=5, anchor='w')

longitudes.set('16')
longitud = tk.Entry(frame_opcion2, font='consolas 12 bold', textvariable=longitudes, justify='center', width=10,)
longitud.pack(anchor='w')

# CICLO PRINCIPAL #
ventana.mainloop()
