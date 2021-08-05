from King import *
from Castle import *
from Army import *


class KingdomFactory(ABC):
    def create_king(self) -> King:
        pass

    def create_army(self) -> Army:
        pass

    def create_castle(self) -> Castle:
        pass


class OrcKingdomFactory(KingdomFactory):
    def __init__(self)-> None: 
        pass
    
    def create_army(self) -> Army:
        descripcion = input("Nombre de la armada? ")
        armada = OrcArmy(descripcion)
        return armada
    
    def create_castle(self) -> Castle:
        descripcion = input("Nombre del castillo? ")
        castillo = OrcCastle(descripcion)
        return castillo
    
    def create_king(self) -> King:
        descripcion = input("Nombre del rey? ")
        rey = OrcKing(descripcion)
        return rey
    
    
class ElfKingdomFactory(KingdomFactory):
    def __init__(self)-> None:
        pass
    
    def create_army(self) -> Army:
        descripcion = input("Nombre de la armada? ")
        armada = ElfArmy(descripcion)
        return armada
    
    def create_castle(self) -> Castle:
        descripcion = input("Nombre del castillo? ")
        castillo = ElfCastle(descripcion)
        return castillo
    
    def create_king(self) -> King:
        descripcion = input("Nombre del rey? ")
        rey = ElfKing(descripcion)
        return rey


    
    
