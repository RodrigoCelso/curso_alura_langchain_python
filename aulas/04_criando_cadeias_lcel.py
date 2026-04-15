from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os 


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    """,
    input_variables=["interesse"]
)

modelo = ChatOpenAI(
    model="google/gemma-3-1b",
    temperature=0.5,
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm_studio"
)

cadeia = prompt_cidade | modelo | StrOutputParser()

resposta = cadeia.invoke(
    {
        "interesse" : "praias"
    }
)

print(resposta)
