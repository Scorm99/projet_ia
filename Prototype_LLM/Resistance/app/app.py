# app/app.py

from huggingface_hub import login

# Replace with your actual token
hf_token = "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"
login(token=hf_token)

import gradio as gr
from chatbot import get_required_components
from inference import ResistanceModel
from verifier import check_components

model = ResistanceModel()

def full_pipeline(prompt, image):
    # 1. Chatbot
    response_text, required = get_required_components(prompt)

    # 2. Vision
    if image is None:
        return response_text, "⚠️ Pas d'image fournie", ""

    detected = model.detect_components(image)

    # 3. Vérification
    verdict = check_components(required, detected)

    return response_text, f"Composants détectés : {', '.join(detected)}", verdict


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Chatbot & Reconnaissance de composants")

    with gr.Row():
        prompt_input = gr.Textbox(label="Demande ton filtre (ex: 'fais-moi un filtre passe-haut')")
    
    with gr.Row():
        image_input = gr.Image(type="filepath", label="Upload une image des composants disponibles")

    with gr.Row():
        chatbot_output = gr.Textbox(label="Réponse du chatbot", lines=4)
    
    with gr.Row():
        detected_output = gr.Textbox(label="Composants détectés", lines=2)
    
    with gr.Row():
        verdict_output = gr.Textbox(label="Vérification", lines=2)

    submit_btn = gr.Button("Analyser")
    submit_btn.click(
        fn=full_pipeline,
        inputs=[prompt_input, image_input],
        outputs=[chatbot_output, detected_output, verdict_output]
    )

demo.launch()

