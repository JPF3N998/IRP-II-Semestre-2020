import cv2 as cv

imgpath1 = "foto.jpg"
imgpath2 = "imagen1.jpg"
imgpath3 = "bordes1.jpg"
resultado1 = "resultado1.jpg"
resultado2 = "resultado2.jpg"
resultante3 = "resultado3.jpg"

############################################

img = cv.imread(imgpath1)

blurredImg = cv.GaussianBlur(img, (5, 5), 0)
cv.imwrite(imgpath2, blurredImg)

############################################

img = cv.imread(imgpath2)

ddepth = cv.CV_16S
kernel_size = 3
imgLapclacianned = cv.Laplacian(img, ddepth = ddepth, ksize = kernel_size)

cv.imwrite(imgpath3, imgLapclacianned)

############################################

blurLaplacianImg = blurredImg - imgLapclacianned

cv.imwrite(resultado1, blurLaplacianImg)


############################################
#Segundo método

from PIL import ImageEnhance

img = cv.imread(imgpath1)

enhancer = ImageEnhance.Sharpness(img)

for i in range(8):
    factor = i / 4.0
    enhancer.enhance(factor).show(f"Sharpness {factor:f}")



############################################
#Segundo método