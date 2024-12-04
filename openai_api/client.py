import openai

def get_car_ai_bio(model, brand, year):
    prompt = f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo."


    from dotenv import load_dotenv 
    import os

    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000 
    )
    
    return response['choices'][0]['message']['content']