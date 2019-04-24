import numpy as np
import math 

def matrizInversa (matriz):
    det = 1 / determinante(matriz)
    nmatriz = matrizAdjunta (matriz)
    multiplicarMatriz(det,nmatriz)
    return nmatriz

def multiplicarMatriz (n,matriz):
    for i in range (0,matriz.__len__()):
        for j in range (0,matriz.__len__()):
            matriz[i][j] *= n

def matrizAdjunta (matriz):
    return matrizTranspuesta(matrizCofactores(matriz))

def matrizCofactores (matriz):
    n = matriz.__len__()
    nm = np.zeros((n,n))
    
    for i in range (0,n):
        for j in range (0,n):
            det = np.zeros((n-1,n-1))
            for k in range (0,n):
                if(k!=i):
                    for l in range (0,n):
                        if (l!=j):
                            if k < i :
                                indice1 = k
                            else:
                                indice1 = k-1
                            
                            if l < j :
                                indice2 = l
                            else:
                                indice2 = l-1
                            
                            det[indice1][indice2] = matriz[k][l]
    
            detValor = determinante(det)
            nm[i][j] = detValor * math.pow(-1,i+j+2)
    
    return nm

def matrizTranspuesta (matriz):
    nuevam = np.zeros((matriz[0].__len__(),matriz.__len__()))

    for i in range (0,matriz.__len__()):
        for j in range (0,matriz.__len__()):
            nuevam[i][j] = matriz[j][i]
    
    return nuevam

def determinante (matriz):
    
    if matriz.__len__() == 2:
        det = (matriz[0][0]*matriz[1][1])-(matriz[1][0]*matriz[0][1])
        return det
    
    suma = 0
    n = matriz.__len__()
    
    for i in range (0,n):
        nm = np.zeros((n-1,n-1))
        for j in range (0,n):
            if j != i:
                for k in range (0,n):
                    indice = -1
                    if j<i:
                        indice = j
                    elif j > i:
                        indice = j-1
                    nm[indice][k-1] = matriz[j][k]
        
        if (i%2 == 0):
            suma += matriz[i][0] * determinante(nm)
        else:
            suma -= matriz[i][0] * determinante(nm)
    
    return suma

A = np.array ([ [2,1,1,0],
                [4,3,3,1],
                [8,7,9,5],
                [6,7,9,8] ])

inver_A = matrizInversa(A)

print ("Inversa de A")


print('inv_A =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in inver_A]))

print (np.dot(A,inver_A))