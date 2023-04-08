from flask import Flask
import settings
import requests
from application.observer import Assunto, WPP
from application.facade import ClientWeather

app = Flask(__name__)


@app.get('/')
def root():
    return {'message': 'FastAPI'}


@app.get('/message/{message}')
def send_message(message:str) -> None:
    
    url = f'https://api.callmebot.com/whatsapp.php?phone={settings.PHONE_NUMBER}&text={message}&apikey={settings.API_KEY}'
    send = requests.get(url)

    return {'message': message, 'status_code': send.status_code, 'k':settings.API_KEY, 'body': send.content}


@app.get('/me/{message}')
def sender(message:str) -> None:
    ins = Assunto()
    WPP(ins)
    ins.add_noticia(message)
    return {'return': ins.enviar()}


@app.get('/clima/')
def clima() -> None:
    cw = ClientWeather()
    res = cw.obter_clima()
    
    ins = Assunto()
    WPP(ins)
    ins.add_noticia(res)
    ins.enviar()
    
    return res

