import requests
import settings
import json
from typing import Dict


# Fachada
class Facade:

    def __init__(self) -> None:
        pass
    
    
    def clima(self):
        ow = OpenWeather()
        res = ow.clima().decode()
        return self.create_dict(json.loads(res))
    

    def create_dict(self, dados) -> Dict:

        response = {
            'cidade': dados['name'],
            'clouds': dados['weather'][0]['description'],
            'main': dados['main'],
            'wind': dados['wind']['speed']
        }
        return response 


# sub sistema
class OpenWeather:

    def __init__(self) -> None:

        self.lat = settings.LAT_LONG['local'][0]
        self.lon = settings.LAT_LONG['local'][1]
        self.api_key = settings.OPEN_WEATHER

        url_weahter = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}&lang=pt_br&units=metric'
        self.__res = requests.get(url_weahter).content

    def clima(self) -> None:
        return self.__res

    def __repr__(self) -> str:
        return 'Dados Open Weather'

class ClientWeather:

    def __init__(self) -> None:
        pass

    def obter_clima(self):
        ow = Facade()
        return ow.clima()