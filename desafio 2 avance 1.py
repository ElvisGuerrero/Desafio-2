#Taller de ingenieria 2- Desafio 2 
#Estudiantes: David Mansilla y Elvis Guerrero
#Profesores: Luz Cardona y Gabriel Nuñez
"------------------------------------------------------------------------------------------------------"
from random import randint

NombreE = input("Porfavor ingrese el nombre de la empresa: ")
Numero = int(input("Porfavor ingrese el número del contenedor correspondiente: "))

listaE = []

for i in range(1):
    listaE.extend([NombreE, Numero])

"Paso 1"
#Creacion del menu interactivo

print("Hola usuario, porfavor ingrese una opcion para elegir")
print("Ingrese 1 para Generar el estado inicial del puerto seco")
print("Ingrese 2 para Imprimir el estado del puerto seco ")
print("Ingrese 3 para Ubicar un contenedor ")
print("Ingrese 4 para Incluir un contenedor ")
print("Ingrese 5 para Retirar un contenero")
print("Ingrese 0 para cerrar su jornada laboral")

Opcion=int(input("Ingrese el valor correspondiente: "))
while(Opcion>0):
    if Opcion==1 :
        n=int(input("Ingrese la cantidad de contenedores maximos que soportara el puerto:"))
        m=int(input("Ingrese la cantidad de pilas maximas que soportara el puerto:"))
        for i in range(n):
            contenedor=[randint(1, n)]
        relleno=int(input("Si desea poner valores especificos en el puerto ingrese 1, si quiere que se genere al azar ingrese 2: "))
    if Opcion>5 :
        print("Valor incorrecto, ingrese nuevamente")
    if Opcion<0 :
        print("Valor incorrecto, ingrese nuevamente")
    Opcion=int(input("Ingrese el valor correspondiente: "))
    

print("Su jornada se cerro correctamente")
print(listaE)