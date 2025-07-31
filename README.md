# OpenCV

--- 

## 기하학적 변환

- **평행이동 (Translate)**  
  이미지를 지정한 픽셀 수만큼 수평/수직으로 이동시킴.  
  `np.float32`로 이동 행렬을 만들고 `cv2.warpAffine()`으로 적용함.

- **크기 조절 (Scale)**  
  두 가지 방법 사용:  
  1) 행렬 방식으로 직접 비율을 곱하는 방식  
  2) `cv2.resize()`를 사용해 비율 또는 정확한 크기 지정

- **회전 (Rotate)**  
  이미지 중심을 기준으로 회전 행렬 생성 후 `cv2.warpAffine()`으로 회전 적용.

- **아핀 변환 (Affine)**  
  세 점을 기준으로 선형 변환 수행.  
  평행선은 유지되며, 회전/이동/스케일/기울기 조절 가능.

- **투시 변환 (Perspective)**  
  네 점을 기준으로 변환 행렬 생성.  
  실제 문서 스캔이나 시점 왜곡 보정에 사용됨.  
  `cv2.getPerspectiveTransform()`과 `cv2.warpPerspective()` 사용.


---

## 🌫 블러링 (Blurring)

- **평균 블러 (Average Blur)**  
  커널 내부의 픽셀 평균값으로 대체.  
  `cv2.blur()` 또는 직접 커널 정의 방식 모두 실습함.

- **미디언 블러 (Median Blur)**  
  커널 내부 픽셀의 중앙값으로 대체.  
  salt & pepper noise 제거에 효과적.

---

## 에지 검출 (Edge Detection)

- **미분 기반 필터**  
  직접 미분 연산을 적용해 간단한 경계 검출 실습.

- **Roberts Cross**  
  2x2 커널 사용. 빠르지만 노이즈에 민감함.

- **Prewitt**  
  경계 강조용 필터. 간단하지만 Sobel보다 정확도 낮음.

- **Sobel**  
  가장 보편적인 에지 검출 필터.  
  x, y 방향 미분 후 합성. `cv2.Sobel()` 사용.

- **Scharr**  
  Sobel보다 더 정밀한 필터.  
  특히 노이즈가 적은 환경에서 정확도 우수.

- **Laplacian**  
  2차 미분을 이용한 에지 검출.  
  경계뿐 아니라 노이즈도 강조되는 특성이 있음.

- **Canny**  
  가장 정밀하고 널리 쓰이는 에지 검출 방법.  
  노이즈 제거 → 그라디언트 계산 → 비최대 억제 → 이중 임계값 → 경로 추적 순으로 동작.

---

## 번호판 전처리 예제

- **plate_processor.py**  
  이미 번호판 부분만 잘려 저장된 이미지를 대상으로 전처리를 수행함.  
  처리 순서는 다음과 같음:

  1. 이미지를 그레이스케일로 변환 (`cv2.cvtColor`)
  2. 가우시안 블러로 노이즈 제거 (`cv2.GaussianBlur`)
  3. 고정 임계값 이진화 (`cv2.threshold`)
  4. 결과 이미지를 새로운 폴더에 저장

  외곽선 추출이나 ROI 설정 없이,  
  저장된 번호판 이미지를 일괄적으로 불러와 전처리하는 방식.

  ```bash
  ../extracted_plates 폴더 → 처리 → ../processed_plates 폴더로 저장

  
### 1. 입력 및 출력 폴더 설정
- 입력 폴더: `../extracted_plates`
- 출력 폴더: `../processed_plates`  
  (출력 폴더가 없으면 자동 생성)

### 2. 이미지 파일 필터링
- `car`로 시작하는 `.png` 파일만 처리 대상에 포함

### 3. 개별 이미지 처리 함수: `process_plate_image(img_path)`
- 이미지 읽기
  - `cv2.imread()`로 이미지 로드 실패 시 경고 출력 후 종료
- 그레이스케일 변환
  - 컬러 이미지를 흑백으로 변환 (`cv2.COLOR_BGR2GRAY`)
- 가우시안 블러 적용
  - 커널 크기 (7x7)와 표준편차 0으로 노이즈 제거
- 고정 임계값 이진화
  - 임계값 120, 픽셀 값 반전 (`cv2.THRESH_BINARY_INV`)으로 이진 이미지 생성
- 결과 저장
  - 원본 파일명 그대로 출력 폴더에 저장

### 4. 전체 이미지 처리 함수: `process_all()`
- 출력 폴더가 없으면 생성
- 입력 폴더에서 조건에 맞는 이미지 리스트 생성 및 정렬
- 각 이미지에 대해 `process_plate_image` 함수 호출

---

### 실행

- 스크립트를 직접 실행하면 `process_all()` 함수가 실행되어, 조건에 맞는 모든 이미지가 한 번에 처리된다.

```bash
python plate_processor.py
```

---
  
### 결과 이미지  
  
<img width="300" height="150" alt="car_04" src="https://github.com/user-attachments/assets/71959bc3-0795-4ad2-8ce7-e9a9ffef3ef1" />

<img width="300" height="150" alt="car_05" src="https://github.com/user-attachments/assets/5842ae06-53ac-4b7d-8cd1-ff86eef194e5" />  
