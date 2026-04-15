import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model="google/gemma-4-e2b",
    temperature=0.5,
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm_studio"
)

lista_perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura. Pode sugerir?",
    "Qual a melhor época do ano para ir?"
]

for uma_pergunta in lista_perguntas:
    resposta = modelo.invoke(uma_pergunta)
    print(f"Usuário: {uma_pergunta}")
    print(f"IA: {resposta.content}")
    print("-" * 50)
