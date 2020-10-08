from itertools import product

def dummy_dataframe(columns, *args):
    """Generates a dataframe shell of all possible combinations available in the cross-section of multiple lists.

    Args:
        columns (list): column headers to use

    Returns:
        dataframe: dataframe of all combinations of the cross-section of multiple lists
    """
    
    list_of_data = list(product(*args))
    return pd.DataFrame(list_of_data, columns=columns)
