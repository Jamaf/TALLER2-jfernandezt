from models.animal import Animal

class AnimalExotico(Animal):

    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuestos = impuestos
    
    #Metodos    
    def calcular_flete(self) -> float:
        return self.impuestos * self.peso
        
    #Getter y setter
    @property
    def pais_origen(self) -> str:
        """ Devuelve el valor del atributo protegigo 'pais_origen' """
        return self._pais_origen
    
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo protegigo 'pais_origen'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._pais_origen = value
        else:
            raise ValueError('Expected str')
    
    @property
    def impuestos(self) -> float:
        """ Devuelve el valor del atributo protegigo 'impuestos' """
        return self._impuestos
    
    @impuestos.setter
    def impuestos(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo protegigo 'impuestos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise ValueError('Expected float')
        
