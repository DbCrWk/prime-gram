# get necessary components to run the tester
import unittest
from anagram import anagram

# define the anagram test class for unit testing
class AnagramTest( unittest.TestCase ):
    # check if it works with just one word
    def test_one_word(self):
        test_output = anagram(['search'])
        known_output = [['arches', 'eschar', 'recash', 'chaser']]
        self.assertEqual( test_output, known_output )

    # check if it works with a list of words
    def test_word_list(self):
        test_output = anagram(['search','eschar'])
        known_output = [
            ['arches', 'eschar', 'recash', 'chaser'],
            ['arches', 'search', 'recash', 'chaser']
        ]
        self.assertEqual( test_output, known_output )

    # check where this is no anagram for a word
    def test_no_anagram(self):
        test_output = anagram(['intractable'])
        known_output = [[]]
        self.assertEqual( test_output, known_output )

    # check where there is no word passed
    def test_empty_word(self):
        test_output = anagram([''])
        known_output = [[]]
        self.assertEqual( test_output, known_output )

    # check where the word is invalid in some way
    def test_invalid_word(self):
        test_output = anagram(['?'])
        known_output = [[]]
        self.assertEqual( test_output, known_output )

# actually perform unit testing
unittest.main()
