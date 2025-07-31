import cv2
import numpy as np
import os

input_dir = '../extracted_plates'
output_dir = '../processed_plates'

def process_plate_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print(f'이미지 불러오기 실패: {img_path}')
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray_eq = cv2.equalizeHist(gray) # 히스토그램 평활화

    blurred = cv2.GaussianBlur(gray_eq, (5, 5), 0) # 가우시안 블러 적용

    # 적응형 임계처리
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # 윤곽선 검출
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 1)