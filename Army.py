from abc import ABC


class Army(ABC):
    def get_description(self) -> str:
        pass


class OrcArmy(Army):
    
    def __init__(self, description: str) -> None:
        self.__description: str = description

    def get_description(self) -> str:
        return self.__description

    
class ElfArmy(Army):
    
    def __init__(self, description: str) -> None:
        self.__description: str = description
        
    def get_description(self) -> str:
        return self.__description
