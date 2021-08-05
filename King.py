from abc import ABC


class King(ABC):
    def get_description(self) -> str:
        pass


class OrcKing(King):
    
    def __init__(self, descripcion) -> None:
        self.__description = descripcion
        
    def get_description(self) -> str:
        return self.__description


class ElfKing(King):
    
    def __init__(self, descripcion) -> None:
        self.__description = descripcion
        
    def get_description(self) -> str:
        return self.__description
    
