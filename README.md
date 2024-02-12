# GPT Copywriter Chatbot

Chatbot para atuar como assistente de copywriting, como foco em textos persuasivos para vendas. O chatbot utiliza a API da OpenAI para gerar respostas baseadas nas solicitações do usuário.

## Configuração do Ambiente

Antes de iniciar, certifique-se de que você tem Python e Poetry instalados em seu sistema. Você pode instalar Poetry seguindo as instruções na [documentação oficial do Poetry](https://python-poetry.org/docs/#installation).

### Instalação das Dependências

1. Clone o repositório para a sua máquina local:
2. Instale as dependências do projeto: 
```poetry install```

### Configuração das Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione a sua chave da API da OpenAI ao arquivo `.env`:
```OPENAI_API_KEY=sua_chave_api_aqui```

## Executando o Projeto

Para rodar o servidor Flask localmente, execute o seguinte comando na raiz do projeto:
```poetry run python chatbot.py```

## Estrutura do Projeto

- `chatbot.py`: Arquivo principal do servidor Flask.
- `templates/`: Pasta contendo os arquivos HTML para a interface do usuário.
- `static/`: Pasta contendo arquivos estáticos, como CSS e imagens.
- `.env`: Arquivo contendo variáveis de ambiente, como a chave da API da OpenAI.