import cv2 as cv

imgPaths = ["imagen.jpg", "foto3.jpg", "vacas.png"]

imgpath1 = imgPaths[1]
imgpath2 = "imagen1.jpg"
imgpath3 = "bordes1.jpg"
resultante = "resultante.jpg"

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

cv.imwrite(resultante, blurLaplacianImg)

