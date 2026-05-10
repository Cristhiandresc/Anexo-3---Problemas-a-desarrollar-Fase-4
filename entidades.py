from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id_entidad):
        self._id = id_entidad
    
    @abstractmethod
    def mostrar_info(self):
        pass