
_MAX_SUGGESTIONS = 10

class _Node:
    def __init__(self, data):
        self.data = data
        self.end_of_word = False
        self.child = {}

class SearchSuggestion:
    def __init__(self):
        self.root = _Node(None)

    def insert(self, word: str) -> None:
        """Given a word will be stored in trie data structure

        Args:
            word (str): Word to store
        """
        word = word.strip()
        curr = self.root
        while word:
            if word[0] not in curr.child:
                curr.child[word[0]] = _Node(word[0])
            curr = curr.child[word[0]]
            word = word[1:]
            if len(word) is 0:
                curr.end_of_word = True

    def batch_insert(self, words: [str]) -> None:
        """Given a list of words will be stored in trie data structure

        Args:
            words ([str]): List of words to store
        """
        for word in words:
            self.insert(word)

    def search(self, word: str, max_suggestions=_MAX_SUGGESTIONS) -> [str]:
        """Given a prefix, will search for words starting with the prefix

        Args:
            word (str): Prefix to search by.
            max_suggestions (int, optional): Number of suggestions in the result. Defaults to 10.

        Returns:
            [str]: List of words with the given prefix
        """
        result = []
        curr = self.root
        og_word = word

        while word:
            if word[0] not in curr.child:
                return result
            curr = curr.child[word[0]]
            word = word[1:]

        if curr.end_of_word:
            result.append(og_word)

        def _search_helper(self, word: str, node: _Node) -> [str]:
            """Recursive function to search trie

            Args:
                word (str): Current word
                node (_Node): Current node

            Returns:
                [str]: List of words with the given prefix
            """
            if len(result) >= max_suggestions:
                return result
            for child_node in node.child.values():
                if child_node.end_of_word and len(result) < max_suggestions:
                    result.append(word + child_node.data)
                _search_helper(self, word + child_node.data, child_node)
            return result
        return _search_helper(self, og_word, curr)
