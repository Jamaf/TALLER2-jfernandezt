from models.ianimal import IAnimal
from abc import abstractmethod

class Animal(IAnimal):
    def __init__(self, nombre:str, peso:float, edad:int):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.kilos_comidos = 0.0
    
    #Metodos
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    def comer(self, kilos) -> None:
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        return self.kilos_comidos 
    
    #Getter y setter
    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo protegigo 'nombre' """
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo protegigo 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
    
    @property
    def peso(self) -> float:
        """ Devuelve el valor del atributo protegigo 'peso' """
        return self._peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo protegigo 'peso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')
        
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo protegigo 'edad' """
        return self._edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo protegigo 'edad'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')
    
    @property
    def kilos_comidos(self) -> float:
        """ Devuelve el valor del atributo protegigo 'kilos_comidos' """
        return self._kilos_comidos
    
    @kilos_comidos.setter
    def kilos_comidos(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo protegigo 'kilos_comidos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._kilos_comidos = value
        else:
            raise ValueError('Expected float')
        

