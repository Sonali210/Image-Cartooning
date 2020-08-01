import cv2
import numpy as np

name = input("Enter name: ")
cam = cv2.VideoCapture(0)
cv2.namedWindow("Capture")

while True:
    ret, frame = cam.read()
    '''if not ret:
                    print("failed to grab frame")
                    break'''
    cv2.imshow("Capture", frame)

    k = cv2.waitKey(1)
    if k%256 == 32:
        cv2.imwrite('static\\' + str(name) + ".jpg", frame)
        print("{} written!".format(name))
        cam.release()
        
        img_original = cv2.imread('static\\' + str(name) + ".jpg")
        img_resize = cv2.resize(img_original, (700, 600), interpolation=cv2.INTER_CUBIC)
        for i in range(50):
            img_bilateral_filter = cv2.bilateralFilter(img_resize, 9, 9, 7)
            img_gray = cv2.cvtColor(img_bilateral_filter, cv2.COLOR_BGR2GRAY)
            img_median_blur = cv2.medianBlur(img_gray, 9)
            img_adaptive_threshold = cv2.adaptiveThreshold(img_median_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
            img_color = cv2.cvtColor(img_adaptive_threshold, cv2.COLOR_GRAY2BGR)
            img_cartoon = cv2.bitwise_and(img_resize, img_color)
            cv2.imshow('Cartoonized Image', img_cartoon)
            cv2.imwrite('cartoon\\' + str(name) + ".jpg", img_cartoon)
cv2.destroyAllWindows()