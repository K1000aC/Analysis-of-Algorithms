import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Para cargar el archivo CSV
df = pd.read_csv('mnist_train.csv') 

# Para la SEparación de etiquetas y características  
y = df['label'].values                  # Vector de etiquetas (0, 1, 2..., 9)
X = df.drop('label', axis=1).values     #Matriz de caracteristicas (784 píxeles por fila)

# Normalización de los datos
X_norm = X / 255.0

#Creación del modelo t-SNE
tsne_global = TSNE(
    n_components=2,
    perplexity=30,
    random_state=42,
    n_jobs=-1
)


# Calculo del nuevo espacio 2D
X_embedded_global = tsne_global.fit_transform(X_norm)

# Graficación 
plt.figure(figsize=(10,8))
scatter = plt.scatter(
    X_embedded_global[:,0],
    X_embedded_global[:,1],
    c=y,
    cmap= 'tab10',
    alpha=0.6,
    s=10,
)

plt.colorbar(scatter, ticks=range(10), label='Dígito')
plt.title('Proyección t-SNE Global de MNIST')
plt.xlabel('Componente t-SNE 1')
plt.ylabel('Componente t-sne 2')
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()

#Para filtrar el dígito 7 mediante una máscara booleana 
mask_7 = (y == 7)
X_7 = X_norm[mask_7]

# Configuración y ejecución de t-SNE exclusivo para el dígito 7
tsne_7 = TSNE(
    n_components=2,
    perplexity=30,
    random_state=42,
    n_jobs=-1
)
X_embedded_7 = tsne_7.fit_transform(X_7)

# Grafciación del dígito 7
plt.figure(figsize=(8,6))
plt.scatter(
    X_embedded_7[:,0],
    X_embedded_7[:,1],
    color='purple',
    alpha=0.6,
    s=15
)
plt.title('Estructura Interna del Dígito 7 (t-SNE Aislado)')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()