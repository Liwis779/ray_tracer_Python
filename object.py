# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:29:18 2021

@author: Anthony
"""
from numpy import*
from math import tan,cos,radians
from PIL import*

centerSphere = array([36,-5,-6])
radiusSphere = 3

sun = array([0,1,0])
sun = sun/linalg.norm(sun)

# Constantes
width = 4080
height = 1080
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
u2 = (cross(Ca,u1)*H)/(linalg.norm(cross(Ca,u1))*height)
rIni = -((width/2)*u1)-((height/2)*u2)
im = Image.new("RGB",(width,height))
colorSky = array([154,202,231])