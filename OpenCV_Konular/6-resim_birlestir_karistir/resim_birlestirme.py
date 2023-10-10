import cv2
import numpy as np

# biz tek resmi yan yana veya alt alta birleştireceğiz ikinci bir resim ekleyip onunla yapabilirsiniz
img = cv2.imread("resim dosya yolu")
cv2.imshow("Orjinal", img)

hor = np.hstack((img,img))              # yatay
cv2.imshow("Horizontal Image", hor)

ver = np.vstack((img,img))              # dikey
cv2.imshow("Vertical Image", ver)

cv2.waitKey(0)