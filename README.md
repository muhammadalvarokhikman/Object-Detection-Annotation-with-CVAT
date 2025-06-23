# Object Detection Annotation with CVAT

https://github.com/user-attachments/assets/7dfe1dbf-744c-4827-a366-45c40b5b96d3

This project demonstrates the creation of an object detection dataset using **CVAT** and training a YOLOv8 model on it.

## Project Structure
Object-Detection-Annotation-with-CVAT/
├── dataset/ # Contains images/, labels/, and data.yaml
├── runs/detect/ # YOLOv8 training outputs (metrics, weights)
├── main.py # YOLOv8 training script
├── scrapping.ipynb # Image downloader via Unsplash API
├── yolov8n.pt # Pretrained YOLOv8n model weights
└── README.md # Project documentation


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
Tool: CVAT
Format: YOLOv5-compatible (.txt per image)
Label: bicycle

## Dataset Info
Images: Downloaded via Unsplash API (scrapping.ipynb)
Labels: Manually annotated with bounding boxes in CVAT

## Output
Trained model: runs/detect/bicycle_yolov8_model/weights/best.pt
Results: mAP, loss, and sample predictions available after training

## Credits
Ultralytics YOLOv8
CVAT Annotation Tool
Unsplash API
