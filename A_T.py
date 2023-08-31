import pytest
import requests

from APIFunctions import *
from A_F import *


# A test function to check the DictionaryAPI functionality
class TestAPI:

    @pytest.fixture()
    def url(self):
        return "https://api.dictionaryapi.dev/api/v2/entries/en/"

    @pytest.mark.parametrize('word',[("apple"), ("aple"), ("elpa"), ("aaple"), ("aapplleee")])
    def test1_Valid_Word_Lookup(self,url,word):
           actual = Valid_Word_Lookup(url, word)
           assert actual, 'do not suport in word lookup'



    @pytest.mark.parametrize("word", ["supercalifragilisticexpialidocious"])
    def test_case_sensitivity(self, url, word):
         definitions = validate_long_word(url, word)
         print(definitions)

    @pytest.mark.parametrize("word", ["Hello"])
    def test_case_sensitivity(self, url, word):
        actual = validate_case_insensitivity(url, word)
        assert actual, "API is case sensitive"
