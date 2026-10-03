import tkinter as tk
from tkinter import ttk, messagebox
import time
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fibonacci_dynamic(n):
    if n <= 0:
        return 0, 0
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    # Espacio aproximado en bytes ocupado por la estructura de memoización
    space_used = sys.getsizeof(memo)
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n], space_used

class DynamicFibApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci - Programación Dinámica (Optimizado)")
        self.root.geometry("850x650")
        
        title_label = tk.Label(root, text="Fibonacci con Programación Dinámica", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        frame_input = tk.Frame(root)
        frame_input.pack(pady=5)
        
        tk.Label(frame_input, text="Valor de n (soporta valores grandes, ej. 500):", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        self.entry_n = ttk.Entry(frame_input, width=10)
        self.entry_n.pack(side=tk.LEFT, padx=5)
        self.entry_n.insert(0, "50")
        
        btn_calc = ttk.Button(frame_input, text="Calcular y Graficar", command=self.calculate)
        btn_calc.pack(side=tk.LEFT, padx=10)
        
        self.info_label = tk.Label(root, text="", font=("Arial", 11, "bold"), fg="darkgreen")
        self.info_label.pack(pady=5)
        
        # Sub-frame para dos gráficas: Tiempo y Espacio
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def calculate(self):
        try:
            n_max = int(self.entry_n.get())
            if n_max < 0 or n_max > 900:
                messagebox.showerror("Error", "Ingresa un valor entre 0 y 900.")
                return
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número entero válido.")
            return
        
        ns = list(range(n_max + 1))
        times = []
        spaces = []
        
        for i in ns:
            start = time.perf_counter()
            res, space = fibonacci_dynamic(i)
            end = time.perf_counter()
            times.append((end - start) * 1_000_000) # microsegundos
            spaces.append(space)
            
        self.ax1.clear()
        self.ax1.plot(ns, times, marker='s', color='forestgreen', linestyle='-', linewidth=2)
        self.ax1.set_title("Complejidad de Tiempo O(n)")
        self.ax1.set_xlabel("n")
        self.ax1.set_ylabel("Tiempo (μs)")
        self.ax1.grid(True, linestyle='--', alpha=0.6)
        
        self.ax2.clear()
        self.ax2.plot(ns, spaces, marker='^', color='dodgerblue', linestyle='-', linewidth=2)
        self.ax2.set_title("Complejidad de Espacio O(n)")
        self.ax2.set_xlabel("n")
        self.ax2.set_ylabel("Memoria (Bytes)")
        self.ax2.grid(True, linestyle='--', alpha=0.6)
        
        self.fig.tight_layout()
        self.canvas.draw()
        
        final_res, final_space = fibonacci_dynamic(n_max)
        self.info_label.config(text=f"Fib({n_max}) = {final_res} | Memoria utilizada: {final_space} bytes")

if __name__ == "__main__":
    root = tk.Tk()
    app = DynamicFibApp(root)
    root.mainloop()