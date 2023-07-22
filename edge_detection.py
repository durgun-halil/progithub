import cv2
# Görüntüyü yükle
image = cv2.imread("segmentasyonn.png")

# Görüntüyü gri tonlamalıya dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# kenar algılama fonksiyonu
def kenar_algila(resim):
    # Resmi gri tonlamaya dönüştür
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    
    # Kenar algılama işlemi için Canny yöntemini kullan
    kenarlar = cv2.Canny(gri_resim, threshold1=120, threshold2=20)
    
    # Kenarları göster
    cv2.imshow("Kenarlar", kenarlar)
    #cv2.imwrite("kenarlar1.png",kenarlar) # # görseli kayıt eder
    cv2.waitKey()
    resim = cv2.imread("segmentasyonn.png")
    cv2.destroyAllWindows()
# Resmi yükle
resim = cv2.imread("segmentasyonn.png")

# Kenar algılama işlemini uygula
kenar_algila(resim)
cv2.waitKey(0)
# Kullanıcının bir tuşa basmasını bekler. 0 parametresi sonsuz bir süre beklemeyi sağlar.

cv2.destroyAllWindows()
# Tüm pencereleri kapatır ve programı sonlandırır.    
    
