import requests
import settings
from abc import ABC, abstractmethod

#https://api.callmebot.com/whatsapp.php?phone=[phone_number]&text=[message]&apikey=[your_apikey]



#assunto
class Assunto:
    
    def __init__(self) -> None:
        self.message = []
        self.meios = []
    
    def inscrever(self, inscrito):
        self.meios.append(inscrito)
    
    def add_noticia(self, mess):
        self.message.append(mess)

    def messager(self):
        url = f'''https://api.callmebot.com/whatsapp.php?phone={settings.PHONE_NUMBER}&text={self.message}&apikey={settings.API_KEY}'''
        send = requests.get(url)
        return {'message': self.message, 'status_code': send.status_code, 'body': send.content}
    
    def enviar(self):
        for i in self.meios:
            i.sender()


# Interface
class Interface(ABC):

    @abstractmethod
    def sender(self):
        pass



#Observer
class WPP(Interface):

    def __init__(self, assunto) -> None:
        self.assunto = assunto
        self.assunto.inscrever(self)
    
    def sender(self):
        return (self.assunto.messager())




if __name__ == '__main__':
    ins = Assunto()

    WPP(ins)
    ins.add_noticia('Teste')
    ins.enviar()
