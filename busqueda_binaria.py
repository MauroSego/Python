objetivo = int(input('Escoga un número: '))
epsilon = 0.0011

bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2
import time
start_time = time.time()

while abs(respuesta**2 - objetivo) >= epsilon: 
    print(f'bajo ={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta 
    else:
        alto = respuesta

    respuesta= (alto + bajo)/2

print(f'La raiz cuadrada del {objetivo} es el {respuesta}')
print("--- %s seconds ---" % (time.time()-start_time))