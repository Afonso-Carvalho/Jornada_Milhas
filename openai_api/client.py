import openai
import os

def get_destino_ai_texto(model):
    prompt = '''
    Faça um resumo sobre {} enfatizando o porque este lugar é incrível. Utilize uma linguagem informal e até 100 caracteres no máximo em cada parágrafo. Crie 2 parágrafos neste resumo.
    '''
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = prompt.format(model)
    response = openai.Completion.create(
        model= 'text-davinci-003',
        prompt = prompt,
        max_tokens=1000
    )
    return response['choices'][0]['text']