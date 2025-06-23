# main.py
from ultralytics import YOLO

def train_yolo():
    # Load pre-trained YOLOv8 model (nano version)
    model = YOLO('yolov8n.pt')

    # Start training
    model.train(
        data='dataset/data.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
        name='bicycle_yolov8_model',
        workers=2,
        device='cpu'
    )

    # Evaluation
    metrics = model.val()

    # Predict
    model.predict(source='dataset/images/bicycle_0ClfreiNppM.jpg', save=True)


if __name__ == '__main__':
    train_yolo()
