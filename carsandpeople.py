import cv2
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

video = cv2.VideoCapture('ornek3.mp4')

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5, minSize=(30, 30))
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    car_count = len(cars)
    
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    human_count = len(humans)
    
    cv2.putText(frame, "Cars: " + str(car_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.putText(frame, "Humans: " + str(human_count), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()