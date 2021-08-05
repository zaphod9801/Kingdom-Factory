from KingdomFactory import *
from enum import Enum
from typing import List
import logging
import Army
import Castle
import King
from Army import *
from Castle import *
from King import *

logger = logging.getLogger('debug_Log')
logger.setLevel(logging.DEBUG)

class KingdomType(Enum):
    ELF = 1
    ORC = 2

    @classmethod
    def value_of(cls, name: str) -> "KingdomType":
        return cls.__getattr__(name)

    @classmethod
    def values(cls) -> List["KingdomType"]:
        return list(cls)

    
class FactoryMaker:
    
    def __init__(self) -> None:
        pass

    def makeFactory(self,  tipo: KingdomType) -> KingdomFactory:
        if tipo == KingdomType.ORC:
            return OrcKingdomFactory()
        elif tipo == KingdomType.ELF:
            return ElfKingdomFactory()
        else:
            raise ValueError("Whatever")
        

class App():
    
    def __init__(self) -> None:
        self.fh = logging.FileHandler('debug.log')
        self.fh.setLevel(logging.DEBUG)
        self.armada: Army
        self.rey: King
        self.castillo: Castle
        self.createKingdom()
        
    def createKingdom(self) -> None:
        reino = FactoryMaker()
        tipo = input("Reino de elfos: ELF  \n Reino de orcos: ORC \n")
        if (tipo == "ELF"):
            r = reino.makeFactory(KingdomType.ELF)
            logger.info('Reino de elfos creado')
            r.create_army()
            r.create_castle()
            r.create_king()
        elif (tipo == "ORC"):
            r = reino.makeFactory(KingdomType.ORC)
            logger.info('Reino de orcos creado')
            r.create_army()
            r.create_castle()
            r.create_king()
        else:
            print("Tipo de reino no valido")
    
    def getArmy(self) -> str:
        return self.armada.get_description()
    
    def getCastle(self) -> str:
        return self.castillo.get_description()
                     
    def getKing(self) -> str:
        return self.rey.get_description()
        
    def setArmy(self, armada: Army) -> None:
        self.armada = armada
        
    def setCastle(self, castillo: Army) -> None:
        self.castillo = castillo
        
    def setKing(self, rey: King) -> None:
        self.rey = rey
        
    def getArmy2(self, fabrica: KingdomFactory) -> Army:
        return fabrica.create_army()
    
    def getCastle2(self, fabrica: KingdomFactory) -> Castle:
        return fabrica.create_castle()
    
    def getKing2(self, fabrica: KingdomFactory) -> King:
        return fabrica.create_king()
    
if __name__=="__main__":
    print("***Creación de reino inicial***")
    game = App() #intenta crear un reino inicial
    print("")
    print("***Creación de reino de prueba para getters y setters***")
    ar = OrcArmy("la armada del bicho") # para el ejemplo de la implementación de lo setters y getters
    ca = ElfCastle("el castillo del bicho")
    re = OrcKing("el bicho")
    game.setArmy(ar)
    game.setCastle(ca)
    game.setKing(re)
    print(game.getArmy())
    print(game.getCastle())
    print(game.getKing())
    print("")
    #ejemplo de los getters usando una fabrica de argumento
    print("***Creación del reino de prueba para los getters con una fabrica de argumento***")
    fabrica = FactoryMaker()
    f = fabrica.makeFactory(KingdomType.ORC)
    print(game.getArmy2(f))
    print(game.getCastle2(f))
    print(game.getKing2(f))