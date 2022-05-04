# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:27:27 2021

@author: Anthony
"""
from numpy import*


def interSphere(orientation,originRay,forme):
        t=0
        oc = originRay-array(forme[2])
        A = dot(orientation,orientation)
        B = 2*(dot(oc,orientation))
        C = dot(oc,oc)-(forme[1]**2)
        delta = (B**2)-4*A*C
        if delta > 0 : 
            t1 = (-B-(delta**0.5))/(2*A)
            t2 = (-B+(delta**0.5))/(2*A)
            if t1 > t2 :
                touch = True
                pos=(orientation*t2)+originRay
                t=t2
            else:
                touch = True
                pos=(orientation*t1)+originRay
                t=t1
        elif delta == 0:
            t = -B/(2*A)
            touch = True
            pos=(orientation*t)+originRay
        else:
            touch = False
            pos=[0,0,0]
        return pos,touch,forme[3],t

        
def interPlan(orientation,originRay,forme):
    t=0
    n= forme[1]/linalg.norm(forme[1])
    denom = -dot(orientation,forme[1])
    if denom > 0:
        pOIO = array(forme[1])-array(originRay)
        t=dot(pOIO,forme[2])/denom
        pos=orientation*t+originRay
        if t>=0 :
            return pos,True,forme[3],t
        else:
            return pos,False,forme[3],t
    else:
        return False,False,forme[3],t
    

    