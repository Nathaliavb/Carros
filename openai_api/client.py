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