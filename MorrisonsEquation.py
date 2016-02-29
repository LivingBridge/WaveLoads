# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:48:28 2016

@author: ifh2
"""
from matplotlib import pyplot as plt
from matplotlib import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]
if __name__ == "__main__":
    clear_all()
plt.close('all')

Cm = 2.04 #Highest value listed in Sorensen "Basic Coastal Engineering" Pg. 147
Cd = 1.6 #Highest value listed in Sorensen "Basic Coastal Engineering" Pg. 147
g = 9.81 #[m/s^2]
rho_w = 1025 #[kg/m^3]
h = 20.12 #[m] depth of water from MW to top of caisson according to bridge drawings
z = 0 #[m] submerged depth of object. Below the water is "-"
m_pontoon = 1344.91 #[kg]
V_pontoon = 1.4127 #[m^3]
pontoon_D = 1.07 #[m]
pontoon_L = 13.72 #[m]
rho_m = m_pontoon/V_pontoon

L = np.arange(5,80,5)
H = np.arange(0,1.875,0.125) #nysgih83002 paper says 2'(0.61m) wave height in small craft harbors (pg.25)
#Note from nysgih: Non breaking waves can be treated as static loads. Breaking waves occur when basin depth is <1.5H
#Assume non-breaking waves(pg 26)
#only annalyze strength parallel and perpendicular to main walkway(pg 27)


#The following equations come from Dean and Dalrymple "Water Wave Mechanics for Engineers and Scientists"
k = 2*np.pi/L 
sigma = np.sqrt(g*k*np.tanh(k*h)) #D&D Pg. 58 Eq. 3.34
u = np.zeros((len(L),len(H)))
dudt = np.zeros((len(L),len(H)))
Fd = np.zeros((len(L),len(H)))
Fi = np.zeros((len(L),len(H)))
F = np.zeros((len(L),len(H)))
for i in range(len(L)):
    for j in range(len(H)):    
        u[i,j] = (H[j]/2)*sigma[i]*np.cosh(k[i]*(h+z))/np.sinh(k[i]*h) #D&D Pg. 79 Eq. 4.3a
        dudt[i,j] = (H[j]/2)*(sigma[i]**2)*np.cosh(k[i]*(h+z))/np.sinh(k[i]*h) #D&D Pg. 80 Eq. 4.4

        #Morrison's
        Fd[i,j] = 0.5*rho_w*(pontoon_D*pontoon_L)*Cd*u[i,j]**2
        Fi[i,j] = Cm*rho_m*V_pontoon*dudt[i,j]
        F[i,j] = Fd[i,j]+Fi[i,j]

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(L[::-1]*np.ones((len(L),len(H))), np.transpose(H[::-1]*np.ones((len(L),len(H)))), F)
plt.xlabel('Wave Length[m]')
plt.ylabel('Wave Height[m]')
ax.set_zlabel('Force[N]')