from fastapi import FastAPI
import settings
import requests
#https://api.callmebot.com/whatsapp.php?phone=[phone_number]&text=[message]&apikey=[your_apikey]
from application.observer import Assunto, WPP
app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'FastAPI'}


@app.get('/message/{message}')
async def send_message(message:str) -> None:
    
    url = f'https://api.callmebot.com/whatsapp.php?phone={settings.PHONE_NUMBER}&text={message}&apikey={settings.API_KEY}'
    send = requests.get(url)

    return {'message': message, 'status_code': send.status_code, 'k':settings.API_KEY, 'body': send.content}


@app.get('/me/{message}')
async def sender(message:str) -> None:
    ins = Assunto()
    WPP(ins)
    ins.add_noticia(message)
    return {'return': ins.enviar()}



