from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pywt
import numpy as np
from scipy import fftpack
import cv2

def calculate_error(mage_matrix, final_matrix):
	#calculate difference
	summ = 0
	for i in range(512):
        	for j in range(512):
                	diff = image_matrix[i,j] - final_matrix[i,j]#(d-x)
                	if diff < 0:
                        	diff = diff * -1
                	diff = diff * diff#(d-x)^2
                	summ = summ + diff#sigma(d-x)^2
	total_difference = summ/(512*512)#average
	print('mean squared error is ', total_difference)

#def do_dct(img):
#	return fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')

#MAIN

#get image
image = Image.open('lena.jpg')

#create matrix of image
image_matrix = np.mat(image)
image_matrix.setflags(write = 1)

#show original
img = Image.fromarray(image_matrix)
img.show()
size = 512

#do the dct
dct = cv2.dct(image_matrix.astype(float))

#show dct image
dct_image = Image.fromarray(dct)
dct_image.show()

idct = cv2.idct(dct)
idct_image = Image.fromarray(idct)
idct_image.show()
#this is where I would use my quantizer if I had one!


#encode image


#send compressed image to file
fname = 'compressed.bin'
dct.tofile(fname)

