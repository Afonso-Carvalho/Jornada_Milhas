<h1 align="center"> Jornada Milhas API </h1>

![Badge Concluído](https://img.shields.io/static/v1?label=Status&message=Concluído&color=success&style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)

## :book: Resumo do projeto
A Jornada Milhas API é uma REST API desenvolvida para uma plataforma que disponibiliza roteiros de viagem para seus clientes, contendo diversos destinos emocionantes.

A aplicação possui endpoints para acessar informações sobre os destinos, depoimentos de outros viajantes, integração com o chat GPT para criar automaticamente textos descritivos para os destinos, além de métodos de login para autenticação dos usuários.

Este projeto foi proposto pela Alura no Challenge Backend 7ª Edição.

## :toolbox: Tecnologias e ferramentas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## :bulb: Funcionalidades

### :lock: API de gerenciamento de Autenticação
- `Login de usuário`: O login deve ser realizado através de um POST com as credenciais do usuário (email e password).

### :airplane: API de gerenciamento de destinos
- `Destino`: Possui as seguintes informações sendo elas de foto do local, *nome*, *preço*, *meta* e o *texto descritivo* sobre o local.
  - O `texto descritivo` possui uma funcionalidade interessante: caso o criador do post opte por não escrever uma descrição sobre o local, essa tarefa será realizada automaticamente pelo Chat GPT. Essa integração com a IA garante que mesmo que o criador não forneça uma descrição manualmente, os destinos ainda serão apresentados com textos atraentes e envolventes para os usuários.<br>

- `Cadastrar`: Salvar um destino através de um POST com as informações de *nome*, *preço*, *meta* e o *texto descritivo* sobre o local.</br>
  - É necessário estar autenticado.<br>

- `Atualizar`: Atualizar o destino utilizando o metodo PUT *destinos/ID* onde *ID* é o identificador.
  - É necessário estar autenticado.<br>

- `Buscar por id`: Busca destinos por ID através de um GET *destinos/ID* , onde *{ID}* é o identificador.
  - É necessário estar autenticado.<br>

- `Buscar todos`: Busca paginada de destino através de um GET *destinos/*.
  - É necessário estar autenticado.<br>

- `Deletar`: Deletar destinos através de um DELETE *destinos/ID*, onde *{ID}* é o identificador do destino.</br>
  - É necessário estar autenticado.<br>

### :mailbox: API de depoimentos
- `Depoimentos`: Possui as seguintes informações *foto*, *nome*, *depoimento*.
  - Além disso, oferecemos como um "plus" um endpoint muito semelhante chamado "depoimentos-home", que permite que o frontend acesse aleatoriamente *3* depoimentos de clientes. Essa funcionalidade adicional torna a experiência do usuário ainda mais interessante, apresentando depoimentos variados de forma dinâmica a cada visita à página inicial.

- `Cadastrar`: Salvar um depoimento através de um POST com as informações de *foto*, *nome* e *depoimento* </br>
  - É necessário estar autenticado.<br>

- `Atualizar`: Atualizar o depoimento utilizando o metodo PUT *depoimentos/ID* onde *ID* é o identificador.
  - É necessário estar autenticado.<br>

- `Buscar por id`: Busca depoimento por ID através de um GET *depoimentos/ID* , onde *{ID}* é o identificador.
  - É necessário estar autenticado.<br>

- `Buscar todos`: Busca paginada de depoimento através de um GET *depoimentos/*.
  - É necessário estar autenticado.<br>

- `Deletar`: Deletar depoimento através de um DELETE *depoimentos/ID*, onde *{ID}* é o identificador do destino.</br>
  - É necessário estar autenticado.<br>

## :computer: Como executar a aplicação?

Clone o projeto:
  ```bash
  git clone https://github.com/Afonso-Carvalho/Jornada_Milhas.git
  ```

Execute o comando:
```bash
python manage.py runserver
  ```

O comando ira executar a API, lembrando de adicionar suas `secrets_key` pessoais do django no [settings.py](https://github.com/Afonso-Carvalho/Jornada_Milhas/blob/master/setup/settings.py), e a `secrets_key` da OpenAI no [Client.py](https://github.com/Afonso-Carvalho/Jornada_Milhas/blob/master/openai_api/client.py).
  
