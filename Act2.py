def insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >=0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave

# Lista desordenada
lista_insercion = [12, 11, 13, 5, 6]
insercion(lista_insercion)
print("Lista ordenada con inserción:", lista_insercion)