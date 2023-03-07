from PIL import Image
import os

import numpy as np




images=[]
pd = os.path.dirname(os.getcwd())
inDir = '/cropped'
outDir = '/fits'

os.chdir(pd+inDir)

filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

print('{} files found'.format(len(filenames)))

dayTimes = [0]
for filename in filenames[:]:
    images.append(np.flip(np.array(Image.open(filename),dtype=np.uint8)[::1,::1,:],0))

os.chdir(pd+outDir)
np.save('image_array',images)
np.save('filenames',filenames)


