# app/inference.py
from ultralytics import YOLO
import os

# Charger le modèle entraîné (à adapter avec ton chemin réel)
MODEL_PATH = os.path.join("runs\\detect\\train\\weights\\best.pt")


class ResistanceModel:
    def __init__(self, model_path=MODEL_PATH):
        self.model = YOLO(model_path)

    def predict(self, image_path: str, prompt: str = "") -> str:
        """
        Analyse une image de composant et retourne la prédiction.
        Le prompt peut servir plus tard pour enrichir la réponse.
        """
        results = self.model(image_path)  # inférence
        # YOLOv8 renvoie une liste de résultats
        detections = results[0].names  # dictionnaire id->label
        boxes = results[0].boxes
        output_text = f"Prompt: {prompt}\n\n"
        for box in boxes:
            cls_id = int(box.cls[0])
            label = detections[cls_id]
            conf = float(box.conf[0])
            output_text += f"→ {label} (confiance: {conf:.2f})\n"
        return output_text
