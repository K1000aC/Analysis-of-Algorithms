import tkinter as tk
import matplotlib.pyplot as plt

x = [3, 4, 5, 6, 7]
y = [10, 12, 14, 16, 18]

plt.plot(x, y)
plt.scatter(x, y, color='purple') #Gráfica de puntos
#plt.bar(x, y, color='lightpink') #Gráfica de barras
plt.title("Mi primera Gráfica")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "mundo"
    lbl.config(text=f"Hola Compa, {nombre}!!")

root=tk.Tk()
root.title("Saludador - My First GUI")
root.geometry("500x600")
lbl = tk.Label(root, text="Eh compa escribe tu nombre y presiona el botón",background="lightpink", foreground="white", font=("Arial Rounded MT Bold", 16))
lbl.pack(pady=20)
entrada = tk.Entry(root, foreground ="pink", font=("Arial Rounded MT Bold", 12))
entrada.pack(pady=10)
bot = tk.Button(root, text="Saludar", command=saludar, font=("Arial Rounded MT Bold", 12))
bot.pack(pady=10)

root.mainloop()

