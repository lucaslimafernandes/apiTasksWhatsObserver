import settings
from application import cron_service
from fastapi import FastAPI, Header
from typing import Union, List
from typing_extensions import Annotated
from application.observer import Assunto, WPP
from application.facade import ClientWeather
from hashlib import sha256

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'FastAPI'}


@app.get('/me/{message}')
async def sender(message:str) -> dict:
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


@app.get('/alarmes/')
async def alarmes():

    res = cron_service.show_alarmes()
    #res = 'aaa'
    return res


@app.get('/alarmes/new/')
async def alarmes_new(nome:str='alarme', message:str='Alarme',
                    minute:int=999, hour:int=999, day:int=999,
                    month:int=999, day_week:int=999, unique_execute:bool=False):
    
    item = {
        'nome'      : nome,
        'message'   : message,
        'c_minute'  : minute,
        'c_hour'    : hour,
        'c_day'     : day,
        'c_month'   : month,
        'c_day_week': day_week,
        'unique_execute': unique_execute
    }

    res = cron_service.new_alarm(item)
    return f'Item inserido - id: {res}'
    
@app.get('/alarmes/delete/{item_id}')
async def alarmes_delete(item_id:int):

    res = cron_service.delete_alarm(item_id)

    return res



@app.get('/teste/')
async def teste(x_token: Annotated[Union[List[str], None], Header()] = None):

    a = {"X-Token values": x_token[0]}
    return a['X-Token values']
