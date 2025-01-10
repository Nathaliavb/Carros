import openai

def get_car_ai_bio(model, brand, year):
    prompt = f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo."
    
    openai.api_key = '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'  
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000 
    )
    
    return response['choices'][0]['message']['content']