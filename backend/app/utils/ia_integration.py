from transformers import pipeline

# Inicializa el pipeline de generación de texto (modelo ligero para pruebas)
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

def generate_syllabus(prompt: str) -> str:
    result = generator(prompt, max_length=500, do_sample=True)
    return result[0]['generated_text']
