## encontrar duplicados
lista = [1,1,4,5,7,1,7,1,7,1,7]
def duplic_01(lista):
	duplicados=[]
	tset=list(set(lista))
	for i in lista:
		if i in lista:
			duplicados.append(i)
		else:
			continue
	return duplicados
def duplic_02(lista):
	return set([numero for numero in lista if lista.count(numero)>1])
#print (duplic_02(lista))
#print (lista.count(0)>1)

lado: int = 10
tope: int = 0
vX: int = lado * 2
vY: int = vX
def llenarMatrix():
	pass
def matrixLados():	
	pass
def matrixInf():	
	pass

def matrixSup(ladoIni: int, ladoFin: int, ):	
	r = list(range(0,vX))
	for i in range(0,lado):
		print (i)
		for j in r:
			print (j,end=" ")
		print ()
		r.pop(0)
		r.pop()
	print ()
	# r =range(lado,lado*2)
	# for i in r:
	# 	print (i,end=" ")
	# for i in range(0,lado*2):
	# 	print (i,end=" ")
	# print ()

def ladosIzqDer():
	#print (tope)
	col:int = lado -2
	for i in range(0,lado):
		print ("|" + " "*col + "|" )
def topeSuperior():
	#print (tope)
	for i in range(0,lado):
		print ("=",end="")
	print()
def topeInferior():
	#print (tope)
	for i in range(0,lado):
		print ("=",end="")
	print()

#print (duplicados1(lista))
def espiral_01():
	matrixSup()
	matrixLados()
	# ladosIzqDer()
	# topeInferior()


espiral_01()