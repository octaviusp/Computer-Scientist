def ordenar(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if (arr[x] < arr[y]):
                aux = arr[y]
                arr[y] = arr[x]
                arr[x] = aux
    return arr

lista = [5,6,2,3]

print(ordenar(lista))
"""
1: arr[x] = 5 -> lista = [2,6,3,5]
2: arr[x] = 6 -> lista = [2,3,5,6]
3: arr[x] = 2 -> lista = [2,3,5,6]
4: arr[x] = 3 -> lista = [2,3,5,6]
"""