from models.huron import Huron
from models.boa import Boa
from models.perro import Perro
from models.gato import Gato

class Guarderia:
    # def __init__(self, boa1:Boa, huron1:Huron, perro:Perro, gato:Gato):
    #     self.boa = boa1
    #     self.huron = huron1
    #     self.perro = perro
    #     self.gato = gato

    boa  = Boa('Boby', 10.0, 6, 'Colombia', 16.5)          
    huron = Huron('Buck', 3.5, 4, 'Brazil', 20.0)     
    perro = Perro('Doggy', 4.0, 8)     
    gato = Gato('Doggy', 4.0, 8)     

    @staticmethod
    def obtener_sonido(animal):
        sonido = None
        aux_animal = None

        if animal in ['Boa', 'Huron', 'Perro', 'Gato']:
            if animal == 'Boa':
                aux_animal = Guarderia.boa
            elif animal == 'Huron':
                aux_animal = Guarderia.huron
            elif animal == 'Perro':
                aux_animal = Guarderia.perro
            else:
                aux_animal = Guarderia.gato

            return aux_animal.hacer_sonido()
        else:
            raise ValueError('animal no encontrado')
