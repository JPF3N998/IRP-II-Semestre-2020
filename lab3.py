import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imgpath = "g.jpg"
img = cv.imread(imgpath, 0)

"""Deducir z = f(w) (mapeo inverso), de acuerdo a la literatura recomendada
definir de forma genera los casos de la funcion de mapeo w = f(z) que s´ı
tienen mapeo inverso."""

"""R/ si el determinante del mapeo b*c - a*d es igual a 0 el mapeo se degenera
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

    return aplicar_mapeo_aux(img, a, b, c, d)#aplicar un mapeo bilineal

def aplicar_mapeo_aux(planoZ, a, b, c , d):
    lamb = a / c
    mu = (b*c) - (a*d)
    alpha = c**2
    beta = c*d

    height, width = planoZ.shape[0], planoZ.shape[1]

    planoW = np.zeros((1, height, width), np.uint8)[0] #matriz en negro

    for y in range(1, height):
        for x in range(1, width):

            z = complex(x, y)
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

            if(u >= 0 and u < width and v >= 0 and v < height):
                planoW[v][u] = planoZ[y][x]

    #cv.imwrite("result.jpg", planoW)
    return planoW

def invertir_mapeo(a, b, c, d, u, v):
    w = complex(u, v)
    z = ((-d*w) + b) / ((c*w) - a)
    return z

def plot_compare(planoZ, planoW):
    plt.subplot(1,2,1),plt.imshow(planoZ, cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(planoW, cmap = 'gray')
    plt.show()


"""a. El mapeo genera una magnificaci´on cuando b = 0 para todos los casos
a != 0 ∧ a ∈ R"""

#planoW = aplicar_mapeo(img, 1.5, 0)
#plot_compare(img, planoW)

"""b. El mapeo genera una magnificaci´on y una rotaci´on cuando b = 0 para
todos los casos donde a != 0 ∧ a ∈ C ∧ a /∈ R"""

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
planoW = aplicar_mapeo(img, complex(1, 1.6), complex(0, 1000), complex(0.001, 0.0001), complex(1, 1.5))
plot_compare(img, planoW)







