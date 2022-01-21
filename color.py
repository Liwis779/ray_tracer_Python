# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:47:50 2021

@author: Anthony
"""
from math import comb,floor
from numpy import*
 
def PolyBernstein (m,t,P):
    Poly=(1-t)**m*P[0]
    for i in range(0,m):
        Poly+=comb(m,i+1)*P[i]*t**(i+1)*(1-t)**(m-(i+1))
    return Poly

def colorPixel(hit,v,s):
    if hit == True:
        return [255,0,0]
    else: 
        sv = abs((dot(s,v)))
        color = []
        color.append(int(PolyBernstein(4,sv,[154,140,260,255])))
        color.append(int(PolyBernstein(4,sv,[202,190,260,255])))
        color.append(int(PolyBernstein(4,sv,[231,220,260,255])))
        return color
    