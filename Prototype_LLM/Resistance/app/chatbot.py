import re
from collections import Counter
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

MODEL_PATH = "C:\\Users\\faury\\Downloads\\Prototype_LLM\\Resistance\\llama_tiny_final"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto"
)

def get_required_components(prompt: str):
    """
    Utilise LLaMA local pour générer la description des composants nécessaires.
    Retourne la réponse textuelle et une liste normalisée de composants.
    """
    try:
        response = generator(
            prompt,
            max_length=200,
            temperature=0.7,
            num_return_sequences=1,
            do_sample=True
        )[0]["generated_text"]

        # Nettoyage (supprimer le prompt répété si nécessaire)
        if response.lower().startswith(prompt.lower()):
            response = response[len(prompt):].strip()

        # Détection des composants avec regex (pluriels et variantes incluses)
        keywords = {
            "résistance": r"résistances?",
            "condensateur": r"condensateurs?",
            "inductance": r"inductances?",
            "bobine": r"bobines?"
        }

        components = []
        for comp, pattern in keywords.items():
            matches = re.findall(pattern, response.lower())
            if matches:
                components.extend([comp] * len(matches))

        return response.strip(), components if components else ["inconnu"]

    except Exception as e:
        return f"Erreur pendant la génération : {e}", []
