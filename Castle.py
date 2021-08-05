from abc import ABC


class Castle(ABC):
    def get_description(self) -> str:
        pass


class OrcCastle(Castle):
    
    def __init__(self, descripcion)-> None:
        self.__description = descripcion
        
    def get_description(self) -> str:
        return self.__description


class ElfCastle(Castle):
    
    def __init__(self, descripcion)-> None:
        self.__description = descripcion
        
    def get_description(self) -> str:
        return self.__description

