from typing import List
from back.material import repository
from back.utils.utils import json_response
from back.material.schema import MaterialSchema

class MaterialController:
    def __init__(self, db, window = None):
        self.db = db
        self.window = window
    
    @json_response(List[MaterialSchema])
    def get_all_materials(self):
        materials = repository.get_all_materials(self.db)
        
        return materials

    @json_response(MaterialSchema)
    def get_material_by_part_number(self, part_number: str):
        material = repository.get_material_by_part_number(self.db, part_number)
        return material

    def add_materials_from_file(self, file):
        try:
            return repository.create_new_materials(self.db, file)
        except Exception as e:
            return {"success": False, "error": f"Error during file processing: {str(e)}"}


