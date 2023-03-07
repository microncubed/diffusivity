from PIL import Image,ImageDraw,ImageFont
import os

#import datetime
#import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
pd = os.path.dirname(cwd)

inDir = '/cropped'
outDir = '/annotated'
os.chdir(pd+inDir)

filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

print('Number of files = ',len(filenames))

images=[]
dayTimes = [0]
for filename in filenames[:]:
	img = Image.open(filename)
	hsize = img.size[0]
	vsize = img.size[1]
	myTime = int(filename.replace('.png',''))-int(filenames[0].replace('.png',''))
	if myTime % 3600 == 0:
		myTime = myTime//3600
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 24)
		
		draw.text((hsize-100,vsize-50), '{:02d}'.format(myTime)+' h',fill=(0,0,0,255),font=font)
		os.chdir(pd+outDir)
		img.save(str(myTime).zfill(2)+'_hours.png')
		os.chdir(pd+inDir)