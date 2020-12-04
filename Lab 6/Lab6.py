import cv2 as cv

imgpath1 = "foto.jpg"
imgpath2 = "lab4\\imagen1.jpg"
imgpath3 = "lab4\\bordes1.jpg"
resultado1 = "lab4\\resultado1.jpg"

############################################
def lab4():
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

from PIL import ImageEnhance,Image


def PillowSharpen():
    img = Image.open(imgpath1)

    enhancer = ImageEnhance.Sharpness(img)

    #img.show()

    #enhancer.enhance(1.75).show()

    for i in range(8):
        factor = i / 4.0
        
        enhancedImg = enhancer.enhance(factor)
        enhancedImg.save("PillowSharpness\\Sharpness "+str(factor)+".png")
    
############################################
#Tercer método
import numpy as np

def filtroSharpen():
    img1 = cv.imread(imgpath1, 1)
    
    # Creating our sharpening filter
    filter = np.array([[-1, -1, -1],
                    [-1,  9, -1],
                    [-1, -1, -1]])

    # Applying cv2.filter2D function on our image
    sharpen_img_1 = cv.filter2D(img1, -1, filter)

    cv.imwrite("FiltroSharpen\\resultado3.jpg", sharpen_img_1)

lab4()
PillowSharpen()
filtroSharpen()