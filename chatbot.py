from dotenv import load_dotenv
import os
from openai import OpenAI
from src.prompts import get_prompt

load_dotenv()
client = OpenAI()

def gera_copy(prompt_usuario):
    prompt_completo = get_prompt()
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_completo},
            {"role": "user", "content": prompt_usuario}
        ]
    )
    
    return completion.choices[0].message.content

while True:
    entrada_usuario = input("Digite sua solicitação de copy ou 'sair' para encerrar: ")
    if entrada_usuario.lower() == 'sair':
        print("Encerrando o chatbot de copywriting. Até mais!")
        break
    
    resposta_copy = gera_copy(entrada_usuario)
    print("Resposta do Chatbot:\n", resposta_copy)
