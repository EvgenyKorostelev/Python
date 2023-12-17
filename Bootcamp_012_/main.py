import cv2

img = cv2.imread('C:\Users\ddc_s\OneDrive\Рабочий стол\Python\Bootcamp_012_\Joker.jpg')

#img = cv2.resize(img, (500, 500))

cv2.imshow('Result', img)

cv2.waitKey(0)