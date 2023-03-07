from PIL import Image
import os
import imageio

import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams['font.size']=16

import os

pd = os.path.dirname(os.getcwd())
inDir = '/fits'
outDir = inDir

os.chdir(pd + inDir)

images = np.load('image_array.npy')
numImages = len(images)
print('{} images found'.format(numImages))


myParams={'colour':0,'slice':110}

sliceArray=[]
for i in range(numImages):
    sliceArray.append(images[i][:,myParams['slice'],myParams['colour']])

fig,ax=plt.subplots(1,1,figsize=[5,4])
xVals = [100+i for i in range(300)]

def myGaussian(x,a,b,c,d,m):
    return a * np.exp(-(x-b)**2/2/c**2)+d+np.multiply(m,x)

popt = []

for i,myslice in enumerate(sliceArray):
    try:
        popt.append(curve_fit(myGaussian,xVals,sliceArray[i][100:400],p0=[-100,250,50,200,-0.1])[0])
    except:
        popt.append(np.array([0,0,0,0]))        
        print('fit exception at',i)


for i,myslice in enumerate(sliceArray[:50:5]):
    if popt[i*5][0] !=0:
        ax.plot(xVals,myslice[100:400],'.',color='b',alpha=0.25)
        ax.plot(xVals,myGaussian(xVals,*popt[i*5]),color='r',linewidth=2,alpha=0.75)

name='red_'+str(myParams['slice'])
ax.set_xlabel('y (px)')
ax.set_ylabel('Intensity')
ax.set_xlim([100,400])
#ax.set_ylim([-50,250])
ax.set_xticks([100,200,300,400])
#ax[1].set_yticks([0,128,256])

fig.tight_layout()
fig.savefig(name+'.png',dpi=300)

#fig.show()
####

sdVals = []
sdValsSq = []

for opt in popt:
    sdVals.append(opt[2])

for item in sdVals:
    sdValsSq.append(item**2)

np.save(name,sdValsSq)





