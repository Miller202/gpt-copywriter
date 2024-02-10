from dotenv import load_dotenv
import os
import openai
from prompts import get_prompt

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def gera_copy(prompt_usuario):
    prompt_completo = get_prompt(prompt_usuario)
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_completo,
        temperature=0.7,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return response.choices[0].text.strip()

while True:
    entrada_usuario = input("Digite sua solicitação de copy ou 'sair' para encerrar: ")
    if entrada_usuario.lower() == 'sair':
        print("Encerrando o chatbot de copywriting. Até mais!")
        break
    
    resposta_copy = gera_copy(entrada_usuario)
    print("Resposta do Chatbot:\n", resposta_copy)
