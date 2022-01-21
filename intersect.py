# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:27:27 2021

@author: Anthony
"""
from numpy import*


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