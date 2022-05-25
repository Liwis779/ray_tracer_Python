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
from random import*
#[i,d,touchPos,colorHit,RayHit]

def randSphere(nb):
    for i in range(nb):
        form = []
        form.append("sphere")
        form.append(uniform(0.5,1))
        form.append([uniform(-5,100),uniform(-5,5),uniform(5,1)])
        form.append([uniform(50,200),uniform(50,200),uniform(50,200)])
        figure.append(form)
        



def main(partBeg,partEn,hbeg,hend,sun,i,objet): 
    l = partEn-partBeg #longeur section
    L = hend-hbeg # largeur section
    ime = Image.new("RGB",(l,L)) #creation image    
    pixelColor = ime.load() #chargement de la matrice d'image
    xp=0
    yp=0
    for x in range(partBeg,partEn):
        yp=0
        for y in range(hbeg,hend):
            currentPix = localpix(x,y)
            currentRayPix,direction = calculRay(currentPix)
            computedRay = colorCompute(currentPix, direction, objet)
            if computedRay[4] == False:
                pixelColor[xp,yp] =  tuple([100,100,100]) #colorSky(direction,sunVec)
            else:
                LightVecComputed = colorCompute(computedRay[3], computedRay[6], objet)
                if LightVecComputed[4]==True:
                    pixelColor[xp,yp]=tuple([0,0,0])
                else:
                    pixelColor[xp,yp] = colorObj(computedRay[6],computedRay[3],computedRay[5])
            yp+=1
        xp+=1
    ime.save("image\\"+str(i)+".png")
    

if __name__ == "__main__" :
    randSphere(20)
    fichiersAsupr = glob("image\\*.png")
    
    for fichierAsupr in fichiersAsupr:
        remove(fichierAsupr)
    
    core = cpu_count()
    pas = int(width/(core/2))
    off = int(width % (core/2))
    aled = []
    
    #width part calcul
    m = 0
    u = pas+off
    
    #height part calcul
    hup = int(ceil(height/2))
    for i in range(0,int((core/2))):
            #part up
            char = chr(65+i)
            p=Process(target=main,args=(m,u,0,hup,sun,char,figure))
            p.start()
            aled.append(p)
            m = u
            u += pas
    #part down
    m=0
    u=pas+off
    for i in range(int(core/2),core):
            char = chr(65+i)
            p=Process(target=main,args=(m,u,hup,height,sun,char,figure))
            p.start()
            aled.append(p)
            m = u
            u += pas
    for um in aled:
        um.join()
        
    partIm =listdir("image\\")
    image1_size = [0,0]
    
    for i in range(0,int((core/2))):
        image1 = Image.open("image\\"+partIm[i],mode="r")
        im.paste(image1,(image1_size[0]*i,0))    
        im.save("image\\merged_image.png","png")
        image1_size = image1.size
        
    image1_size = [0,0]
    count = 0
    
    for i in range(int(core/2),core):
        image1 = Image.open("image\\"+partIm[i],mode="r")
        im.paste(image1,(image1_size[0]*count,hup))
        im.save("image\\merged_image.png","png")
        image1_size = image1.size
        count+=1
    im.show()


#main(0,500,0,500,sun,'a',figure)

