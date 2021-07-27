#Classes for making the list of objects to be displayed in the result tab

class TableInfo:

    def __init__(self,address_from,coordenates,data=[]):
        self.address_from = address_from
        self.coordenates = coordenates
        self.data = data


class DataTableInfo:
    
    def __init__(self,address_destine,coordenates_destine,distance):
        self.address_destine = address_destine
        self.coordenates_destine = coordenates_destine
        self.distance = distance
        