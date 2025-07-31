import cv2
import numpy as np

img = cv2.imread('../img/gaussian_noise.jpg')

#blur() 함수로 블러링
blur1 = cv2.blur(img, (10, 10))
#boxFilter() 함수로 블러링 적용
blur2 = cv2.boxFilter(img, -1, (10, 10))

#결과 출력
merged = np.hstack((img, blur1, blur2))
cv2.imshow('blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
