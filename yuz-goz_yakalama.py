from pickle import NONE
from tkinter import N
from tkinter.messagebox import NO
import cv2

yuzCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gozCascade=cv2.CascadeClassifier('haarcascade_eye.xml')

kamera=cv2.VideoCapture(0)
kamera.set(3,1280)#genişlik
kamera.set(4,720)#yükseklik
dosyaad=None
kaydedici=None
while True:
    _,kare=kamera.read()
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler=yuzCascade.detectMultiScale(
        gri,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(20,20)
    )

    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
        gri_kutu=gri[y:y+h,x:x+w]
        renkli_kutu=kare[y:y+h,x:x+w]
        gozler=gozCascade.detectMultiScale(
            gri_kutu,
            scaleFactor=1.5,
            minNeighbors=10,
            minSize=(3,3)
        )
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(renkli_kutu,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('kare',kare)
    if kaydedici is None and dosyaad is not None:
        fourcc=cv2.VideoWriter_fourcc(dosyaad,fourcc,24.0,kare.shape[1],kare.shape[0],True)
    if kaydedici is not None:
        kaydedici.write(kare)
    k=cv2.waitKey(10) & 0xff
    if k==27 or k==ord('q'):
        break
kamera.release()
if kaydedici:
    kaydedici.release()
cv2.destroyAllWindows()                        