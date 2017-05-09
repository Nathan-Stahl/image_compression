#I cry many tears of sadness
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

#Main

#read image from file
fname = 'compressed.bin'
array = np.fromfile(fname)
print(array)
#decode array

#dequantize image


#do idct of image
img = cv2.idct(array)

#show new decompressed image.
img.shape = (512,512)
fin_img = Image.fromarray(img)
fin_img.show()
