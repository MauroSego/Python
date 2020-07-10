objetivo = int(input('Escoge un número: '))
epsilon = 0.01 #Que tan cerca quiero estar de la respuesta
paso = epsilon ** 2 #Cuanto me voy a ir acercando por iteración a la respuesta 
respuesta = 0.0
import time
start_time = time.time()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
    #print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
print("--- %s seconds ---" % (time.time()-start_time)) # Print que muestra en cuanto tiempo terminó 

#La aproximación funciona similar a la enumeración exhaustiva pero más puntilloso. epsilon es una variable de cercania y con cada paso hago más fino cada paso