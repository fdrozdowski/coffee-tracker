class CoffeeWeightToStatusTranslator:

    MAX_COFFEE_MAKER_WEIGHT = 200
    MIN_COFFEE_MAKER_WEIGHT = 100

    SLOPE = 100.0 / (MAX_COFFEE_MAKER_WEIGHT - MIN_COFFEE_MAKER_WEIGHT)
    YINTERCEPT = - MIN_COFFEE_MAKER_WEIGHT * SLOPE

    def __init__(self): pass

    def translate(self, weight):

        if weight > self.MAX_COFFEE_MAKER_WEIGHT:
            weight = self.MAX_COFFEE_MAKER_WEIGHT

        if weight < self.MIN_COFFEE_MAKER_WEIGHT:
            weight = self.MIN_COFFEE_MAKER_WEIGHT

        return self.SLOPE * weight + self.YINTERCEPT

