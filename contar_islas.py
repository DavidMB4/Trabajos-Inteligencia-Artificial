matriz = [
    [0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

limite_x = len(matriz) 
limite_y = len (matriz[0])
total = 0

def recorrer(x, y):
    if matriz[x][y] == 1:
        matriz[x][y] = 0
        if x+1 < limite_x:
            recorrer(x+1, y) #Revisar a la derecha
        if x-1 >= 0:
            recorrer(x-1, y) #Revisar a la izquierda
        if y+1 < limite_y:
            recorrer(x, y+1) #Revisar a la arriba
        if y-1 >= 0:
            recorrer(x, y-1) #Revisar a la abajo

for i in range(len(matriz)):
    for n in range(len(matriz[0])):
        if matriz[i][n]:
            total += 1
            recorrer(i, n)

print(f"El numero de islas es: {total}")
