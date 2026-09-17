import tkinter as tk
import copy
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import time
from BubbleSort import bubble_sort
from Exchange_sort import exchange_sort
from Gnome_sort import gnome_sort
from Insertion_sort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from Randomm import generate
from SelectionSort import selection_sort


ALGORITMOS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Exchange Sort": exchange_sort,
    "Gnome Sort": gnome_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

def medir_tiempo(algoritmo, datos):
    inicio = time.perf_counter()
    algoritmo(datos)
    return time.perf_counter() - inicio


def obtener_parametros():
    inicio = int(entrada_inicio.get() or 30)
    incremento = int(entrada_incremento.get() or 20)
    fin = int(entrada_fin.get() or 100)

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
    tiempos = {nombre: [] for nombre in ALGORITMOS}

    for n in range(inicio, fin + 1, incremento):
        datos = generate(n, 1, 100)
        tamanios.append(n)
        for nombre, algoritmo in ALGORITMOS.items():
            tiempos[nombre].append(medir_tiempo(algoritmo, copy.copy(datos)))

    graficar(tamanios, tiempos)
    mensaje.config(text="Comparación completada.", foreground="green")


def graficar(tamanios, tiempos):
    plt.figure()
    for nombre, resultados in tiempos.items():
        plt.plot(tamanios, resultados, marker="o", label=nombre)

    plt.title("Comparación de algoritmos de ordenamiento")
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

mensaje = tk.Label(root, text="Deja un campo vacío para usar sus valores predeterminados.")
mensaje.pack(pady=5)

root.mainloop()
