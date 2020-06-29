# Search Suggestion

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/search-suggestion)
![PyPI](https://img.shields.io/pypi/v/search-suggestion)
![PyPI - License](https://img.shields.io/pypi/l/search-suggestion)

## ℹ️ Overview
Build a search suggestion system with millions of search terms with ultrafast query speed. Search Suggestion utilizes comples trie data structures in the background to manage large datasets without compromising speed.

## 🏗️ Install
To install Search Suggestion, simply use pip:
```
pip install search-suggestion
```

## 🏁 Quick Start 
```python
from search_suggestion import SearchSuggestion

ss = SearchSuggestion()

ss.insert('cat')

ss.batch_insert(['car', 'dog'])

result = ss.search('c')
print(result)
> ['cat', 'car']
```

The number of search results defaults to 10, an optional `max_suggestions` can be provided to override this value.
```python
result = ss.search('c', max_suggestions=20)
```

## 💭 Feature Suggestion
If you have any requests, please feel free to submit a [ticket](https://github.com/5tigerjelly/search-suggestion-python/issues/new). I will try to prioritize based on available time.