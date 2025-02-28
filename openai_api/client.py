
import openai
from pathlib import Path
import os
import environ


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


openai.api_key = env('OPENAI_API_KEY')

def get_car_ai_bio(model, brand, year):
    prompt = f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo."
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000 
    )
    
    return response['choices'][0]['message']['content']