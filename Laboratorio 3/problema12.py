

def funcionY (x):
	return x / (1-x)

def varPorcnetual(x1,x2,y1,y2):
	return ((y2-y1)/(y1)) / ((x2-x1)/(x1))

x1 = 0.93
x2 = 0.94

y1 = funcionY(x1)
y2 = funcionY(x2)

print ("x1: "+str(funcionY(x1)))
print ("x2: "+str(funcionY(x2)))
print ("Valor porcentual: "+str(varPorcnetual(x1,x2,y1,y2)))

