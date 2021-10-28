from random import randint


N = int(input("Ingrese un valor para la cantidad de notas: "))
M = int(input("Ingrese un valor para la cantidad de alumnos: "))


alumnos = []
for i in range(M):
	notas = []
	for j in range(N):
		notas.append(randint(1,7))
	alumnos.append(notas)

print (alumnos)

del alumnos[:]


alumnos = []
for i in range(M):
	notas = []*N
	alumnos.append(notas)

print (alumnos)
del alumnos[:]


alumnos = []
for i in range(M):
	notas = []
	for j in range(N):
		notas.append(input("Ingrese nombre estudiane y nota con formato Nombre/nota: "))
	alumnos.append(notas)

print (alumnos)
del alumnos[:]
