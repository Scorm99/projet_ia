# app/verifier.py
def check_components(required, detected):
    missing = [c for c in required if c not in detected]
    if missing:
        return f"❌ Il manque : {', '.join(missing)}"
    return "✅ Tous les composants nécessaires sont présents."
