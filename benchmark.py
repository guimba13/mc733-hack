import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.image as mpimg
from PIL import Image

x = []
y = []
z = []
mpl.rcParams['agg.path.chunksize'] = 10000
for i in range(0,2000000):
    x.append(random.uniform(-10000, 10000))
    y.append(random.uniform(-10000, 10000))
    z.append(x[i]*y[i])
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.savefig("grafico.png")
#plt.show()

imagem = 'carro.jpg'

img = mpimg.imread(imagem)
lum_img = img[:, :, 0]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.colorbar()

img = mpimg.imread(imagem)
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('hot')

img = Image.open(imagem)  # opens the file using Pillow - it's not an array yet
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img, interpolation="nearest")

img = mpimg.imread(imagem)
lum_img = img[:, :, 0]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')

img = Image.open(imagem)  # opens the file using Pillow - it's not an array yet
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)

a = []
b = []
z = []
l = []
x = []
leng = range(0, 500)
for j in leng:
    l.append(2)

for i in leng:
    a.append(l)
    b.append(l)

for j in leng:
    x.append(0)
  
for i in leng:  
    z.append(x[:])

for i in leng:
    for j in leng:
        for w in leng:
            z[i][j] = z[i][j] + (a[i][w]*b[w][j])
