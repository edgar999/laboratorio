import matplotlib.pyplot as plt
import math


a=input("introduzca latitud")
b=input("introduzca longitud")
c=input("introduzca latitud")
d=input("introduzca longitud")
def distancia(t1,g1,t2,g2,):
    pi=3.1416
    x1=(t1*pi/180)
    y1=(g1*pi/180)
    x2=(t2*pi/180)
    y2=(g2*pi/180)
    distancia=6371.01*math.acos*(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    output=distancia(a,b,c,d)
    print output
    
