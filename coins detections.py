import cv2

# Bozuklukların değerlerini tanıtma
bir_lira_ornek = cv2.imread("birlira.png")
bir_lira_degeri = 1.0

elli_kurus_ornek = cv2.imread("ellikurus.png")
elli_kurus_degeri = 0.5

yirmi_bes_kurus_ornek = cv2.imread("25kurus.png")
yirmi_bes_kurus_degeri = 0.25

on_kurus_ornek = cv2.imread("10kurus.png")
on_kurus_degeri = 0.10

bes_kurus_ornek = cv2.imread("5kurus.png")
bes_kurus_degeri = 0.05

bir_kurus_ornek = cv2.imread("1kurus.png")
bir_kurus_degeri = 0.01

# Görüntü işlemleri
cember = True
kare = cv2.imread("lira2.png")
blur = cv2.GaussianBlur(kare, (3, 3), 0)
canny = cv2.Canny(blur, 30, 250)

karnel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
morf = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, karnel)

konturlar, _ = cv2.findContours(morf.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

say = 0
threshold = 0.6  # Threshold değerini uygun bir şekilde ayarlayın
toplam_tl = 0
threshold1 = 0.7

for kontur in konturlar:
    alan = cv2.contourArea(kontur)
    if alan > 10000:
        say = say + 1
        (x, y, w, h) = map(int, cv2.boundingRect(kontur))
        cv2.rectangle(kare, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if cember:
            (x, y), ycap = cv2.minEnclosingCircle(kontur)
            merkez = (int(x), int(y))
            ycap = int(ycap)
            img = cv2.circle(kare, merkez, ycap, (255, 0, 0), 2)

            # Bozukluğun değerini tespit etme
            bozukluk_resim = kare[int(y):int(y + h), int(x):int(x + w)]
            uyuşum_degeri = None

            # Bir lira
            uyuşum = cv2.matchTemplate(bozukluk_resim, bir_lira_ornek, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(uyuşum)
            if max_val > threshold:
                uyuşum_degeri = bir_lira_degeri

             # 50 kuruş
            uyuşum = cv2.matchTemplate(bozukluk_resim, elli_kurus_ornek, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(uyuşum)
            if max_val > threshold:
                   uyuşum_degeri = elli_kurus_degeri    

            # 25 kuruş
            uyuşum = cv2.matchTemplate(bozukluk_resim, yirmi_bes_kurus_ornek, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(uyuşum)
            if max_val > threshold:
                uyuşum_degeri = yirmi_bes_kurus_degeri     

            # 10 kuruş
            uyuşum = cv2.matchTemplate(bozukluk_resim, on_kurus_ornek, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(uyuşum)
            if max_val > threshold:
                uyuşum_degeri = on_kurus_degeri   

            # 5 kuruş
            #uyuşum = cv2.matchTemplate(bozukluk_resim, bes_kurus_ornek, cv2.TM_CCOEFF_NORMED)
            #_, max_val, _, _ = cv2.minMaxLoc(uyuşum)
            #if max_val > threshold:
             # uyuşum_degeri = bes_kurus_degeri

           # 1 kuruş
            #uyuşum = cv2.matchTemplate(bozukluk_resim, bir_kurus_ornek, cv2.TM_CCOEFF_NORMED)
            #_, max_val, _, _ = cv2.minMaxLoc(uyuşum)
            #if max_val > threshold:
             #  uyuşum_degeri = bir_kurus_degeri   
       

           

            if uyuşum_degeri is not None:
                # Bozukluğun değerini toplama ekleme
                toplam_tl += uyuşum_degeri

                # Bozukluğun değerini yazdırma
                print("Tespit edilen bozukluğun değeri:", uyuşum_degeri)

if say > 0:
    cv2.putText(kare, f"{say} bozukluk bulundu", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Toplam TL değerini yazdırma
print("Toplam TL değeri:", toplam_tl)

cv2.imshow('kare', kare)
cv2.waitKey(0)



