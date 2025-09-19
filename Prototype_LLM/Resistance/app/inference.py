# app/inference.py
from ultralytics import YOLO
import os

# Charger le modèle entraîné (à adapter avec ton chemin réel)
MODEL_PATH = os.path.join("C:\\Users\\faury\\Downloads\\Prototype_LLM\\Resistance\\best.pt")

class ResistanceModel:
    def __init__(self, model_path=MODEL_PATH):
        self.model = YOLO(model_path)

    def detect_components(self, image_path: str):
        results = self.model(image_path)
        detections = results[0].names
        boxes = results[0].boxes
        components = []
        for box in boxes:
            cls_id = int(box.cls[0])
            label = detections[cls_id]
            components.append(label.lower())
        return components
