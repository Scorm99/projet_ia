from PIL import Image, ImageDraw
import os, random

os.makedirs("dataset/images", exist_ok=True)
os.makedirs("dataset/labels", exist_ok=True)

colors_list = ["noir","marron","rouge","orange","jaune","vert","bleu","violet","gris","blanc","or","argent"]
color_rgb = {
    "noir": (0,0,0), "marron": (150,75,0), "rouge": (255,0,0),
    "orange": (255,165,0), "jaune": (255,255,0), "vert": (0,128,0),
    "bleu": (0,0,255), "violet": (128,0,128), "gris": (128,128,128),
    "blanc": (255,255,255), "or": (212,175,55), "argent": (192,192,192)
}

num_images = 100
for i in range(num_images):
    img = Image.new("RGB", (300,100), "white")
    draw = ImageDraw.Draw(img)
    
    # Corps résistance
    draw.rectangle([50,30,250,70], fill=(200,200,200), outline="black")
    
    # Choisir 4 bandes aléatoires
    bands = random.sample(colors_list[:10],3) + [random.choice(["noir","marron","rouge","orange","jaune","vert","bleu","violet","or","argent"])]
    
    bboxes = []
    band_width = 15
    for j,color in enumerate(bands):
        x = 50 + 20 + j*(band_width+10)
        draw.rectangle([x,30,x+band_width,70], fill=color_rgb[color], outline="black")
        # Bounding box normalisée YOLO
        x_center = (x + x+band_width)/2 / 300
        y_center = (30+70)/2 / 100
        w = band_width / 300
        h = (70-30)/100
        bboxes.append(f"{colors_list.index(color)} {x_center} {y_center} {w} {h}")
    
    img.save(f"dataset/images/resistor_{i}.png")
    with open(f"dataset/labels/resistor_{i}.txt","w") as f:
        f.write("\n".join(bboxes))
