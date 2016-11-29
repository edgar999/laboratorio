#tarea 2
#Edgar Martinez Macedonio
#ejercicio 1
import math
def hipotenusa(cat1,cat2):
    sumcat= (cat1**2) + (cat2**2)
    raiz= math.sqrt(sumcat)
    return raiz

a= int (input("cateto1"))
b= int (input("cateto2"))
hipotenusa= hipotenusa(a,b)
print "hipotenusa=", hipotenusa
   
