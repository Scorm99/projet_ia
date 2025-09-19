# app/app.py
import gradio as gr
from inference import ResistanceModel
 
model = ResistanceModel()
 
def chatbot(image):
    if image is None:
        return "⚠️ Merci de charger une image de composant."
    # On ne prend plus de 'prompt', tu peux mettre un prompt fixe si besoin
    return model.predict(image, "")
 
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Reconnaissance de Composants Électroniques")
 
    with gr.Row():
        image_input = gr.Image(type="filepath", label="Upload une image de composant")
 
    submit_btn = gr.Button("Analyser")
   
    with gr.Row():
        output = gr.Textbox(label="Quelle est la résistance ici ?", lines=5)
   
    submit_btn.click(fn=chatbot, inputs=image_input, outputs=output)
 
demo.launch()