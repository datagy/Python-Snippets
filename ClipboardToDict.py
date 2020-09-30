import pandas as pd
from pandas.io.clipboard import copy

def clipboard2dict(key=0, value=1):
    """Returns a dictionary based on clipboard contents. For example, copy a range in Excel as input. 
    The resulting dictionary will be a key:value pair of two columns in the range.
    
    Args:
        key (int, optional): Identify the index position for the column to be used as the key. Defaults to 0.
        value (int, optional): Identify the index position for the column to be used as the value. Defaults to 1.

    Returns:
        dictionary: dictionary representation of range in clipboard.
    """
    
    df = pd.read_clipboard()
    dictionary = dict(zip(df.iloc[:, key], df.iloc[:, value]))
    copy(str(dictionary))
