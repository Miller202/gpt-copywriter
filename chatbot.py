from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
from src.prompts import get_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gera_copy', methods=['POST'])
def gera_copy():
    data = request.json
    prompt_usuario = data['mensagem']

    prompt_completo = get_prompt()
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_completo},
            {"role": "user", "content": prompt_usuario}
        ]
    )
    
    return jsonify({"resposta": completion.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)
