import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resmin dosya yolu")
img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orjinal Resim")
# eşik değeri belirle
# threshold değeri üzerindekileri beyaz yap altındakileri siyah yap
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.title("Threshold")

"""
Yukarıdaki bölümde eşik değer olarak global bir değer kullandık. 
Ancak görüntünün farklı alanlarda farklı aydınlatma koşullarına sahip olduğu tüm koşullarda iyi olmayabilir.
Bu durumda, uyarlamalı eşiklemeye gidiyoruz. 
Bunda, algoritma görüntünün küçük bir bölgesi için eşiği hesaplar. 
böylece aynı görüntünün farklı bölgeleri için farklı eşikler elde ederiz ve 
bu bize farklı aydınlatmaya sahip görüntüler için daha iyi sonuçlar verir.
"""
# cv2.ADAPTIVE_THRESH_MEAN_C: eşik değeri, seçilen alanın ortalamasıdır.
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.title("Adaptive Threshold")