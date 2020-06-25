import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

OrbitaMarte=np.loadtxt("MarsOrbit.dat")
MarteX=OrbitaMarte[:,1]
MarteY=OrbitaMarte[:,2]
MarteZ=OrbitaMarte[:,3]
Tiempo=OrbitaMarte[:,0]

OrbitaTierra=np.loadtxt("EarthOrbit.dat")
TierraX=OrbitaTierra[:,1]
TierraY=OrbitaTierra[:,2]
TierraZ=OrbitaTierra[:,3]
TiempoT=OrbitaTierra[:,0]
fig=plt.figure(figsize=(20,20))
ax=fig.add_subplot(121,projection='3d')
ax.plot(TierraX,TierraY,TierraZ,'black')
ax.plot(MarteX,MarteY,MarteZ,'blue')
plt.title("Orbitas Terrestre(Color Negro) y Marciana(Color Azul)", fontsize = 12)
plt.xlabel("Posicion en el eje X(UA)")
plt.ylabel("Posicion en el eje Y(UA)")
plt.savefig('Orbitas.pdf')
plt.close()


def derivada(array):
	h=(Tiempo[1]-Tiempo[0])*(31536000)
	derivada2=np.zeros(len(MarteX))
	for i in range(1,len(MarteX)-1):
		derivada2[i]=((array[i+1]+array[i-1]-2*array[i])*(149597870700)/h**2)
	return derivada2


def aceleracion():
	lista1=np.zeros(len(MarteX))
	for i in range(len(MarteX)):	
		lista1[i]=np.sqrt((derivada(MarteX)[i])**2 + (derivada(MarteY)[i])**2 +(derivada(MarteZ)[i])**2)
	return lista1
ace=aceleracion()

def radio():	
	lista=np.zeros(len(MarteX))
	
	for i in range(len(MarteX)):
		lista[i]=(np.sqrt(MarteX[i]**2 + MarteY[i]**2 + MarteZ[i]**2))*(149597870700)
	return lista
rad=radio()


def masa():
	masat=np.zeros(len(MarteX))
	for i in range(len(MarteX)-1):
		masat[i]=(ace[i]*(rad[i]**2))/(6.674E-11)
	return masat
masatotal=masa()
print "La masa del sol obtenida a partir de las posiciones de la orbita de Marte es:" +str(np.mean(masatotal)) 


def derivadaT(array):
	h=(TiempoT[1]-TiempoT[0])*(31536000)
	derivada2=np.zeros(len(TierraX))
	for i in range(1,len(TierraX)-1):
		derivada2[i]=((array[i+1]+array[i-1]-2*array[i])*(149597870700)/h**2)
	return derivada2


def aceleracionT():
	lista1=np.zeros(len(TierraX))
	for i in range(len(TierraX)):	
		lista1[i]=np.sqrt((derivada(TierraX)[i])**2 + (derivada(TierraY)[i])**2 +(derivada(TierraZ)[i])**2)
	return lista1
ace=aceleracionT()

def radioT():	
	lista=np.zeros(len(TierraX))
	
	for i in range(len(TierraX)):
		lista[i]=(np.sqrt(TierraX[i]**2 + TierraY[i]**2 + TierraZ[i]**2))*(149597870700)
	return lista
rad=radioT()


def masaT():
	masat=np.zeros(len(TierraX))
	for i in range(len(TierraX)-1):
		masat[i]=(ace[i]*(rad[i]**2))/(6.674E-11)
	return masat
masa_total=masa()
print "La masa del sol obtenida a partir de las posiciones de la orbita de la Tierra es:" +str(np.mean(masa_total)) 














