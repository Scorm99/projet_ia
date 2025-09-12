from ultralytics import YOLO

#utiliser pour train le modèle

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=1,
        device=0  # GPU
    )
