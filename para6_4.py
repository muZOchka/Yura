class BuildingError(Exception):
    def __str__(self):
        return f"Whith so much material the house cannot build!"

def check_material(amount_of_material, limit_material):
    if amount_of_material > limit_material:
        return "enough material"
    else:
        raise BufferError

material = 323
check_material(material, 300)