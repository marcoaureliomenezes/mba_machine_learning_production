

class WeightSensor:

    __weight: float

    def __init__(self):
        self.__weight = 0

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight