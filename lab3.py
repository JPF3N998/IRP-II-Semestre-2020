import cv2 as cv
import numpy as np
import math

def superponer(horizontal,vertical):
    
    height,width = horizontal.shape[0], horizontal.shape[1]
    
    canvasSuperpuesta = np.zeros((1, height,width), np.uint8)[0] #matriz en negro
    
    for y in range(height):
        for x in range(width):
            canvasSuperpuesta[y][x] = math.sqrt( (horizontal[y][x]**2) + (vertical[y][x]**2) )
    
    return canvasSuperpuesta

imgpath = "g.jpg"
img = cv.imread(imgpath, 0)

#cv.imwrite("H+V_"+imgpath, superpuesta)

#Deducir z = f(w) (mapeo inverso), de acuerdo a la literatura recomendada
#definir de forma genera los casos de la funcion de mapeo w = f(z) que s´ı
#tienen mapeo inverso.

#R/ si el determinante del mapeo b*c - a*d es igual a 0 el mapeo se degenera
#y no es posible y no habría existencia de un mapeo inverso.

#Desarrolle una funci´on que reciba como entradas las constantes
#complejas a, b, c, d y determine si las mismas genera una funci´on
#de variable compleja cuyo mapeo inverso s´ı existe.
def tiene_mapeo_inverso(a, b, c, d):
    if( ((b*c) - (a*d)) == 0):
        return False
    else:
        return True

#Desarrolle una funci´on que reciba como entradas una imagen y las constantes
#complejas a, b, c, d y, tomando la imagen de entrada como el Plano z genere
#la representaci´on de dicho plano en el Plano w.
def aplicar_mapeo(img, a, b, c = 0, d = 1):

    if(not tiene_mapeo_inverso(a, b, c, d)):
        print("La combinación de las variables a, b, c, d no tienen un mapeo inverso")
        return

    if(c == 0):
        print("C no puede valer 0")
        return 
    
    return aplicar_mapeo_aux(img, a, b, c, d)

def aplicar_mapeo_aux(planoZ, a, b, c , d):
    lamb = a / c                        #hay que hacer el catch de cuando c = 0
    mu = (b*c) - (a*d)
    alpha = c**2
    beta = c*d

    height, width = horizontal.shape[0], horizontal.shape[1]
    
    planoW = np.zeros((1, height, width), np.uint8)[0] #matriz en negro
    
    for y in range(height):
        for x in range(width):

            
            planoW[y][x] = planoZ[y][x]

            
    return canvasSuperpuesta
    


#Desarrolle una funci´on que reciba como entradas una imagen y las constantes
#complejas a, b y asuma que c = 0 ∧ d = 1 y genere el mapeo lineal
def aplicar_mapeo(img, a, b):
    c = 0
    d = 1
    return True













