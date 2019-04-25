import numpy as np
from numpy import linalg as LA

def metJacobi (A,b,error,x):

    n = len (A)
    D = np.zeros ((n,n))

    d = np.diag(A)
    cont = 0

    for i in range(n):
        for j in range(n):
            if (i == j):
                D[i][j] = d[cont]
                cont = cont + 1

    R = A-D
    T = np.dot(-np.linalg.inv(D),R)
    C = np.dot(np.linalg.inv(D),b)

    iteracion = 0
    print (x)


#    for i in range(100)
    while LA.norm (np.dot(A,x)-b) >= error:
        x = np.dot(T,x) + C
        iteracion += 1
        print (x)

    print ("Numero de iteaciones: "+str(iteracion))


A = np.array ([ [2,1],
                [5,7] ])
b = np.array ([11,13])
error = 10**-6
x = np.array ([1,1])

metJacobi(A,b,error,x)