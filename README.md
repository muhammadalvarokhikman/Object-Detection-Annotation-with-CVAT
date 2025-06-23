# Object Detection Annotation with CVAT

https://github.com/user-attachments/assets/7dfe1dbf-744c-4827-a366-45c40b5b96d3

This project demonstrates object detection dataset creation using CVAT and YOLOv8 model training.

## Project Structure
Object-Detection-Annotation-with-CVAT/
- dataset/ # Contains images/, labels/, and data.yaml
- runs/detect/ # YOLOv8 training outputs (metrics, weights)
- main.py # YOLOv8 training script
- scrapping.ipynb # Image downloader via Unsplash API
- yolov8n.pt # Pretrained YOLOv8n model weights
- README.md # Project documentation

## 🧠 Model Training (YOLOv8)
```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(
    data='dataset/data.yaml',
    epochs=50,
    imgsz=640,
    batch=16,
    device='cpu'
)
```

## Annotation Info
- Tool: CVAT
- Format: YOLOv5-compatible (.txt per image)
- Label: bicycle

## Dataset Info
- Images: Downloaded via Unsplash API (scrapping.ipynb)
- Labels: Manually annotated with bounding boxes in CVAT

## Output
- Trained model: runs/detect/bicycle_yolov8_model/weights/best.pt
- Results: mAP, loss, and sample predictions available after training

## Credits
- Ultralytics YOLOv8
- CVAT Annotation Tool
- Image via Unsplash API:
    - images/bicycle_tG36rvCeqng.jpg | Credit: Robert Bye
    - images/bicycle_yjAFnkLtKY0.jpg | Credit: Mikkel Bech
    - images/bicycle_igKjieyjcko.jpg | Credit: Carl Nenzen Loven
    - images/bicycle_0ClfreiNppM.jpg | Credit: Tiffany Nutt
    - images/bicycle_Lpqg7ypu2B4.jpg | Credit: Chris Barbalis
    - images/bicycle_AoSAOV2Vtro.jpg | Credit: Alejandro Lopez
    - images/bicycle_IlR3M0BMrWQ.jpg | Credit: Alesia Kazantceva
    - images/bicycle_1ow9zrlldJU.jpg | Credit: Patrick Hendry
    - images/bicycle_sw9Vozf6j_4.jpg | Credit: Dmitrii Vaccinium
    - images/bicycle_RRcYcdGY630.jpg | Credit: Daniel Salcius
    - images/bicycle_nPOtzvGLYW0.jpg | Credit: Jonny Kennaugh
    - images/bicycle_OxzhYtL-00Y.jpg | Credit: Alexander Shustov
    - images/bicycle_giFeTshEYYQ.jpg | Credit: Jacek Dylag
    - images/bicycle_XVTWFHcNIko.jpg | Credit: Josh Nuttall
    - images/bicycle_JXIc86xKJRM.jpg | Credit: Andrik Langfield
    - images/bicycle_WeBASN7ESOY.jpg | Credit: Marc Kleen
    - images/bicycle_OFyh9TpMyM8.jpg | Credit: Coen van de Broek
    - images/bicycle_JK6lD_y3aDg.jpg | Credit: Solé Bicycles
    - images/bicycle_jpgJSBQtw5U.jpg | Credit: Mac Blades
    - images/bicycle_zeutQl8ooeU.jpg | Credit: Zoltan Tasi
    - images/bicycle_4yfdgmbgBWU.jpg | Credit: Didier Weemaels
    - images/bicycle_zkVi57UYHIQ.jpg | Credit: Josh Nuttall
    - images/bicycle_cAY9X4rPG3g.jpg | Credit: Alessandra Caretto
    - images/bicycle_pIwu5XNvXpk.jpg | Credit: Josh Nuttall
    - images/bicycle_zbFU4MM9WGQ.jpg | Credit: Solé Bicycles
