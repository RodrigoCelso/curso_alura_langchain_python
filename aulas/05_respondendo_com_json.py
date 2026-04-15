from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain.globals import set_debug
import os 


set_debug(True)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Destino(BaseModel):
    cidade:str = Field(description="A cidade sugerida para visitar")
    motivo:str = Field(description="motivo pelo qual é interessante visitar essa cidade")

parseador = JsonOutputParser(pydantic_object=Destino)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()}
)

modelo = ChatOpenAI(
    model="google/gemma-4-e2b",
    temperature=0.5,
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm_studio"
)

cadeia = prompt_cidade | modelo | parseador

resposta = cadeia.invoke(
    {
        "interesse" : "praias"
    }
)

print(resposta)
