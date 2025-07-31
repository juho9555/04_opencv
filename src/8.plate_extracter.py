import cv2
import numpy as np
import os
import datetime

save_dir = "../extracted_plates"

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
                    width, height = 300, 150

                    #변환 후 좌표(0,0) 기준 모서리 지정
                    pts2 = np.float32([[0, 0], [width-1, 0], [width-1, height-1], [0, height-1]])
                    
                    # 원근 변환 행렬
                    mtrx = cv2.getPerspectiveTransform(pts1, pts2)
                    # 원근 변환 적용 및 출력
                    result = cv2.warpPerspective(img, mtrx, (width, height))
                    
                    # 저장 파일명 설정 - 방식 1: 타임스탬프 기반
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"plate_{timestamp}.png"

                    # 저장 경로
                    save_path = os.path.join(save_dir, filename)

                    # 이미지 저장
                    success = cv2.imwrite(save_path, result)
                    if success:
                        print(f"번호판 저장 완료: {save_path}")
                        cv2.imshow('Extracted Plate', result)
                    else:
                        print("저장 실패!")

        cv2.imshow(win_name, draw)
        cv2.setMouseCallback(win_name, onMouse)
        
        while True:
            key = cv2.waitKey(1)
            if pts_cnt == 4:  # Enter 키 누르면 다음 이미지
                break
            elif key == 27:  # ESC 키 누르면 종료
                exit()
        cv2.destroyAllWindows()

# 이미지 경로 리스트 정의 (이건 경로에 맞게 수정하세요)
image_paths = [f'../img/car0{i}.jpg' for i in range(1, 6)]


# 함수 실행
process_images(image_paths)
