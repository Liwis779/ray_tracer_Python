# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:10:36 2021

@author: Anthony
"""
from numpy import*
from object import*
def localpix(Nx,Ny):
    rO=posCam+n*Ca+rIni+Nx*u1+Ny*u2
    return rO

def calculRay(posPix):
    v = (posPix-posCam)/linalg.norm(posPix-posCam)
    v /= linalg.norm(v)
    ray = posPix+f*v
    return ray,v