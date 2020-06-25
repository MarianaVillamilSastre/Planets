import numpy as np
import scipy as sp
import matplotlib.pyplot as plt



def funcion(x,y):
    m=(x+np.cos(y)*x)**3
    return m



x_1=0
x_2=np.pi
y_1=0
y_2=1
n = 10000
x = np.random.random(n)*(x_2-x_1)+x_1
y = np.random.random(n)*(y_2-y_1)+y_1
z = np.random.random(n)*(x_2-x_1)*(y_2-y_1)


k=0
for i in range(0,n):
	if z[i] <= funcion(x,y)[i]:
        	k=k+funcion(x[i],y[i])

i_1=(x_2-x_1)*(y_2-y_1)
integral_montecarlo=i_1*(k/n)



print ('El valor de la integral con el metodo montecarlo es', integral_montecarlo)



def meanvalueintegral(f,x_1,x_2,y_1,y_2,n1,n2):
	mx,my = ((x_2-x_1)/float(n1)),((y_2-y_1)/float(n2))
    
    	meanvalueint= 0
    	for i in range(n1):
        	for k in range(n2):
            		xi,yk = (x_1+mx/2+i*mx),(y_1+my/2+k*my)
            		meanvalueint+=(mx*my*f(xi,yk))
    	return meanvalueint


meanvalueint=meanvalueintegral(funcion,x_1,x_2,y_1,y_2,10,10)


print('El valor de la integral con el mean value method es:',meanvalueint)
