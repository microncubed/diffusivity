
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

fig,ax = plt.subplots(1,3,figsize=[16,4])
ax[0].pcolor(red,vmin=0,vmax=255)
ax[0].set_title('Red')
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[1].pcolor(green,vmin=0,vmax=255)
ax[1].set_title('Green')
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[2].pcolor(blue,vmin=0,vmax=255)
ax[2].set_title('Blue')
ax[2].set_xticks([])
ax[2].set_yticks([])
os.chdir(pd+outDir)
fig.savefig('colours.png',dpi=300)
