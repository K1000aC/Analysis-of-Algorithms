import tkinter as tk
from tkinter import ttk, messagebox
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fib_brute(n):
    if n <= 0: return 0
    elif n == 1: return 1
    return fib_brute(n-1) + fib_brute(n-2)

def fib_dynamic(n):
    if n <= 0: return 0
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

class ComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparativa: Fibonacci Fuerza Bruta vs Programación Dinámica")
        self.root.geometry("900x650")
        
        title_label = tk.Label(root, text="Comparativa de Rendimiento: Fibonacci", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        frame_input = tk.Frame(root)
        frame_input.pack(pady=5)
        
        tk.Label(frame_input, text="Valor máximo de n para comparar (recomendado <= 30):", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        self.entry_n = ttk.Entry(frame_input, width=10)
        self.entry_n.pack(side=tk.LEFT, padx=5)
        self.entry_n.insert(0, "25")
        
        btn_calc = ttk.Button(frame_input, text="Ejecutar Comparativa", command=self.compare)
        btn_calc.pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(root, text="", font=("Arial", 11))
        self.info_label.pack(pady=5)
        
        self.fig, self.ax = plt.subplots(figsize=(7, 4.5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def compare(self):
        try:
            n_max = int(self.entry_n.get())
            if n_max < 0 or n_max > 32:
                messagebox.showerror("Error", "Para comparar con fuerza bruta, usa un n máximo de 32 para evitar bloqueos por crecimiento exponencial.")
                return
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido.")
            return
        
        ns = list(range(n_max + 1))
        times_brute = []
        times_dynamic = []
        
        for i in ns:
            # Medir fuerza bruta
            start = time.perf_counter()
            fib_brute(i)
            end = time.perf_counter()
            times_brute.append((end - start) * 1000) # ms
            
            # Medir dinamico
            start = time.perf_counter()
            fib_dynamic(i)
            end = time.perf_counter()
            times_dynamic.append((end - start) * 1000) # ms
            
        self.ax.clear()
        self.ax.plot(ns, times_brute, marker='o', color='red', label='Fuerza Bruta O(2^n)', linewidth=2)
        self.ax.plot(ns, times_dynamic, marker='s', color='blue', label='Programación Dinámica O(n)', linewidth=2)
        self.ax.set_title("Comparativa de Tiempos de Ejecución")
        self.ax.set_xlabel("n")
        self.ax.set_ylabel("Tiempo (ms)")
        self.ax.legend()
        self.ax.grid(True, linestyle='--', alpha=0.6)
        self.canvas.draw()
        
        self.info_label.config(text=f"Comparación completada para n={n_max}. Observa la diferencia abrumadora de escalas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ComparisonApp(root)
    root.mainloop()