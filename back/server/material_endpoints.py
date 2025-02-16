from flask import request, Blueprint
from back.controllers import material_controller

material_blueprint = Blueprint("material", __name__)

@material_blueprint.route("/get_material_info", methods=["GET"])
def get_material_info():

    part_number = request.args.get('material_part_number')
    return material_controller.get_material_by_part_number(part_number)

@material_blueprint.route("/get_all_materials", methods = ["GET"])
def get_all_materials():
    return material_controller.get_all_materials() 