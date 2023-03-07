
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['font.size']=16

cwd = os.getcwd()
pd = os.path.dirname(cwd)

inDir = '/cropped'
outDir = '/figures'

os.chdir(pd+inDir)

number = 1596443764 + 3600*1

img = Image.open(str(number)+'.png')
img = np.array(img)

red = np.flip(img[:,:,0],0)
green = np.flip(img[:,:,1],0)
blue = np.flip(img[:,:,2],0)

print(np.max(red),np.max(green),np.max(blue))

fig,ax = plt.subplots(1,2,figsize=[10,4])
ax[0].imshow(img)
ax[1].plot(red[256,:],color='r')
ax[1].plot(green[256,:],color='g')
ax[1].plot(blue[256,:],color='b')
os.chdir(pd+outDir)
fig.savefig('horiz.png',dpi=300)

fig,ax = plt.subplots(1,2,figsize=[10,4])
ax[0].imshow(img)
ax[1].plot(red[:,110],color='r')
ax[1].plot(green[:,110],color='g')
ax[1].plot(blue[:,110],color='b')
ax[0].set_xticks([0,256,512])
ax[0].set_yticks([0,256,512])
ax[0].set_xlabel('x (pix)')
ax[0].set_ylabel('y (pix)')

ax[1].set_xlabel('y (px)')
ax[1].set_ylabel('Intensity')
ax[1].set_xlim([0,512])
ax[1].set_ylim([0,256])
ax[1].set_xticks([0,256,512])
ax[1].set_yticks([0,128,256])
os.chdir(pd+outDir)
fig.tight_layout()
fig.savefig('vert_100.png',dpi=300)
