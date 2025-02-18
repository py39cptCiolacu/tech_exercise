from typing import List
from back.aircraft import repository
from back.utils.utils import json_response
from back.aircraft.schema import AircraftSchema

class AircraftController:
    def __init__(self, db, window = None):
        self.db = db
        self.window = window
    
    @json_response(List[AircraftSchema])
    def get_all_aircrafts(self):
        aircrafts = repository.get_all_aircrafs(self.db)

        return aircrafts
    
    @json_response(AircraftSchema)
    def get_aircraft_by_serial_number(self, serial_number: str):
        aircraft = repository.get_aircraft_by_serial_number(self.db, serial_number)
        return aircraft

    def add_aircrafts_from_file(self, file):
        try:
            return repository.create_new_aircrafts(self.db, file) 
        except Exception as e:
            return {"success": False, "error": f"Error during file processing: {str(e)}"}

