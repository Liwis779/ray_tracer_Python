# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 18:52:01 2021

@author: Anthony
"""

    
from PIL import Image
from numpy import*
from math import*
from intersect import*
from object import*
from ray import*
from color import*
from multiprocessing import*
from os import*
from glob import*

def main(partBeg,partEn,height,sun,i): 
    l = partEn-partBeg    
    ime = Image.new("RGB",(l,height))     
    pixelColora = ime.load() 
    xp=0
    for x in range(partBeg,partEn):
        for y in range(0,height):
            currentPix = localpix(x,y)
            currentRayPix,direction = calculRay(currentPix)
            RayHit = interSphere(direction,posCam,centerSphere,radiusSphere) 
            pixelColora[xp,y] = tuple(colorPixel(RayHit,direction,sun))
        xp+=1
    ime.save("image\\"+str(i)+".png")
    
            

if __name__ == "__main__" :
    fichiersAsupr = glob("image\\*.png")
    for fichierAsupr in fichiersAsupr:
        remove(fichierAsupr)
    core = cpu_count()
    pas = int(width/core)
    off = width % core
    aled = []
    m = 0
    u = pas+off
    for i in range(0,core):
        char = chr(65+i)
        p=Process(target=main,args=(m,u,height,sun,char))
        p.start()
        m = u
        u += pas
        aled.append(p)
    for um in aled:
        um.join()
        
    partIm =listdir("image\\")
    image1_size = [0,0]
    for i in range(0,core):
        image1 = Image.open("image\\"+partIm[i],mode="r")
        im.paste(image1,(image1_size[0]*i,0))
        im.save("image\\merged_image.jpg","JPEG")
        image1_size = image1.size
    im.show()
