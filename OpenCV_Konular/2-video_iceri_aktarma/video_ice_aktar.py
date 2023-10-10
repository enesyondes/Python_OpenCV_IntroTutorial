import cv2 

video_name = "video dosya yolu"

cap = cv2.VideoCapture(video_name)      # video'yu cap değişkenine al

if cap.isOpened() == False:             # video gelmediyse hata ver
    print("Error")

else:                                   
    while True:                         # kare kare oynatmak için döngüye gir
        ret, frame = cap.read()         # cap.read() sonucu oluşan iki değeri ata

        frame = cv2.resize(frame, (960, 540))       # kare pixel boyutunu istediğin gibi ayarla

        cv2.imshow("Video",frame)       # kareyi ekrana ver
        cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == ord(27):        # esc basarak çık videodan (döngüden)
            break

cap.release()               # capture durdur
cv2.destroyAllWindows()