import unittest
from /translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):

    def test_english_to_french_null_input(self):
        result = english_to_french(None)
        self.assertIsNone(result)

    def test_french_to_english_null_input(self):
        result = french_to_english(None)
        self.assertIsNone(result)

    def test_english_to_french_translation_hello(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_french_to_english_translation_bonjour(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

    def test_english_to_french_translation_empty_string(self):
        result = english_to_french('')
        self.assertEqual(result, '')

    def test_french_to_english_translation_empty_string(self):
        result = french_to_english('')
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
