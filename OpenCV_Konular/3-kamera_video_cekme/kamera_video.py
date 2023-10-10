import cv2

cap = cv2.VideoCapture(0)       # video kaynağı olarak kamera seçtik

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      # kamera pixel değerlerini alıyoruz (width,height)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)

writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width,height))    # videoyu kaydetmek için yazıcı oluşturuyoruz

while True:
    ret, frame = cap.read() 
    writer.write(frame)     # kare kare yazıyoruz videoyu kaydetmek için
    cv2.imshow("frame", frame)  
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break           # q ile çıkıyoruz

cap.release() # capture durdur
writer.release()
cv2.destroyAllWindows()