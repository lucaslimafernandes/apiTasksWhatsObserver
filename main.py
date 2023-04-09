from fastapi import FastAPI
import settings
import requests
from application.observer import Assunto, WPP
from application.facade import ClientWeather

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


@app.get('/clima/')
async def clima() -> None:
    cw = ClientWeather()
    res = cw.obter_clima()

    formatt = f'''Cidade: {res['cidade']}\nNuvens: {res['clouds']}\nTemperatura: {res['main']['temp']}\n\tSensação Térmica: {res['main']['feels_like']}\n\tMínima: {res['main']['temp_min']}\n\tMáxima: {res['main']['temp_max']}\n\tHumidade: {res['main']['humidity']}\nVento: {res['wind']}'''
    
    ins = Assunto()
    WPP(ins)
    ins.add_noticia(formatt)
    ins.enviar()
    
    return res

