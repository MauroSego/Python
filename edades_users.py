nombre_1 = input("Ingrese su nombre: ")
edad_1 = int(input(f'{nombre_1} ingrese su edad: '))
nombre_2 = input("Ingrese su nombre: ")
edad_2 = int(input(f'{nombre_2} ingrese su edad: '))

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2}')
elif edad_1 < edad_2:
    print(f'{nombre_2} es mayor que {nombre_1}')
else:
    print(f'{nombre_1} y {nombre_2} tienen la misma edad')