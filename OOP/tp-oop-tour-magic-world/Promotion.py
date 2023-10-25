from Common import CommonClass


class Promotion(CommonClass):
    def __init__(self):
        super().__init__()
        self.promotion: {
            'code': None,
            'name': None,
            'category': None,
            'atractions_one': None,
            'atractions_two': None,
            'atractions_three': None,
            'discount': 100,
        }
        self.TYPE_DISCOUNT = ["Abs", "AxB", "Por"]
        self.promotionById = "SELECT tipo, nombre, categoria, atraccion_1, atraccion_2, atraccion_n, descuento FROM promociones WHERE id = %s"
        self.promotionByCategory = "SELECT * FROM promociones WHERE promociones.categoria = %s ORDER BY categoria DESC"

    def getPromotionByCatergory(self, category):
        response_promotion = self.connectionDB.sendQuery(
            self.promotionByCategory, (category))
        return response_promotion

    def getPromotionById(self, id_promotio):
        response_promotion = self.connectionDB.sendQuery(
            self.promotionById, (id_promotio))
        for result in response_promotion:
            return result

    def createNewPromotion(self, code, name, category, atractions_one, atractions_two, atractions_three, discount):
        if code is not None and name is not None and category is not None and discount is not None:
            self.promotion["code"] = code
            self.promotion["name"] = name
            self.promotion["category"] = category
            self.promotion["atractions_one"] = atractions_one
            self.promotion["atractions_two"] = atractions_two
            self.promotion["atractions_three"] = atractions_three
            self.promotion["discount"] = discount

            super().connectionDB.addNewPromotion(self.promotion)
        else:
            print(
                "Promotion not created. Please code, name, category and discount are required")

    def promotionModify(self, id_Promotion, code, name, category, atractions_one, atractions_two, atractions_three, discount):
        if id_oldPromotion is not None and code is not None and name is not None and category is not None and discount is not None:
            self.promotion["code"] = code
            self.promotion["name"] = name
            self.promotion["category"] = category
            self.promotion["atractions_one"] = atractions_one
            self.promotion["atractions_two"] = atractions_two
            self.promotion["atractions_three"] = atractions_three
            self.promotion["discount"] = discount

            super().connectionDB.upDatePromotion(id_Promotion, self.promotion)
        else:
            print(
                "Promotion not modify. Please id, code, name, category and discount are required")

    def discount(self, mount, code_discount, value_discount):
        if code_discount == self.TYPE_DISCOUNT[1]:
            return (0 * mount)
        elif code_discount == self.TYPE_DISCOUNT[0]:
            return (mount - value_discount)
        else:
            return round(mount * (value_discount/100), 2)


# pro = Promotion()
# print(pro.getPromotionById(5))

# print(pro.getPromotionByCatergory('DEGUSTACION'))
