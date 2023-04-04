from abc import ABCMeta, abstractmethod

# Assunto/Tópico

class AgenciaNoticias:

    def __init__(self) -> None:
        self.__inscritos = []
        self.__ultima_noticia = None
    
    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)
    
    def desinscrever(self, inscrito=None):
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)
    
    def notificar_todos(self):
        for i in self.__inscritos:
            i.notificar()
    
    def add_noticia(self, noticia):
        self.__ultima_noticia = noticia
    
    def mostrar_noticia(self):
        return f'Urgente: {self.__ultima_noticia}'
    
    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]


# Interface Observer
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass


# observador A
class InscritosSMS(TipoInscricao):

    def __init__(self, agencia_noticia) -> None:
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')

# observador B
class InscritosEmail(TipoInscricao):

    def __init__(self, agencia_noticia) -> None:
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')

# observador C
class InscritosOutros(TipoInscricao):

    def __init__(self, agencia_noticia) -> None:
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}')


if __name__ == '__main__':
    ag = AgenciaNoticias()

    InscritosSMS(ag)
    InscritosEmail(ag)
    InscritosOutros(ag)

    print(f'Inscritos: {ag.inscritos()}')

    ag.add_noticia('Novo curso na Geek University')
    ag.notificar_todos()

    print(f'Descadastrado: {type(ag.desinscrever()).__name__}')
    print(f'Inscritos: {ag.inscritos()}')
    
    ag.add_noticia('Design Patterns ...')
    ag.notificar_todos()