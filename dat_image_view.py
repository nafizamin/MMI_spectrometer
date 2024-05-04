#python script to view the image files in .dat file format
# required python packages
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

def load_dat_image(fname,img_size=(1005,2560)):
    _image = np.fromfile(fname,dtype=np.uint16).reshape(img_size)
    return _image

# the two dat files has different sizes. use the appropriate image_size
# image_size_3C= (1005,2560)
# image_size_4C= (400,2560)

image_name = "image3C.dat"
image_size=(1005,2560)

# make sure the dat file is in the same folder location as this script
image=load_dat_image(image_name,img_size=image_size)
# below lines flips the image matrix, to be as shown in the manuscript
image=np.fliplr(image)
image_final=np.flipud(image)

plt.rcParams["figure.figsize"] = (10,12)
plt.imshow(image_final,vmin= np.quantile(image_final,0),vmax=np.quantile(image_final,0.99),cmap='gray')
plt.axis('off')