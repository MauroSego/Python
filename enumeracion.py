objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    #print(f'{respuesta} -> {respuesta**2}') #Paso a paso de como llegó al objetivo
    respuesta += 1


if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else: 
    print(f'{objetivo} no tiene una raiz cuadrada exacta')

#Con este algoritmo lo que se hace es probar todas las posibilidades, por ejemplo probamos cual es la raiz de un entero pasando por todos los enteros anteriores