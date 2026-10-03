import tkinter as tk
from tkinter import ttk, messagebox
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fibonacci_brute(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_brute(n - 1) + fibonacci_brute(n - 2)

class BruteForceFibApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci - Fuerza Bruta (Sin Programación Dinámica)")
        self.root.geometry("800x600")
        
        title_label = tk.Label(root, text="Fibonacci por Fuerza Bruta", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        frame_input = tk.Frame(root)
        frame_input.pack(pady=5)
        
        tk.Label(frame_input, text="Valor de n (máx recomendado ~30):", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        self.entry_n = ttk.Entry(frame_input, width=10)
        self.entry_n.pack(side=tk.LEFT, padx=5)
        self.entry_n.insert(0, "20")
        
        btn_calc = ttk.Button(frame_input, text="Calcular y Graficar", command=self.calculate)
        btn_calc.pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(root, text="", font=("Arial", 11))
        self.info_label.pack(pady=5)
        
        # Frame para gráfica
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def calculate(self):
        try:
            n_max = int(self.entry_n.get())
            if n_max < 0 or n_max > 35:
                messagebox.showerror("Error", "Por favor ingresa un valor entre 0 y 35 (la fuerza bruta crece exponencialmente O(2^n)).")
                return
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido.")
            return
        
        ns = list(range(n_max + 1))
        times = []
        
        for i in ns:
            start = time.perf_counter()
            fibonacci_brute(i)
            end = time.perf_counter()
            times.append((end - start) * 1000) # en milisegundos
            
        self.ax.clear()
        self.ax.plot(ns, times, marker='o', color='crimson', linestyle='-', linewidth=2)
        self.ax.set_title("Tiempo de Ejecución - Fuerza Bruta O(2^n)")
        self.ax.set_xlabel("n")
        self.ax.set_ylabel("Tiempo (ms)")
        self.ax.grid(True, linestyle='--', alpha=0.6)
        self.canvas.draw()
        
        self.info_label.config(text=f"Cálculo completado para n={n_max}. Tiempo exponencial observado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceFibApp(root)
    root.mainloop()