import cv2
import numpy as np


def calculate_pixel_difference(image1, image2):
  
    if image1.shape != image2.shape:
       
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    
    difference = cv2.absdiff(image1, image2)
    difference = np.sum(difference) / (image1.shape[0] * image1.shape[1])

    return difference


image1 = cv2.imread("kenarlaaar.png")
image2 = cv2.imread("kenar.png")


pixel_diff = calculate_pixel_difference(image1, image2)
print("Piksel Farkı:", pixel_diff)

cv2.waitKey(0)
cv2.destroyAllWindows()




























"""
import cv2
import numpy as np
# İki resim arasındaki piksel farkını hesaplayan fonksiyon
def calculate_pixel_difference(image1, image2):
    # İki resmin boyutunu kontrol et
    if image1.shape != image2.shape:
        # Boyutları eşitlemek için küçük resmi yeniden boyutlandır
        if image1.shape[0] > image2.shape[0] or image1.shape[1] > image2.shape[1]:
            image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
        else:
            image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Piksel farkını hesapla
    difference = cv2.absdiff(image1, image2)
    difference = np.sum(difference)

    return difference

# İki resmi yükle
image1 = cv2.imread("kenarlaaar.png")
image2 = cv2.imread("segmentasyonn.png")

# Piksel farkını hesapla
pixel_diff = calculate_pixel_difference(image1, image2)
print("Piksel Farkı:", pixel_diff)
cv2.waitKey(0)
# Kullanıcının bir tuşa basmasını bekler. 0 parametresi sonsuz bir süre beklemeyi sağlar.

cv2.destroyAllWindows()
# Tüm pencereleri kapatır ve programı sonlandırır.
"""
