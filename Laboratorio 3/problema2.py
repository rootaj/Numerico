
import numpy as np

def eliminacionGaussiana (A,b):
	return np.linalg.solve(A,b);

def construyeH (i,j):
	H = np.zeros ((i,j))
	for i_aux in range(0,i,1):
		for j_aux in range(0,j,1):
			H[i_aux][j_aux] = 1.0 / (i_aux+j_aux+1.0)
	return H

def construyeB (j):
	return np.ones	(j)

i = j = 10
H = construyeH(i,j)
b = construyeB(i)
x = eliminacionGaussiana(H,b)

print ("Solucion x:")
cont = 0
for i in x:
	cont += 1
	print ("X["+str(cont)+"]: "+str(i))