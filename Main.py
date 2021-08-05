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
        logger.addHandler(self.fh)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        logger.addHandler(self.fh)
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
            logger.info('Armada de elfos creada')
            r.create_castle()
            logger.info('Castillo de elfos creado')
            r.create_king()
            logger.info('Rey de elfos creado')
        elif (tipo == "ORC"):
            r = reino.makeFactory(KingdomType.ORC)
            logger.info('Reino de orcos creado')
            r.create_army()
            logger.info('Armada de orcos creada')
            r.create_castle()
            logger.info('Castillo de orcos creado')
            r.create_king()
            logger.info('Rey de orcos creado')
        else:
            print("Tipo de reino no valido")
            logger.warning('Tipo de reino invalido')
    
    def getArmy(self) -> str:
        logger.info('Armada principal de la aplicacion solicitada')
        return self.armada.get_description()
    
    def getCastle(self) -> str:
        logger.info('Castillo principal de la aplicacion solicitado')
        return self.castillo.get_description()
                     
    def getKing(self) -> str:
        logger.info('Rey principal de la aplicacion solicitado')
        return self.rey.get_description()
        
    def setArmy(self, armada: Army) -> None:
        logger.info('Armada principal de la aplicacion creada')
        self.armada = armada
        
    def setCastle(self, castillo: Army) -> None:
        logger.info('Castillo principal de la aplicacion creado')
        self.castillo = castillo
        
    def setKing(self, rey: King) -> None:
        logger.info('Rey principal de la aplicacion creado')
        self.rey = rey
        
    def getArmy2(self, fabrica: KingdomFactory) -> Army:
        logger.info('Armada con tipo de fabrica solicitado')
        return fabrica.create_army()
    
    def getCastle2(self, fabrica: KingdomFactory) -> Castle:
        logger.info('Castillo con tipo de fabrica solicitado')
        return fabrica.create_castle()
    
    def getKing2(self, fabrica: KingdomFactory) -> King:
        logger.info('Rey con tipo de fabrica solicitado')
        return fabrica.create_king()
    
if __name__=="__main__":
    print("***Creación de reino inicial***")
    game = App() #intenta crear un reino inicial
    logger.info('Reino inicial creado')
    print("")
    print("***Creación de reino de prueba para getters y setters***")
    ar = OrcArmy("la armada del bicho") # para el ejemplo de la implementación de lo setters y getters
    ca = ElfCastle("el castillo del bicho")
    re = OrcKing("el bicho")
    game.setArmy(ar)
    game.setCastle(ca)
    game.setKing(re)
    logger.info('Reino principal de la aplicación creado')
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