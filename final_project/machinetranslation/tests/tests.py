import unittest
from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(translator.english_to_french('hello'), 'bonjour')
        # test when 'Bye' is given as input the output is not 'random'.
        self.assertNotEqual(translator.english_to_french('Bye'), 'random')

class Test_french_to_english(unittest.TestCase):
    def test1(self):
        # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        # test when 'Bonheur' is given as input the output is not 'Sad'.
        self.assertNotEqual(translator.french_to_english('Bonheur'), 'Sad')

unittest.main()
