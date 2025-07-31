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

        def onMouse(event, x, y, flags, param):
            nonlocal pts_cnt, draw # global로 하면 반복되면서 오류남

            # 마우스로 점 4개까지 찍을수있게 함
            if event == cv2.EVENT_LBUTTONDOWN and pts_cnt < 4:
                cv2.circle(draw, (x, y), 5, (0, 255, 0), -1)
                cv2.imshow(win_name, draw) #이미지 표시

                pts[pts_cnt] = [x, y] # 클릭한 좌표를 배열에 저장
                pts_cnt += 1

                # 4개 점 모두 클릭했으면 원근 변환 시작
                if pts_cnt == 4:
                    sm = pts.sum(axis=1)
                    diff = np.diff(pts, axis=1)

                    topLeft = pts[np.argmin(sm)]
                    bottomRight = pts[np.argmax(sm)]
                    topRight = pts[np.argmin(diff)]
                    bottomLeft = pts[np.argmax(diff)]

                    pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

                    # scan된 번호판 크기 정렬
                    width = 300
                    height = 150

                    #변환 후 좌표(0,0) 기준 모서리 지정
                    pts2 = np.float32([[0, 0], [width-1, 0],
                                       [width-1, height-1], [0, height-1]])