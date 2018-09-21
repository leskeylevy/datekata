import unittest
from app.models import Language
Language = Language

class LanguageTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_languages = Language('python')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_languages,Language))
