# Search Suggestion

## ℹ️ Overview
Build a search suggestion system with millions of search terms with ultrafast query speed. Search Suggestion utilizes comples trie data structures in the background to manage large datasets without compromising speed.

## 🏗️ Installation
```
pip install search-suggestion
```

## 🏁 Quick Start 
```python
from search_suggestion import SearchSuggestion

ss = SearchSuggestion()

ss.insert('cat')

ss.batch_insert(['car', 'dog'])

ss.search('c')
> ['car', 'cat']
```

The number of search results defaults to 10, an optional `max_suggestions` can be provided to override this value.
```python
ss.search('c', max_suggestions=20)
```