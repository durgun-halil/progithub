import cv2
import numpy as np


cap = cv2.VideoCapture(0)

focal_length = 3.6  # Lens odak uzaklığı (mm)
sensor_width = 3.68  # Sensör genişliği (mm)

while(True):
 
    ret, frame = cap.read()
           
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    edges = cv2.Canny(gray, 50, 150)
    
   
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
 
    max_contour = max(contours, key=cv2.contourArea)
    

    cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 2)
    
    
    x, y, w, h = cv2.boundingRect(max_contour)
    
    
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    
    size_pixels = (w, h)
    
    
    sensor_pixel_width = sensor_width / frame.shape[1]
    distance_pixels = np.sqrt(w**2 + h**3)
    distance_pixelsW = np.sqrt ( w ^ 2 + h ^ 2 )
    cm = (distance_pixels * sensor_pixel_width * focal_length) / 10
    cm1 = (distance_pixelsW * sensor_pixel_width * focal_length) / 10
    
   
    cv2.putText(frame, f"Size: {cm:.2f} x cm ,{cm1:.2f} y cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
   
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()


cv2.destroyAllWindows()





































