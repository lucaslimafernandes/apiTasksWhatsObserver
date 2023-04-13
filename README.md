# apiTasksWhatsObserver

author: Lucas Lima Fernandes
e-mail: lucas.lfernandes@live.com

## Sobre o Projeto

Estudo de uso do design pattern Observer e Façade

ao realizar a chamada ao endpoint /clima/ recebo a seguinte resposta no whatsapp: 

    [Cidade: Qualquer
    Nuvens: chuva moderada
    Temperatura: 22.49
    Sensação Térmica: 23.77
    Mínima: 21.18
    Máxima: 23.05
    Humidade: 87
    Vento: 3.6]

## Settings

renomear o arquivo settings_model.py para settings.py

Seguir os passos encontrados em: https://www.callmebot.com/blog/free-api-whatsapp-messages/

Que são:

    1. Adicionar o número aos contatos: +34 644 44 21 48

    2. Envia a seguinte mensagem ao número: I allow callmebot to send me messages

Salvar a apikey recebida na constante API_KEY no arquivo settings.py

Salvar seu número de telefone na constante PHONE_NUMBER no arquivo settings.py

Criar conta no https://openweathermap.org/api e na aba api keys pegar a chave e salvar na constante OPEN_WEATHER no arquivo settings.py

Na constante LAT_LONG = {'local': [0, 0]} substituir os zeros pela latitude e longitude respectivamente do local desejado.

por fim, para adicionar uma segurança a mais, salve um hash SHA256 de uma senha de sua escolha na constante TK do arquivo settings.py

para gerar está hash, basta executar o arquivo criar_tk.py

Tomar cuidado com os caminhos das pastas 


## Setting up local (Linux)

    sudo apt update

    sudo apt install -y python3-pip

    sudo apt install -y python3-venv

    git clone https://github.com/lucaslimafernandes/apiTasksWhatsObserver.git

    cd apiTasksWhatsObserver

    python

    python3 -m venv ambiente

    source ambiente/bin/activate

    python -m pip install --upgrade pip

    pip install -r requirements


## Run
Para testes ou execução local:

> uvicorn main:app --reload

Para deploy:

> nohup uvicorn main:app --host 0.0.0.0 --port 5000

ou via service (apiTasksWhats.service)


## Execução

Acessar o navegador com o endereço ip fornecido pelo uvicorn (provavelmente: http://127.0.0.1:8000)

e navegar pelas rotas 

    - /me/ -> qualquer texto após a / para enviar uma mensagem para o whats

    - /clima/ -> para enviar os dados de clima, só funcionará passando via header a sua senha gerada

    uma forma fácil de passar é usando curl:

    curl http://127.0.0.1:8000/clima/ -H 'X-Token: SUA_SENHA_AQUI'

    ou via alguma plataforma de desenvolvimento de API - Recomento Insomnia ou Postman

também existem opções para Android, basta buscar por API Tester. 


## Setting up VPS

Para rodar o projeto em algum servidor linux

seguir os passos em install.sh ou tentar executar no bash

referências:

https://fastapi.tiangolo.com/deployment/manually/

https://docs.oracle.com/en-us/iaas/developer-tutorials/tutorials/flask-on-ubuntu/01oci-ubuntu-flask-summary.htm


## Próximos passos do projeto

- Kubernetes

- Adicionar outras rotas para outros serviços

