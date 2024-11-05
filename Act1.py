def burbuja(arr):
    n = len(arr)
    for i in range(n):
        intercambiado = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambiado = True
        if not intercambiado:
            break

lista_burbuja = [64, 34, 25, 12, 22, 11, 90]
burbuja(lista_burbuja)
print("Lista ordenada con burbuja:", lista_burbuja)
