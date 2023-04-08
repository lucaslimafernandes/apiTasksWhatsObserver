import requests
import settings
import json

#lat = settings.LAT_LONG['casa'][0]
#lon = settings.LAT_LONG['casa'][1]

#url_weahter = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={settings.OPEN_WEATHER}&lang=pt_br'
#url_weahter = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPEN_WEATHER}&lang=pt_br'


#res = requests.get(url_weahter)

#print(res.content)


# Fachada
class Facade:

    def __init__(self) -> None:
        pass
    
    def clima(self):
        ow = OpenWeather()
        res = ow.clima().decode()
        print(res)
        print(type(res))
        print(json.loads(res))
        print(type(json.loads(res)))   
        return json.loads(res)
        


# sub sistema
class OpenWeather:

    def __init__(self) -> None:

        self.lat = settings.LAT_LONG['casa'][0]
        self.lon = settings.LAT_LONG['casa'][1]
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