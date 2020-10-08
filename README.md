# Python-Snippets
Helpful snippets to work with Python

## Motivation
These are snippets of code I frequently use in my day-to-day work and figured might be helpful to others.

## What are these snippets?
These snippets are helpful tools that I've developed to aid my own workflow. I'll try to include some use cases wherever needed/possible.

## Snippets
### [Clipboard2Dict.py](https://github.com/datagy/Python-Snippets/blob/master/ClipboardToDict.py)
This snippet takes your clipboard (from a tabular format (e.g., Excel)) and turns it into a dictionary. The resulting dictionary is returned to your clipboard.

For example, this table:
| col1 | col2 |
|------|------|
| a    | 1    |
| b    | 2    |

Then running `clipboard2dict()` would add the following dictionary: `{'a':1, 'b':2}` to your clipboard.

### [Dummy_Data.py](https://github.com/datagy/Python-Snippets/blob/master/dummy_data.py)
This snippet relies on the product method from itertools, which generates a dot product of all possible combinations of multiple lists. The product is then applied to a dataframe. 

For example:
```
countries = ['Germany', 'Canada', 'USA']
years = [2018, 2019, 2020]
type = ['A', 'B', 'C']

print(dummy_dataframe(['Country', 'Year', 'Type'], countries, years, type))
```

|    | Country   |   Year |
|---:|:----------|-------:|
|  0 | Germany   |   2018 |
|  1 | Germany   |   2019 |
|  2 | Germany   |   2020 |
|  3 | Canada    |   2018 |
|  4 | Canada    |   2019 |
|  5 | Canada    |   2020 |
|  6 | USA       |   2018 |
|  7 | USA       |   2019 |
|  8 | USA       |   2020 |

