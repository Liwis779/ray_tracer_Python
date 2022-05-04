# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:47:50 2021

@author: Anthony
"""
from math import comb,floor
from numpy import*
from object import*
from intersect import*

def PolyBernstein (m,t,P):
    Poly=(1-t)**m*P[0]
    for i in range(0,m):
        Poly+=comb(m,i+1)*P[i]*t**(i+1)*(1-t)**(m-(i+1))
    return Poly

def colorObj(s,c,n):
    color = []
    L = 1*1*max(0,abs(dot(n,s)))
    color.append(int(L*c[0]))
    color.append(int(L*c[1]))
    color.append(int(L*c[2]))
    return tuple(color)

def colorSky(v,s):
    sky = []
    color =[]
    sky.append(int(skyColor[0]*v[1]+horizon[0]*(1-v[1])))
    sky.append(int(skyColor[1]*v[1]+horizon[1]*(1-v[1])))
    sky.append(int(skyColor[2]*v[1]+horizon[2]*(1-v[1])))
    sv = dot(s,v)**1500
    color.append(round(4*int(252*sv),2))
    color.append(round(4*int(229*sv),2))
    color.append(round(4*int(112*sv),2))
    return tuple(add(sky,color))

def colorCompute(rayPos,rayDir,formList):
    d=1e100
    LightVec=[0,0,0]
    n=[0,0,0]
    numObj=0
    RayHit=False
    colorHit = 0
    touchPos = 0
    objTouch = [numObj,d,touchPos,colorHit,RayHit,n,LightVec]
    for i in range(0,len(formList)):
        if formList[i][0] == "sphere":
            touchPos,RayHit,colorHit,d = interSphere(rayDir,rayPos,formList[i])
            numObj=i
            if RayHit==True:      
                if d < objTouch[1]:
                    colorHit=colorHit/d
                    n=touchPos-formList[i][2]
                    LightVec = array(touchPos-sun)
                    objTouch=[numObj,d,touchPos,colorHit,RayHit,n,LightVec]     
        elif formList[i][0] == "plan":
            touchPos,RayHit,colorHit,d = interPlan(rayDir,rayPos,formList[i])           
            numObj=i
            if RayHit == True:
                if d < objTouch[1]:
                    LightVec = array(touchPos-sun)
                    n=formList[i][2]
                    objTouch=[numObj,d,touchPos,colorHit,RayHit,n,LightVec]
    return objTouch