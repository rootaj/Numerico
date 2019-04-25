import numpy as np

def LU(c):
    a=np.array(c)
    m=np.zeros_like(a)
    per=np.eye(n)
    for k in range(n-1):
        p=k+np.argmax(np.abs(a[k:,k]))
        #print('Paso {}:'.format(k+1))
        if p != k:
         #   print('  Inter. filas {0}-{1}:'.format(k+1,p+1))
            a[[p,k],:]=a[[k,p],:]
            per[[p,k],:]=per[[k,p],:]
            m[[p,k],:]=m[[k,p],:]            
        if np.abs(a[k,k])==0:
            print('La matriz es singular')
            break
        else:
            for i in range(k+1,n):
                m[i,k]=a[i,k]/a[k,k]
                a[i,k:]=a[i,k:]-m[i,k]*a[k,k:]
            #print('   L{0} =\n'.format(k+1)+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
            #    for row in m]))
            #print('   A{0} =\n'.format(k+1)+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
            #    for row in a]))
        m[k,k]=1    
    m[n-1,n-1]=1    
    return(m,a,per)

n=4
a = np.array([2,1,1,0,4,3,3,1,8,7,9,5,6,7,9,8],
             dtype='f').reshape((n,n))
(L,U,P)=LU(a)
print('FACTORIZACION DOOLITLE')
print('L =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in L]))
print('U =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in U]))
print('P =\n'+'\n'.join([''.join(['{:8.3f}'.format(item) for item in row]) 
      for row in P]))