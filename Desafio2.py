
def llenarpuerto(N,M):

	puerto = []

	if N==M or N<M: # dejamos la ultima fila vacía
		
		for i in range(M):
			contenedores = []
			for j in range(N):
				contenedores.append(input("Ingrese numero/NombreEmpresa: "))
			contenedores.append(0) # valor 0 representa espacio vacío
			puerto.append(contenedores)
		
	else: # dejamos la ultima fila vacía + 1 elmento
		
		for i in range(M):
			contenedores = []
			for j in range(N):
				if i == 0 and j == N-1:
					contenedores.append(0) # valor 0 representa espacio vacío
				else:
					contenedores.append(input("Ingrese numero/NombreEmpresa: "))	
			contenedores.append(0) # valor 0 representa espacio vacío
			puerto.append(contenedores)
	return puerto
	
def imprimepuerto(puerto,N,M):

	i = N-1
	while (i >= 0):
		j = M-1
		print("| ", end = " ")
		while (j >= 0):
			print (puerto[j][i], " | ", end=" ")
			j = j - 1
		print("")
		i = i - 1

def buscar(puerto, contenedor):
	
	index = -1
	i = 0
	while(i<len(puerto)):
		
		if puerto[i].count(contenedor) > 0:
			index= puerto[i].index(contenedor)
			pilak = i
		i = i + 1
	if index != -1:
		return (pilak,index)
	else:
		print("no se encuentra contenedor")
				
	
####### programa principal #####
	
N = int(input("Ingrese n: ")) # N+1
M = int(input("Ingrese m: "))

puerto = llenarpuerto(N,M)
imprimepuerto(puerto, N+1, M)

a,b = buscar(puerto, 'c')

print("Contenedor ", puerto[a][b]," fue encontrado en los indices",a,b)
