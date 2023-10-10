import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")


img = cv2.imread("resmin dosya yolu")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal Görüntü")


"""
iki bulanıklaştırma yöntemini uygulayacağız
1-Ortalama Bulanıklaştırma
2-Gaussian Bulanıklaştırma

Ortalama Bulanıklaştırma: Bu yöntemin algoritmasında bir hayali kutu çalışır bizim belirlediğimiz bu kutu
-örneğin (3,3) olsun- tüm pikselleri en köşeden başlayarak dolaşır ve her üzerine geldiği alanın ortalama
değerini alır ve o alana uygular bu şekilde ortalama bulanıklaştırma yöntemi elde edilir
"""

dst2 = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Ortalama Bulanıklaştırma")

"""
Gauss Bulanıklaştırma: Bu yöntemde kutu filtresi yerine Gauss çekirdeği kullanılır.
Bu, cv.GaussianBlur () işleviyle yapılır. 
Pozitif ve tek olması gereken çekirdeğin genişliğini ve yüksekliğini belirtmeliyiz. 
Sırasıyla sigmaX ve sigmaY X ve Y yönlerindeki standart sapmayı da belirtmeliyiz. 
Yalnızca sigmaX belirtilirse, sigmaY, sigmaX ile aynı şekilde alınır. 
Her ikisi de sıfır olarak verilirse, çekirdek boyutundan hesaplanır. 
Gauss bulanıklığı, bir görüntüden Gauss gürültüsünün giderilmesinde oldukça etkilidir.
"""
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gauss Bulanıklaştırma")

# Bulanıklaştırma yöntemleri genelde Noise(gürültü) giderilmesinde kullanılır.
# Bir kaç noise çeşitleri şunlardır:Salt-Pepper Noise, Gaussian Noise