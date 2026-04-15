from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 4
numero_criancas = 2
atividade = "música"

prompt = f"Crie um roteiro de viagem de {numero_dias}, para uma família com {numero_criancas} crianças, que gosta de {atividade}"

cliente = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
    )

resposta = cliente.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente de roteiro de viagens."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(resposta.choices[0].message.content)
