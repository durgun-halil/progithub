import cv2
# Görüntüyü yükle
image = cv2.imread("gorsel1.png")

# Görüntüyü gri tonlamalıya dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşikleme işlemi uygula
# İkinci parametre olarak verilen 120 değeri, eşikleme işlemi için kullanılacak eşik değeridir.
# Daha parlak pikseller beyaz olarak, daha koyu pikseller ise siyah olarak işaretlenecektir.
_, thresholded = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Segmentasyon sonucunu göster
cv2.imshow("Segmentasyon", thresholded)
# imshow fonksiyonuyla "Segmentasyon" adında bir pencere açılır ve segmentasyon sonucu gösterilir.

cv2.imwrite("segmentasyonn.png", thresholded) # görseli kayıt eder

cv2.waitKey(0)
# Kullanıcının bir tuşa basmasını bekler. 0 parametresi sonsuz bir süre beklemeyi sağlar.

cv2.destroyAllWindows()
# Tüm pencereleri kapatır ve programı sonlandırır.