from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "praia"

modelo_de_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagem de {dias} dias, 
    para uma família com {numero_criancas} crianças,
    que gostam de {atividade}
    """
)

prompt = modelo_de_prompt.format(
    dias=numero_dias,
    numero_criancas = numero_criancas,
    atividade=atividade
)

print("Prompt : \n", prompt)

modelo = ChatOpenAI(
    model="google/gemma-3-1b",
    temperature=0.5,
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm_studio"
)

resposta = modelo.invoke(prompt)
print(resposta.content)
