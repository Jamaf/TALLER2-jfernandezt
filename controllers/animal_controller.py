from models.guarderia import Guarderia

from flask import jsonify
from flask import Blueprint

animal_blueprint = Blueprint('animal_bp', __name__, url_prefix="/animales")

@animal_blueprint.route('/hacer_sonido/<string:nombre_animal>/') 
def hacer_sonido( nombre_animal:str ):
    codigo_rpta = 200
    try:
        sonido = Guarderia.obtener_sonido(nombre_animal) 
        rpta = {
            'animal': nombre_animal
            ,'sonido': sonido
        }  
    except ValueError as exc:
        rpta = {
            'animal': nombre_animal
            ,'error_msg': str(exc)
        } 
        codigo_rpta = 404
    
    return jsonify(rpta), codigo_rpta