import unittest

from weight_translator import CoffeeWeightToStatusTranslator


class TestWeightTranslator(unittest.TestCase):

    translator = CoffeeWeightToStatusTranslator()
    max_weight = translator.MAX_COFFEE_MAKER_WEIGHT
    min_weight = translator.MIN_COFFEE_MAKER_WEIGHT
    diff = max_weight - min_weight

    def test_translator(self):
        self.assertEqual(self.translator.translate(self.min_weight - self.diff), 0)
        self.assertEqual(self.translator.translate(self.min_weight - 0.5 * self.diff), 0)
        self.assertEqual(self.translator.translate(self.min_weight), 0)
        self.assertEqual(self.translator.translate(self.min_weight + 0.1 * self.diff), 10)
        self.assertEqual(self.translator.translate(self.min_weight + 0.25 * self.diff), 25)
        self.assertEqual(self.translator.translate(self.max_weight), 100)
        self.assertEqual(self.translator.translate(self.max_weight + 0.5 * self.diff), 100)
        self.assertEqual(self.translator.translate(self.max_weight + self.diff), 100)

if __name__ == '__main__':
    unittest.main()