import cv2 as cv
import numpy as np

imgpath1 = "foto3.jpg"
imgpath2 = "imagen1.jpg"
imgpath3 = "bordes1.jpg"
resultante = "resultante.jpg"

############################################

img = cv.imread(imgpath1)

blurredImg = cv.GaussianBlur(img,(5,5),0)
cv.imwrite(imgpath2,blurredImg)

############################################

img = cv.imread(imgpath2)

ddepth = cv.CV_8U
kernel_size = 3
imgLapclacianned = cv.Laplacian(img,ddepth=ddepth, ksize=kernel_size)

cv.imwrite(imgpath3,imgLapclacianned)

############################################

print(blurredImg.dtype)
print(imgLapclacianned.dtype)

cv.imwrite(resultante,cv.add(imgLapclacianned,blurredImg))
