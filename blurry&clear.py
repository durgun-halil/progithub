import cv2 
import numpy as np
# Fotoğrafı yükle
image = cv2.imread("image.png")

blurred = cv2.GaussianBlur(image, (5, 5), 1)

kernel_sharpening = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
usm = cv2.filter2D(blurred, -1, kernel_sharpening)

laplacian = cv2.Laplacian(usm, cv2.CV_64F)

sharpened = cv2.convertScaleAbs(image - laplacian)
output = np.concatenate((image, sharpened), axis=1)

cv2.imshow("Blurred vs Enhanced", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
