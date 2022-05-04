# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:29:18 2021

@author: Anthony
"""
from numpy import*
from math import tan,cos,radians
from PIL import*


figure = [["sphere",0.5,[2,-1,-2],[255,255,255]],
          ["sphere",0.5,[10,-1,-2],[255,255,255]],
          ["plan",[0,1,0],[0,2,0],[255,255,255]]]




# Constantes
width = 1500
height = 500

n=1
f=100
fov = 60
posCam = array([-1,0,0],dtype= int)
posEcran = array([0+n,0,0])
H = 2*n*tan(radians(fov/2))
L =   (width/height)*H

Ca =  array([1,0,0])
Ca =  Ca/linalg.norm(Ca)

Ch =  array([cos(radians(fov/2)),sin(radians(fov/1)),0])
Ch /= linalg.norm(Ch)

u1 =  (cross(Ca,Ch)*L)/(linalg.norm(cross(Ca,Ch))*width)
u2 =  (cross(Ca,u1)*H)/(linalg.norm(cross(Ca,u1))*height)
rIni =-((width/2)*u1)-((height/2)*u2)

im =  Image.new("RGB",(width,height))


skyColor = array([154,202,231])
horizon = array([227,169,136])

sun = array([0.5,0,-1],dtype=int)
sunVec = array(sun-posCam, dtype= int)
sunVec= true_divide(sunVec,linalg.norm(sunVec))