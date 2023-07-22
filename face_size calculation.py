import cv2

# Load the pre-trained classifier for detecting objects
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect objects in the grayscale frame
    objects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Loop through each detected object and draw a rectangle around it
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Calculate the size of the object in pixels
        object_size = w * h
        
        # Display the object size in the frame
        cv2.putText(frame, f"Size: {object_size} pixels", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Object Size Detector', frame)
    
    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
