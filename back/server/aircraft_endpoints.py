import logging
from flask import request, Blueprint
from back.controllers import aircraft_controller

aircraft_blueprint = Blueprint("aircraft", __name__)

@aircraft_blueprint.route("/get_aircraft_info", methods=["GET"])
def get_aircraft_info():
    serial_number = request.args.get('serial_number')
    logging.info(f"/get_aircfraft_info was called for {serial_number}")
    return aircraft_controller.get_aircraft_by_serial_number(serial_number)

@aircraft_blueprint.route("/get_all_aircrafts", methods=["GET"])
def get_all_aicrafts():
    logging.info(f"/get_all_aircrafts was called") 
    return aircraft_controller.get_all_aircrafts()
