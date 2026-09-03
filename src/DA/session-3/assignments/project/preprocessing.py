import pandas as pd
from pathlib import Path



def Read_data_file(file_path:str)->pd.DataFrame:
    '''
    read csv file and return a panda DataFrame
    Args:
        file_path: (str) file path of csv file
    Returns:
        return panda DataFrame of Csv file you send it's path
    '''
    # CHECK THAT FILE_PATH IS A STRING
    if not isinstance(file_path,str):
        raise TypeError("file_path must be string")
    try:
        file_path=Path(file_path)

        # CHECK THE PATH POINT TO FILE
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        return pd.read_csv(file_path)

    except PermissionError:
        raise("File exists but cannot be read")
    except OSError:
        raise("File cannot be opened")



def Drop_unnecessary_features(df:pd.DataFrame,cols_to_drop:list[str])->pd.DataFrame:
    '''
    remove unnecessary columns from DataFrame
    Args:
        df: pandas DataFrame you want to remove unnecessary columns from it
        cols_to_drop: list of unnecessary columns name 
    Returns:
        return panda DataFrame after dropping unnecessary columns from it
    '''

    if not isinstance(df,pd.DataFrame) :
        raise TypeError("df should by DataFrame")

    if not (isinstance(col,str)  for col in cols_to_drop) :
        raise TypeError("columns you want to dorp should be string ")

    if  not set(cols_to_drop).issubset(df.columns):
        raise ValueError("one or more column in cols_to_drop doesn't exist in df")
    
    df.drop(columns=cols_to_drop , inplace=True)
    return df


def Check_data_type(df:pd.DataFrame)->pd.DataFrame:
    '''
    check datatypes columns inside df (panda DataFrame)
    Args:
        df: panda DataFrame you want to check it's columns datatype
    Returns:
        return: panda DataFrame contain each column (inside df) name , datatype and number of unique values on it
    '''

    if not isinstance(df,pd.DataFrame):
        raise TypeError("df should be DataFrame Object")
    return pd.DataFrame({ "Datatype":df.dtypes.values , "NumofUniqueValues":df.nunique().values}).T