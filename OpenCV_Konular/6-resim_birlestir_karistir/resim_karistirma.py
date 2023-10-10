import cv2
import matplotlib.pyplot as plt                     # görselleştirmek için matplotlib kullandım

# blending
img1 = cv2.imread("birinci resmin yolu")
img1= cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)         # rengi RGB formatına dönüştürür

img2 = cv2.imread("ikinci resmin yolu")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)        # rengi RGB formatına dönüştürür

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)           # resimlerin boyutlarına bakıyorum
print(img2.shape)

img1 = cv2.resize(img1,(600,600))       # boyutları eşit yapmam lazım (600,600) belirledim
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img1.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# aşağıdaki denklem şeklinde işliyor karışım değerleri hangi resim baskın olsun istiyorsak değeri ona göre veririz
# alpha birinci resmin saydamlık değeridir
# beta ikinci resmin saydamlık değeridir
# ikiside başlangıçta 1.0 kabul edilir toplam yine 1.0 a tamamlanılır
# blended = alpha*img1 + beta*img2 + gamma
blended = cv2.addWeighted(src1=img1, alpha = 0.3, src2=img2, beta=0.7, gamma = 0)
plt.figure()
plt.imshow(blended)