from skimage import data
from scipy.signal import convolve2d as conv2
from skimage.morphology import watershed
from skimage.filters import gaussian
from skimage.filters import median
from skimage.color import rgb2gray
from skimage import color
from skimage.io import imread
from skimage.io import imsave
import numpy as np
import matplotlib.pyplot as plt

a=data.coins()

imsave('tmp.png',a)


I = rgb2gray(imread('tmp.png').astype(np.float64)/255)





I=median(I,mask=np.zeros((10,10)))
I=gaussian(I,10)




dxm=np.array([[0,0,0],[-1,0,1],[0,0,0]])

dym=dxm.T


dx=conv2(I,dxm,'same')
dy=conv2(I,dym,'same')


absG=np.sqrt(dx**2+dy**2)




plt.imshow(absG)
plt.show()




labels = watershed(absG)



plt.imshow(color.label2rgb(labels))
plt.show()






plt.imshow(labels)
plt.show()







I = rgb2gray(data.coins().astype(np.float64)/255)





