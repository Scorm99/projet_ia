# app/app.py
import gradio as gr
from inference import ResistanceModel

model = ResistanceModel()

def chatbot(prompt, image):
    if image is None:
        return "⚠️ Merci de charger une image de composant."
    return model.predict(image, prompt)

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Reconnaissance de Composants Électroniques")

    with gr.Row():
        prompt_input = gr.Textbox(label="Entre ton prompt (ex: 'Quel est ce composant ?')")
    
    with gr.Row():
        image_input = gr.Image(type="filepath", label="Upload une image de composant")
    
    with gr.Row():
        output = gr.Textbox(label="Résultat du modèle")
    
    submit_btn = gr.Button("Analyser")
    submit_btn.click(fn=chatbot, inputs=[prompt_input, image_input], outputs=output)

demo.launch()
