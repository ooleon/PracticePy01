## encontrar duplicados
lista = [1,1,4,5,7,1,7,1,7,1,7]
def duplicados1(lista):
	duplicados=[]
	tset=list(set(lista))
	for i in lista:
		if i in lista:
			duplicados.append(i)
		else:
			continue
	return duplicados

#print (duplicados1(lista))

print (lista)
def duplicados2(lista):
	return set([numero for numero in lista if lista.count(numero)>1])
print (duplicados2(lista))
print (lista.count(0)>1)
