import unittest
from unittest.mock import patch
import translator 

class TestTranslatorMethods(unittest.TestCase):
    def test_french_to_english_null(self):
        with self.assertRaises(ValueError):
            translator.french_to_english(None)
    
    def test_english_to_french_null(self):
        with self.assertRaises(ValueError):
            translator.english_to_french(None)

    @patch('translator.english_to_french')
    def test_hello_to_bonjour(self, mock_translate):
        mock_translate.return_value = 'Bonjour'
        result = translator.english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')
        
    @patch('translator.french_to_english')
    def test_bonjour_to_hello(self, mock_translate):
        mock_translate.return_value = 'Hello'
        result = translator.french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

if __name__ == '__main__':
    unittest.main()
