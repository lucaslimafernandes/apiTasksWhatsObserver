from fastapi import FastAPI, Header
from typing import Union, List
from typing_extensions import Annotated
import settings
import requests
from application.observer import Assunto, WPP
from application.facade import ClientWeather
from hashlib import sha256

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'FastAPI'}


@app.get('/me/{message}')
async def sender(message:str) -> None:
    ins = Assunto()
    WPP(ins)
    ins.add_noticia(message)
    return {'return': ins.enviar()}


@app.get('/clima/')
async def clima(x_token: Annotated[Union[List[str], None], Header()] = None) -> None:
    try:
        if settings.TK == sha256({'X-Token values': x_token[0]}['X-Token values'].encode()).hexdigest():
        
            cw = ClientWeather()
            res = cw.obter_clima()

            formatt = f'''Cidade: {res['cidade']}\nNuvens: {res['clouds']}\nTemperatura: {res['main']['temp']}\n\tSensação Térmica: {res['main']['feels_like']}\n\tMínima: {res['main']['temp_min']}\n\tMáxima: {res['main']['temp_max']}\n\tHumidade: {res['main']['humidity']}\nVento: {res['wind']}'''
            
            ins = Assunto()
            WPP(ins)
            ins.add_noticia(formatt)
            ins.enviar()
        
            return res
    except:
        return {'Error': 'Please, contact admnistrator!'}


@app.get('/teste/')
async def teste(x_token: Annotated[Union[List[str], None], Header()] = None):
    
    a = {"X-Token values": x_token[0]}
    
    return a['X-Token values']
