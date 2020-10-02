def date_df(start_date, end_date=datetime.datetime.today(), intervals = 'D', column_name = 'Date'):
    """Generates a single column dataframe with continuous dates.

    Args: 
        start_date (str): enter date in 'YYYY-MM-DD' format. 
        end_date (str, optional): enter date in 'YYYY-MM-DD' format. Defaults to today.
        intervals (str, optional): Defaults to 'D'.
        column_name (str, optional): Name to give column. Defaults to 'Date'.
    
    Returns:
        dataframe (df): dataframe object
    """
    
    
    date_range = pd.date_range(
        start=start_date,
        end=end_date,
        freq=intervals)
    df = pd.DataFrame(date_range, columns=[f'{column_name}'])
    
    return df
