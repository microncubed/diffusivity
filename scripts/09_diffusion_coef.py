from PIL import Image
import os
import imageio

import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib as mp
mp.rc('font',size=16)


#12 mm is 80 pix
# 1 pix is 150 um
scale = 150

pd = os.path.dirname(os.getcwd())
inDir = '/fits'
outDir = inDir
os.chdir(pd + inDir)

left = scale**2/1e6*np.load('red_110.npy')
middle= scale**2/1e6*np.load('red_240.npy')
right= scale**2/1e6*np.load('red_380.npy')

t_vals = np.array([i*720 for i in range(len(left))])
print(len(left))




fig,ax=plt.subplots(1,1,figsize=[5,4])
ax.plot(t_vals[:50:1]/3600,left[:50:1],'.',markersize=12,alpha=0.5,color='violet')
ax.plot(t_vals[:50:1]/3600,middle[:50:1],'.',markersize=12,alpha=0.5,color='cyan')
ax.plot(t_vals[:50:1]/3600,right[:50:1],'.',markersize=12,alpha=0.5,color='b')
#ax.set_xlim([0,150])
#ax.set_ylim([0,1500])


def myLinear(t,a,b):
    return a+b*t


popt_list=[]

popt,pcov = curve_fit(myLinear,t_vals[:50],left[:50],p0=[100,4e-3])
dLeft = '{:3.0f}'.format(popt[1]/2*1e6)
print(dLeft,'um sq per s')

ax.plot(t_vals[:50]/3600,myLinear(np.array(t_vals[:50]),*popt),linewidth=2,color='red',alpha=1)

popt,pcov = curve_fit(myLinear,t_vals[:50],middle[:50],p0=[100,4e-3])
dMiddle = '{:3.0f}'.format(popt[1]/2*1e6)
print(dMiddle,'um sq per s')
ax.plot(t_vals[:50]/3600,myLinear(np.array(t_vals[:50]),*popt),linewidth=2,color='magenta',alpha=1)

popt,pcov = curve_fit(myLinear,t_vals[:50],right[:50],p0=[100,4e-3])
dRight = '{:3.0f}'.format(popt[1]/2*1e6)
print(dRight,'um sq per s')

ax.plot(t_vals[:50]/3600,myLinear(np.array(t_vals[:50]),*popt),linewidth=2,color='pink',alpha=1)

ax.set_ylabel('$\sigma ^2 (mm^2)$')
ax.set_xlabel('t (hr)')
ax.set_ylim([0,40])
ax.set_xlim([0,10])
fig.tight_layout()
fig.savefig('fits.png',dpi=300)
fig.show()
