
# Eliminacion de Gauss-Jordam
# Con pivote

import numpy as np

def formaTriangulaInferior (A):
	
	n =  len(A)
	for k in xrange(n-1):
		maxindex = abs(A[k:,k]).argmax() + k
		if A[maxindex, k] == 0:
			raise ValueError("Matrix is singular.")
		if maxindex != k:
			A[[k,maxindex]] = A[[maxindex, k]]
		for row in xrange(k+1, n):
			multiplier = A[row][k]/A[k][k]
			A[row][k] = multiplier
			for col in xrange(k + 1, n):
				A[row][col] = A[row][col] - multiplier*A[k][col]
	return A



A = np.array ([ [2,1,1,0],
				[4,3,3,1],
				[8,7,9,5],
				[6,7,9,8] ])

print (formaTriangulaInferior(A))