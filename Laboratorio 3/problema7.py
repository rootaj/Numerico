import numpy as np

def LU_partial_decomposition(matrix):
    n, m = matrix.shape
    P = np.identity(n)
    L = np.identity(n)
    U = matrix.copy()
    PF = np.identity(n)
    LF = np.zeros((n,n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:,k]))
        index = index + k 
        if index != k:
            P = np.identity(n)
            P[[index,k],k:n] = P[[k,index],k:n]
            U[[index,k],k:n] = U[[k,index],k:n] 
            PF = np.dot(P,PF)
            LF = np.dot(P,LF)
        L = np.identity(n)
        for j in range(k+1,n):
            L[j,k] = -(U[j,k] / U[k,k])
            LF[j,k] = (U[j,k] / U[k,k])
        U = np.dot(L,U)
    np.fill_diagonal(LF, 1)
    return PF, LF, U

A = [[2, 1, 1, 0],
     [4, 3, 3, 1],
     [8, 7, 9, 5],
     [6, 7, 9, 8]]

A = np.array(A)

P1, L1, U1 = LU_partial_decomposition(A)

print('L =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in L1]))
print('U =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in U1]))
print('P =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in P1]))