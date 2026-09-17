import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import time
from randomm import generate

# Algoritmos 
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def selection_sort(lista):

    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

# Comparación de tiempos de ejecución
def comparar():
    inicio = int(entrada_inicio.get())
    incremento = int(entrada_incremento.get())
    fin = int(entrada_fin.get())

    if inicio == "":
        inicio = 30
    else:
        inicio = int(inicio)

    if incremento == "":
        incremento = 20
    else:
        incremento = int(incremento)     

    if fin == "":
        fin = 1000
    else:
        fin = int(fin)       

    tamanios = []
    tiempos_bubble = []
    tiempos_selection = []

    for n in range(inicio, fin + 1, incremento):
        datos = generate(n, 1, 100)

        lista_bubble = datos.copy()
        lista_selection = datos.copy()

        #Bubble Sort
        tiempo_inicio = time.perf_counter()
        bubble_sort(lista_bubble)
        tiempo_fin = time.perf_counter()
        tiempo_bubble=(tiempo_fin - tiempo_inicio)

        #Selection Sort
        tiempo_inicio = time.perf_counter()
        selection_sort(lista_selection)
        tiempo_fin = time.perf_counter()
        tiempo_selection=(tiempo_fin - tiempo_inicio)

        #Guardar resultados
        tamanios.append(n)
        tiempos_bubble.append(tiempo_bubble)
        tiempos_selection.append(tiempo_selection)


    # Gráfica
    plt.figure()

    plt.plot(
        tamanios,
        tiempos_bubble,
        marker="o",
        label="Bubble Sort"
    )

    plt.plot(
        tamanios,
        tiempos_selection,
        marker="o",
        label="Selection Sort"
    )
    plt.title("Comparación de algoritmos")

    plt.xlabel("Tamaño de entrada n")

    plt.ylabel("Tiempo de ejecución (s)")

    plt.legend()

    plt.grid()

    plt.show()


# GUI

root = tk.Tk()

root.title("Comparación de Algoritmos")
root.geometry("500x600")

lbl = tk.Label(
    root,
    text="Comparación de algoritmos",
    background="lightpink",
    foreground="white",
    font=("Arial Rounded MT Bold", 16)
)
lbl.pack(pady=20)

lbl_inicio = tk.Label(
    root,
    text="Valor inicial:",
    font=("Arial Rounded MT Bold", 12)
)
lbl_inicio.pack(pady=5)


entrada_inicio = tk.Entry(
    root,
    foreground="pink",
    font=("Arial Rounded MT Bold", 12)
)
entrada_inicio.pack(pady=5)

lbl_incremento = tk.Label(
    root,
    text="Incremento:",
    font=("Arial Rounded MT Bold", 12)
)
lbl_incremento.pack(pady=5)


entrada_incremento = tk.Entry(
    root,
    foreground="pink",
    font=("Arial Rounded MT Bold", 12)
)
entrada_incremento.pack(pady=5)


lbl_fin = tk.Label(
    root,
    text="Valor final:",
    font=("Arial Rounded MT Bold", 12)
)
lbl_fin.pack(pady=5)


entrada_fin = tk.Entry(
    root,
    foreground="pink",
    font=("Arial Rounded MT Bold", 12)
)
entrada_fin.pack(pady=5)

bot = tk.Button(
    root,
    text="Comparar",
    command=comparar,
    font=("Arial Rounded MT Bold", 12)
)
bot.pack(pady=20)

root.mainloop()
