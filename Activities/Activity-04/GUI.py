import tkinter as tk
import copy
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import time
from BubbleSort import bubble_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from Randomm import generate
from SelectionSort import selection_sort

def medir_tiempo(algoritmo, datos):
    inicio = time.perf_counter()
    algoritmo(datos)
    return time.perf_counter() - inicio


def obtener_parametros():
    inicio = int(entrada_inicio.get() or 30)
    incremento = int(entrada_incremento.get() or 20)
    fin = int(entrada_fin.get() or 1000)

    if inicio <= 0 or incremento <= 0 or fin < inicio:
        raise ValueError("Usa valores positivos y un fin mayor o igual al inicio.")

    return inicio, incremento, fin


def comparar():
    try:
        inicio, incremento, fin = obtener_parametros()
    except ValueError as error:
        mensaje.config(text=str(error), foreground="red")
        return

    tamanios = []
    tiempos_bubble = []
    tiempos_selection = []
    tiempos_merge = []
    tiempos_quick = []

    for n in range(inicio, fin + 1, incremento):
        datos = generate(n, 1, 100)
        tamanios.append(n)
        tiempos_bubble.append(medir_tiempo(bubble_sort, copy.copy(datos)))
        tiempos_selection.append(medir_tiempo(selection_sort, copy.copy(datos)))
        tiempos_merge.append(medir_tiempo(merge_sort, copy.copy(datos)))
        tiempos_quick.append(medir_tiempo(quick_sort, copy.copy(datos)))

    graficar(tamanios, tiempos_bubble, tiempos_selection, "Fuerza Bruta")
    graficar(tamanios, tiempos_merge, tiempos_quick, "Divide y Vencerás")
    mensaje.config(text="Comparación completada.", foreground="green")


def graficar(tamanios, tiempos_primero, tiempos_segundo, categoria):
    nombres = {
        "Fuerza Bruta": ("Bubble Sort", "Selection Sort"),
        "Divide y Vencerás": ("Merge Sort", "Quick Sort"),
    }

    plt.figure()
    plt.plot(tamanios, tiempos_primero, marker="o", label=nombres[categoria][0])
    plt.plot(tamanios, tiempos_segundo, marker="o", label=nombres[categoria][1])
    plt.title(f"Comparación: {categoria}")
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

mensaje = tk.Label(root, text="Deja un campo vacío para usar su valor predeterminado.")
mensaje.pack(pady=5)

root.mainloop()
