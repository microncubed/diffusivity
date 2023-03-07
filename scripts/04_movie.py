from PIL import Image,features
import os
import imageio
images=[]
import datetime

cwd = os.getcwd()
pd = os.path.dirname(cwd)

inDir = '/annotated'
outDir = '/movie'  

os.chdir(pd+inDir)

filenames = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

dayTimes = [0]

os.chdir(pd+outDir)

writer = imageio.get_writer('movie.mp4', fps=10)


for im in filenames:
    os.chdir(pd+inDir)
    writer.append_data(imageio.imread(im))
writer.close()