import cv2
import numpy as np
import time
import time
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

global start_time
start_time=0


cap=cv2.VideoCapture(0)

lower_range=np.array([0,104,160])
upper_range=np.array([179,255,255])

while True:
    
    ret,frame=cap.read()

    
    cv2.resize(frame, (800, 600),interpolation = cv2.INTER_LINEAR)

    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    
    mask=cv2.inRange(hsv,lower_range,upper_range)

 
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)

   
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

  
    cv2.line(frame, (0,240), (640,240), (255,0,0), 3)

    
    for c in cnts:
        x=2000
        
        if cv2.contourArea(c)>x:

           
            x,y,w,h=cv2.boundingRect(c)
            if  y < 240:

                
                cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
                start_time=time.time()

            if (time.time()-start_time) > 5:

               
                cv2.putText(frame,("NORMAL DEGIL"),(500,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
                import webbrowser
                import pyautogui
             
                to_email = "yourmail@gmail.com"
                subject = "E-posta Konusu"
                message = "Anormal bir durum tespit edildi."


                mailto_link = f"mailto:{to_email}?subject={subject}&body={message}"
                webbrowser.open(mailto_link) 
                time.sleep(2)
              
                send_button_position = pyautogui.locateCenterOnScreen("send_button.png", confidence=0.8)


                if send_button_position is not None:
                 pyautogui.click(send_button_position)
                else:
                    print("Gönder düğmesi bulunamadı.")
               


                
                




           
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    
    cv2.imshow("FRAME",frame)

    
    if cv2.waitKey(1)&0xFF==27:
        break
    
cap.release()
cv2.destroyAllWindows()




