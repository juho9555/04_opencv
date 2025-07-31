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