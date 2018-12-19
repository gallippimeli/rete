class Constants:
    @staticmethod
    def getConstant(key, value):
        dicc = {}
        diccEnfermedades = {"0": "Dengue", "1": "Zica", "2": "Chikunguña"}
        dicc["Enfermedades"] = diccEnfermedades
        return dicc[key][value]

    @staticmethod
    def hasKey(key):
        return  key in ["Enfermedades"]