import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dtu2.jpg',0)  #to read image
f = np.fft.fft2(img) #fft of image
fshift = np.fft.fftshift(f)
fsort=np.sort(np.abs(f.reshape(-1)))   #sort by magnitude
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')  # to plot gray scaled image
plt.title('Input Image'), plt.xticks([]), plt.yticks([])  #xticks,yticks shows location of a parameter
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')  #plot fourier transformed image
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

#Zero out small coefficients and inverse transform
for keep in (0.8, 0.2, 0.09, 0.02):
    thresh=fsort[int(np.floor((1-keep)*len(fsort)))]
    print(thresh)
    ind=np.abs(f)>thresh #find small indices
    imgtlow= f*ind #threshold small indices
    imglow= np.fft.ifft2(imgtlow).real #compressed image
    plt.figure()
    plt.imshow(256-imglow, cmap='gray')
    plt.axis('off')
    plt.title('Compressed image: keep= '+ str(keep*100)+'%')
plt.show()

'''import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("lipi.jpg",0)
plt.imshow(img,"gray"),plt.title("original image")'''

#Bt=np.fft.fft2(B)
#Btsort=np.sort(np.abs(Bt.reshape(-1)))#sort by magnitude

#rows, cols = img.shape
#print(rows,cols)
#crow,ccol = rows/2 , cols/2  #to find centre of image
#print(crow,ccol)
#fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#f_ishift = np.fft.ifftshift(fshift)
#img_back = np.fft.ifft2(f_ishift)
#img_back = np.abs(img_back)

'''plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()'''

