def merge_sort(arr):
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(arr) <= 1:
        return

    # 1. DIVIDE: Encontrar el punto medio y dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. VENCE: Llamadas recursivas para ordenar cada mitad
    merge_sort(left_half)
    merge_sort(right_half)

    # 3. COMBINA (Merge): Fusionar las dos mitades ordenadas en la lista original
    i = j = k = 0

    # Comparar elementos de ambas mitades y colocar el menor en 'arr'
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Verificar si quedaron elementos en la mitad izquierda
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Verificar si quedaron elementos en la mitad derecha
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# --- Ejemplo de uso ---
if __name__ == "__main__":
    mi_lista = [38, 27, 43, 3, 9, 82, 10]
    print(f"Lista original: {mi_lista}")
    
    merge_sort(mi_lista)
    print(f"Lista ordenada: {mi_lista}")

