# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:52:01 2021

@author: Anthony
"""
from PIL import Image
from numpy import*
from math import*
#from matplotlib.pyplot import*

# Constantes
width = 500
height = 500
n=1
f=100
fov = 60
posCam = array([-1,0,0])
posEcran = array([0+n,0,0])
H = 2*n*tan(radians(fov/2))
L = (width/height)*H
Ca = array([1,0,0])
Ca = Ca/linalg.norm(Ca)
Ch = array([cos(radians(fov/2)),sin(radians(fov/1)),0])
Ch /= linalg.norm(Ch)
u1 = (cross(Ca,Ch)*L)/(linalg.norm(cross(Ca,Ch))*width)
u1 /= linalg.norm(u1)
u2 = (cross(Ca,u1)*H)/(linalg.norm(cross(Ca,u1))*height)
u2 /= linalg.norm(u2)
rIni = -((width/2)*u1)-((height/2)*u2)
im = Image.new("1",(width,height))
pixelColor = im.load()
centerSphere = array([1.01,0,0])
radiusSphere = 2

def localpix(Nx,Ny):
    rO=posCam+n*Ca+rIni+Nx*u1+Ny*u2
    return rO

def calculRay(posPix):
    v = (posPix-posCam)/linalg.norm(posPix-posCam)
    v /= linalg.norm(v)
    ray = posPix+f*v
    return ray,v

def interSphere(orientation,originRay,posSphere,radius):
    A = dot(orientation,orientation)
    B = 2*(dot((originRay-posSphere),orientation))
    C = dot(originRay-posSphere,originRay-posSphere)-radius**2
    delta = (B**2)-4*A*C
    if delta > 0 : 
        t1 = (-B-(delta**0.5))/(2*A)
        t2 = (-B+(delta**0.5))/(2*A)
        if t1 > t2 :
           return True
        else:
            return True
    elif delta == 0:
        t = -B/(2*A)
        return True
    else:
        return False
    
def colorPixel(hit):
    if hit == True:
        return 1 
    else:
        return 0
    
for x in range(0,width-1):
    for y in range(0,height-1):
        print(x,y)
        currentPix = localpix(x,y)
        currentRayPix,direction = calculRay(currentPix)
        RayHit = interSphere(direction,posCam,centerSphere,radiusSphere)
        pixelColor[x,y]=colorPixel(RayHit)
        print(RayHit,colorPixel(RayHit))
im.save("image.png")
im.show()
