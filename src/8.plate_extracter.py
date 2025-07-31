import cv2
import numpy as np
import os
import datetime

save_dir = "extracted_plates"

def process_images(image_paths):
    win_name = "scanning" # 스캔하는 창 이름 
    
    for path in image_paths: # 이미지를 하나씩 불러오기
        img = cv2.imread(path)
        if img is None:
            print(f"failed load image: {path}")
            continue
        
        draw = img.copy()
        pts = np.zeros((4, 2), dtype=np.float32) # 클릭 좌표 4개를 저장할 배열
        pts_cnt = 0