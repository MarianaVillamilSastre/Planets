import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Lee los datos
DatosMarzo =np.loadtxt("DatosMarzo.txt")
GRF=np.loadtxt("GRF_vs_EQ.txt")
#Separa columnas y las mete en variables relevantes
GlacierRockFall=DatosMarzo[:,0]
LargestEarthquake=DatosMarzo[:,1]
GlacierPorMeses=GRF[:,0]
LEPorMeses=GRF[:,1]
#Plotea los datos dependiendo la variable temporal
gVsLE=plt.scatter(GlacierRockFall,LargestEarthquake,c='green',s=30,label="Glacier&RockFall-LargestEarthqueakes in March")
gVsLE_Total=plt.scatter(GlacierPorMeses,LEPorMeses, color='black',s=3, label="Glacier&RockFall-LargestEarthqueakes for all months")
plt.title("Glacier & Rockfall vs Largest EarthQuake")
plt.xlabel("Glacier & Rockfall")
plt.ylabel("Largest EarthQuake")
plt.legend(loc=0)
plt.savefig('PlotTolima.pdf')
plt.close()

