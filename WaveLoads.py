# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:21:25 2016

@author: ifh2
"""

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

import numpy as np
import matplotlib.pyplot as plt

body_length = 18

Rel_Bod_Len = np.linspace(0,1, num=7)
Bod_Len_Adj = np.array([0,.3,.75,1,.75,.3,0])
plt.figure(1)
plt.plot(Rel_Bod_Len,Bod_Len_Adj)

Wave_Length = [20,50,100,150,200,250,300]
Wave_Force = [30,14,7,6,5.5,5,4]

plt.figure(2)
plt.plot(Wave_Length,Wave_Force)

for i in range(len(Wave_Length)):
    Rel_Leng[i] = body_length/Wave_Length[i]
    