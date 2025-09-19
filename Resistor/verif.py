from ultralytics import YOLO

#utiliser pour vérifier une image, l'image vérifier sera sous format result.jpg

# Charger ton modèle entraîné
model = YOLO("runs/detect/train/weights/best.pt")

# Chemin vers ton image
img_path = r"dataset\test\images\IMG_20250314_144926_556_jpg.rf.1eaebad7247d310abb0aa000e5218979.jpg"

# Faire la prédiction et afficher directement
results = model(img_path, show=True)  

# Sauvegarder l'image annotée
results[0].save("result.jpg")  
print("✅ Résultat enregistré dans result.jpg")


