import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

imgpath = "g.jpg"
img = cv.imread(imgpath, 0)

#Parte 1 lab
#=======================================================================================================================

"""Deducir z = f(w) (mapeo inverso), de acuerdo a la literatura recomendada
definir de forma genera los casos de la funcion de mapeo w = f(z) que s´ı
tienen mapeo inverso."""

"""Para mapeo lineal: De la forma alpha*z + beta si alpha = 0 todos los valores se mapean al punto
beta por lo que el mapeo se degenera y en estos casos no existe mapeo inverso"""

"""R/ Para mapeo bilineal: Si el determinante del mapeo b*c - a*d es igual a 0 el mapeo se degenera
y no es posible y no habría existencia de un mapeo inverso."""

"""Desarrolle una funci´on que reciba como entradas las constantes
complejas a, b, c, d y determine si las mismas genera una funci´on
de variable compleja cuyo mapeo inverso s´ı existe."""

def tiene_mapeo_inverso(a, b, c, d):
    if( ((b*c) - (a*d)) == 0):
        return False
    else:
        return True

"""Desarrolle una funci´on que reciba como entradas una imagen y las constantes
complejas a, b, c, d y, tomando la imagen de entrada como el Plano z genere
la representaci´on de dicho plano en el Plano w."""

def aplicar_mapeo(img, a, b, c = 0, d = 1):

    if(not tiene_mapeo_inverso(a, b, c, d)):
        print("La combinación de las variables a, b, c, d no tienen un mapeo inverso")
        return np.zeros((1, 1, 1), np.uint8)[0]

    if(c == 0 and d == 1):#implica que se debe aplicar un mapeo lineal
        return aplicar_mapeo_lineal(img, a, b)

    if(c == 0):
        print("C no puede ser 0")
        return np.zeros((1, 1, 1), np.uint8)[0]
    
    return aplicar_mapeo_aux(img, a, b, c, d)#aplicar un mapeo bilineal (fractional linear transformation)

def aplicar_mapeo_aux(planoZ, a, b, c , d):
    lamb = a / c
    mu = (b*c) - (a*d)
    alpha = c**2
    beta = c*d

    height, width = planoZ.shape[0], planoZ.shape[1]

    planoW = np.zeros((1, height, width), np.uint8)[0] #matriz en negro

    for y in range(1, height):
        for x in range(1, width):

            z = complex(x, y) #z = z + jy
            w = lamb + (mu / ((alpha * z) + beta))
            u = int(w.real)
            v = int(w.imag)

            if(u >= 0 and u < width and v >= 0 and v < height):
                planoW[v][u] = planoZ[y][x]

    return planoW

"""Desarrolle una funci´on que reciba como entradas una imagen y las constantes
complejas a, b y asuma que c = 0 ∧ d = 1 y genere el mapeo lineal"""

def aplicar_mapeo_lineal(planoZ, a, b):#c = 0 d = 1

    """este escalado multiplica la parte real de a por el alto y ancho de la imagen, para poder capturar
        la mayoría de las imagenes en el plano W pero esto hace que cuando no hay rotación la única diferencia
        entre ambos planos es que el W está escalado de la parte real de a veces
    if(a.real >= 1):
        height, width = int(planoZ.shape[0] * a.real), int(planoZ.shape[1] * a.real)
    else:
        height, width = planoZ.shape[0], planoZ.shape[1]
    """
    height, width = planoZ.shape[0], planoZ.shape[1]

    planoW = np.zeros((1, height, width), np.uint8)[0] #matriz en negro

    for y in range(height):
        for x in range(width):

            z = complex(x, y)
            w = (a*z) + b
            u = int(w.real)
            v = int(w.imag)

            if(u >= 0 and u < width and v >= 0 and v < height): #Limitamos los calculos a solo pares ordenados dentro del primer cuadrante
                planoW[v][u] = planoZ[y][x]

    #cv.imwrite("result.jpg", planoW)
    return planoW

def plot_compare(planoZ, planoW):
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1),plt.imshow(planoZ, cmap = 'gray')
    plt.title('Original'), 

    plt.subplot(1,2,2),plt.imshow(planoW, cmap = 'gray')
    plt.show()

"""a. El mapeo genera una magnificaci´on cuando b = 0 para todos los casos
a != 0 ∧ a ∈ R"""

#planoW = aplicar_mapeo(img, 1.5, 0)
#plot_compare(img, planoW)

"""b. El mapeo genera una magnificaci´on y una rotaci´on cuando b = 0 para
todos los casos donde a != 0 ∧ a ∈ C ∧ a !∈ R"""

#planoW = aplicar_mapeo(img, complex(1.5, 0.4), 0)
#plot_compare(img, planoW)

"""c. El mapeo genera ´unicamente un desplazamiento de todo el Plano z cuando
b != 0 ∧ a = 1"""

#planoW = aplicar_mapeo(img, 1, complex(100, 100))
#plot_compare(img, planoW)

"""d. Para el caso donde a != 0 ∧ b != 0, que el mapeo genera la combinaci´on
de una magnificaci´on, una rotaci´on y un desplazamiento de la im´agen del
Plano z en el Plano w."""

#planoW = aplicar_mapeo(img, complex(1.5, 0.4), complex(100, 100))
#plot_compare(img, planoW)


#planoW = aplicar_mapeo(img, complex(1.5, 0.4), complex(0, 0), complex(0.001, -0.001), complex(1, 2))
#planoW = aplicar_mapeo(img, complex(1, 1.6), complex(0, 1000), complex(0.001, 0.0001), complex(1, 1.5))
#plot_compare(img, planoW)

#Parte 2
#=======================================================================================================================

a = complex(3, 0.4)
b = complex(-700, 700)
c = complex(0.001, -0.001)
d = complex(1, 2)

"""2. Utilizando la biblioteca o herramienta seleccionada, desarrolle una aplicaci´on que reciba como entradas una
imagen y las constantes complejas a, b, c, d y genere el mapeo directo de la imagen en el Plano w), siempre y
cuando el mapeo exista, guarde la imagen resultante con el nombre imagen2."""

planoW = aplicar_mapeo(img, a, b, c, d)
cv.imwrite("imagen2.jpg", planoW)

"""3. Utilizando el mapeo inverso obtenga los valores de los pixeles faltantes en la imgagen generada en el punto 2.,
guarde la imagen resultante como imagen3."""

def invertir_mapeo(a, b, c, d, u, v):
    w = complex(u, v)
    z = ((-d*w) + b) / ((c*w) - a)
    return z

def reconstruir_mapeo(planoZ, planoW, a, b, c, d):

    height, width = planoW.shape[0], planoW.shape[1]

    for v in range(1, height):
        for u in range(1, width):

            if(planoW[v][u] == 0):
                z = invertir_mapeo(a, b, c, d, u, v)
                x = int(z.real)
                y = int(z.imag)

                if (x >= 0 and x < width and y >= 0 and y < height):
                    planoW[v][u] = planoZ[y][x]

    return planoW

planoWreconstruido = reconstruir_mapeo(img, planoW, a, b, c, d)
cv.imwrite("imagen3.jpg", planoWreconstruido)


"""4. Utilizando el mapeo inverso e interpolaci´on de pixeles en colindancia N=4, obtenga los valores de los pixeles
faltantes en la imgagen generada en el punto 2., guarde la imagen resultante como imagen4."""

filtroColindancia4  = [[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0]]

filtroColindancia8  = [[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]]

def applyfilter(X, filter):
    val = 0

    for y in range(len(X)):
        for x in range(len(X[0])):
            val += X[y][x] * filter[y][x]
    return val


def reconstruir_mapeo_interpolacion(planoZ, planoW, a, b, c, d, kernel, colindancia):
    height, width = planoW.shape[0], planoW.shape[1]

    for v in range(1, height):
        for u in range(1, width):

            if (planoW[v][u] == 0):
                z = invertir_mapeo(a, b, c, d, u, v)
                x = int(z.real)
                y = int(z.imag)

                """if (x > 0 and x < width - 1 and y > 0 and y < height - 1):
                    focusedRows = planoZ[y:y + 3]
                    subMatrix = []

                    for row in focusedRows:
                        subMatrix += [row[x - 1:x + 2]]

                    pxlValue = applyfilter(subMatrix, kernel) / colindancia
                    planoW[v][u] = abs(pxlValue)"""

                if (x > 0 and x < width - 1 and y > 0 and y < height - 1):
                    plxValue = 0

                    for j in range(-1, 2):
                        for i in range(-1, 2):
                            plxValue += kernel[j + 1][i + 1] * planoZ[y + j][x + i]

                    plxValue = plxValue / colindancia
                    planoW[v][u] = abs(plxValue)

    return planoW

planoW = cv.imread("imagen2.jpg", 0)
planoWreconstruidointerpolado4 = reconstruir_mapeo_interpolacion(img, planoW, a, b, c, d, filtroColindancia4, 5)
cv.imwrite("imagen4.jpg", planoWreconstruidointerpolado4)

"""5. Utilizando el mapeo inverso e interpolaci´on de pixeles en colindancia N=8, obtenga los valores de los pixeles
faltantes en la imgagen generada en el punto 2., guarde la imagen resultante como imagen5."""

planoW = cv.imread("imagen2.jpg", 0)
planoWreconstruidointerpolado8 = reconstruir_mapeo_interpolacion(img, planoW, a, b, c, d, filtroColindancia8, 9)
cv.imwrite("imagen5.jpg", planoWreconstruidointerpolado8)

"""6. Utilizando un filtro Gausseano con una m´ascara de 5x5, realize el proceso de suavizado de la im´agen2, guarte
la imagen resultante como imagen6."""

planoW = cv.imread("imagen2.jpg", 0)
planoWgaus = cv.GaussianBlur(planoW, (5, 5), 0)
cv.imwrite("imagen6.jpg", planoWgaus)

"""nota: los puntos 4 y 5 creo que están mal planteados, porque dicen que utilice el mapeo inverso e interpolación
para obtener los datos faltantes, pero de la imagen2 y la imagen2 es ya un mapeo al que le falta información por lo que
creo que se refiere a la imagen original"""