# 샤르 마스크로 경계 검출 

import cv2
import numpy as np

img = cv2.imread("../img/sudoku.jpg")

# 샤르 커널 생성
gx_kernel = np.array([[ -3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
gy_kernel = np.array([[-3, -10, -3],[0, 0, 0], [3, 10, 3]])

# 필터 적용
edge_gx = cv2.filter2D(img, -1, gx_kernel)
edge_gy = cv2.filter2D(img, -1, gy_kernel)

# 샤르 API를 생성해서 엣지 검출
scharrx = cv2.Scharr(img, -1, 1, 0)
scharry = cv2.Scharr(img, -1, 0, 1)

# 결과 출력
merged1 = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
merged2 = np.hstack((img, scharrx, scharry, scharrx+scharry))
merged = np.vstack((merged1, merged2))
cv2.imshow('Scharr', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()