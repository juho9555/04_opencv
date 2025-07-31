# OpenCV

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


