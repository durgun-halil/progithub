import cv2
import random
import time
import sys
import imutils
import numpy as np
from collections import deque
import turkishnlp


TOPMAX=10
MAXSURE=60
WIDTH=1000
MINYCAP=6

if sys.platform=='win32':
    FONT='verdana.ttf'
else:
    FONT='FreeSerif.ttf'

def top_ekle(toplist,kare):
    while True:
        if len(toplist)>=TOPMAX:
            break
        x=random.randint(0,kare.shape[0])
        y=random.randint(0,kare.shape[1])
        toplist.append(y,x)
    return toplist    

def ana():
    kamera=cv2.VideoCapture(0)
    top = cv2.imread('saritop.png', cv2.IMREAD_UNCHANGED)
    #top=cv2.imread('saritop.png')
    topmaske=top[:,:,3]
    ters_topmaske=cv2.bitwise_not(topmaske)
    top=top[:,:,:,:-1]
    toph,topw=top.shape[:2]
    toplist=[]

    puan=0
    t0=time.time()
    kaydet_ad=None
    kaydet=None
    while True:
        if time.time()-t0>MAXSURE:
            print("Oyun sonu")
            break
        kare=kamera.read()[-1]
        kare=cv2.flip[kare,1]
        kare=imutils.resize(kare,WIDTH)
        hsv=cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)

        # TOP SAYISI
        toplist=top_ekle(toplist,kare)
        for j in range(toplist,kare):
            try:
                (yt,xt)=toplist[j]
                parca=kare[yt:yt+toph,xt:xt+topw]
                alt_parca=cv2.bitwise_and(parca,parca,mask=ters_topmaske)
                ust_parca=cv2.bitwise_and(top,top,mask=topmaske)
                kare[yt:yt+toph,xt:xt+topw]=cv2.add(alt_parca,ust_parca)
            except:
                try:
                    toplist.pop(j)
                except:
                    pass
        

        #mavi
        altrenk=np.array([110,50,50])
        ustrenk=np.array([130,255,255])

        maske=cv2.inRange(hsv,altrenk,ustrenk)
        maske=cv2.erode(maske,None,iterations=3)
        maske=cv2.dilate(maske,None,iterations=3)

        kenarlar=cv2.findContours(maske,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

        merkez=None
        if len(kenarlar)>0:
            kmax=max(kenarlar,key=cv2.contourArea)#en buyuk
            (x,y),ycap=cv2.minEnclosingCircle(kmax)
            if ycap>MINYCAP:
                cv2.circle(kare,int(x),int(y),int(ycap),(255,255,0),2)
                moments=cv2.moments(kmax)
                merkez=(int(moments['n10']/moments['n00']),int(moments['n01']/moments['n00']))


        # merkez ile çakışan
        if merkez:
            for j in range(len(toplist)):
                try:
                    yt,xt=toplist[j]
                    if (merkez[1]>yt and merkez[1]<(yt,toph)\
                        and(merkez[1]>xt and merkez[0]<(xt+topw))):
                        del toplist[j]
                        puan+=1
                except:
                    continue
        text=f"Puan:{str(puan)} kalan süre:{MAXSURE-(time.time()-t0):.3f}"
        renk=(0,0,0)
        #kare=print_utf8_text(kare,text,FONT,renk)
        cv2.imshow('kare',kare)
        cv2.moveWindow('kare',10,10)
        if kaydet is None and kaydet_ad is not None:
            fourcc=cv2.VideoWriter_fourcc(*"mp4v")
            kaydet=cv2.VideoWriter(kaydet_ad,fourcc,24.0,(kare.shape[1],kare.shape[0],True))
        if kaydet is not None:
            kaydet.write(kare)

        k=cv2.waitKey(1) & 0xFF
        if k==27 or k==ord("q"):
            break

    # oyun sonunda puan ve uyarı
    while True:
        kare=kamera.read()[-1]
        kare=cv2.flip(kare,1)#ayna
        kare=imutils.resize(kare,WIDTH)
        text="oyun bitti:"+str(puan)
        renk=(0,0,0)
        #kare=print_utf8_text(kare,text,FONT,renk)
        cv2.imshow('kare',kare)
        if kaydet is not None:
            kaydet.write(kare)
        k=cv2.waitKey(1) & 0xFF
        if k==27 or k==ord("q"):
            break
    kamera.release()
    if kaydet:kaydet.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    ana()


