import cv2

img = cv2.imread("resim yolumuzu giriyoruz")

cv2.imshow(winname="resim", mat=img)
cv2.waitKey(0)
