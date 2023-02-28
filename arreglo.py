def encontrar_minimo(arr):
    minimo = arr[0]
    for num in arr:
        if num < minimo:
            minimo = num
    return minimo
    
a = [2,3,5,7,8,1]

print("El numero menor del arreglo es: ", encontrar_minimo(a))
