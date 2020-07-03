import unittest
from search_suggestion import SearchSuggestion

class TestSearchSuggestion(unittest.TestCase):

    def test_empty(self):
        s = SearchSuggestion()
        self.assertEqual(s.search('test'), [])
        self.assertEqual(s.search(''), [])

    def test_one_word(self):
        s = SearchSuggestion()
        s.insert("apple")
        self.assertEqual(s.search('a'), ["apple"])
        self.assertEqual(s.search('b'), [])

    def test_whitespace(self):
        s = SearchSuggestion()
        s.insert("apple")
        self.assertEqual(s.search('   a'), ["apple"])
        self.assertEqual(s.search('a   '), ["apple"])
        self.assertEqual(s.search(' a '), ["apple"])

    def test_batch_insert(self):
        s = SearchSuggestion()
        s.batch_insert(["apple", "grape", "banana"])
        self.assertEqual(s.search('a'), ["apple"])

    def test_empty_search_word(self):
        s = SearchSuggestion()
        s.batch_insert(["apple", "grape", "banana"])
        self.assertEqual(s.search(''), [])
        self.assertEqual(s.search('  '), [])

    def test_bad_search_word(self):
        s = SearchSuggestion()
        s.batch_insert(["apple", "grape", "banana"])
        self.assertEqual(s.search('c'), [])

    def test_search_multiple_words(self):
        s = SearchSuggestion()
        s.batch_insert(["apple", "app", "abs"])
        self.assertSetEqual(set(s.search('a')), {"apple", "app", "abs"})

if __name__ == '__main__':
    unittest.main()
