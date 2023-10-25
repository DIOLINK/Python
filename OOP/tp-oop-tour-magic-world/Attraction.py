from Common import CommonClass


class Attraction(CommonClass):
    def __init__(self):
        super().__init__()
        self.attraction: {
            'name': None,
            'cost': 0,
            'duration': 24.00,
            'cupo': 100,
            'type': None,
        }
        self.attractionByName = "SELECT nombre, costo, durasion, cupo, tipo FROM atracciones WHERE nombre = %s"
        self.attractionByCategoryType = "SELECT * FROM atracciones WHERE atracciones.tipo = %s ORDER BY tipo DESC"

    def getAttractionByName(self, name):
        response_attraction = self.connectionDB.sendQuery(
            self.attractionByName, (name))
        for result in response_attraction:
            return result

    def getAttractionByCategoryType(self, category_type):
        response_attraction = self.connectionDB.sendQuery(
            self.attractionByCategoryType, (category_type))
        return response_attraction


# atr = Attraction()
# print(atr.getAttractionByName('Hogsmeade'))

# print(atr.getAttractionByCategoryType('DEGUSTACION'))
