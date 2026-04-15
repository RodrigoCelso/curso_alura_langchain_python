from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 4
numero_criancas = 2
atividade = "cachoeira"

prompt = f"Crie um roteiro de viagens, para um período de {numero_dias}, para uma família com {numero_criancas} que busca atividades relacionadas a {atividade}"

modelo = ChatOpenAI(
    model="google/gemma-3-1b",
    temperature=0.5,
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm_studio"
)

resposta = modelo.invoke(prompt)

print(resposta.content)
