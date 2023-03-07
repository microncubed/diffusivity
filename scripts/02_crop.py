from PIL import Image,ImageDraw,ImageFont
import os

images=[]

inDir = '/images'
outDir = '/cropped'        
cwd = os.getcwd()
pd = os.path.dirname(cwd)

print('Project directory',pd)
os.chdir(pd+inDir)

filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

for filename in filenames:
    img = Image.open(filename)
    #img.show()
    #print(img.size)
    img1 = img.crop((660,320,1172,832))
    os.chdir(pd+outDir)
    img1.save(filename)
    os.chdir(pd+inDir)
