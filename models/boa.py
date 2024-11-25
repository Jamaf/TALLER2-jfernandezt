from models.animalexotico import AnimalExotico

class Boa(AnimalExotico):

    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self)->str:
        return '¡Tsss!.'
    
    def agregar_raton(self, ratones:int)->None:
        self.ratones_comidos += ratones

    @property
    def ratones_comidos(self) -> int:
        """ Devuelve el valor del atributo privado 'ratones_comidos' """
        return self.__ratones_comidos
    
    @ratones_comidos.setter
    def ratones_comidos(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ratones_comidos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            if value > 20: #La guardería ha decretado que el límite de ratones para la boa ahora será de 20.
                raise ValueError('Demasiados Ratones!')
            self.__ratones_comidos = value
        else:
            raise ValueError('Expected int')
        
