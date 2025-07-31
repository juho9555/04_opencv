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

    # 1. 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. 가우시안 블러 (노이즈 제거)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # 3. 고정 임계값 이진화 (adaptive threshold 대신)
    _, binary = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)

    # 4. 저장
    base_name = os.path.basename(img_path)
    save_path = os.path.join(output_dir, base_name)
    cv2.imwrite(save_path, binary)
    print(f'저장 완료: {save_path}')

def process_all():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 파일명이 'car'로 시작하고 .png인 것만 처리
    image_files = [f for f in os.listdir(input_dir) if f.startswith('car') and f.endswith('.png')]
    image_paths = [os.path.join(input_dir, f) for f in sorted(image_files)]

    for path in image_paths:
        process_plate_image(path)

if __name__ == "__main__":
    process_all()