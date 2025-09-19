from ultralytics import YOLO

model = YOLO("yolov8s.pt")  # modèle small pré-entraîné
model.train(data="resistor_dataset.yaml", epochs=50, imgsz=640)
