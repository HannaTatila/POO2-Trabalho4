from abc import abstractmethod, ABCMeta

__author__ = 'dell'

class EstadoMenu:
    __metaclass__ = ABCMeta

    @abstractmethod
    def proximo_valor(self):
        pass

    @abstractmethod
    def valor_anterior(self):
        pass

    @abstractmethod
    def selecionar_valor(self):
        pass




