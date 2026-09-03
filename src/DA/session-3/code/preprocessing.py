
import pandas as pd 


def drop_cols(df:pd.DataFrame,cols:list[str])->pd.DataFrame:
   '''
   Drop specific cols from dataframe
   Args:
    df: DataFrame that you want to drop specific columns from it 
    cols: List of Columns name that you want to drop from dataframe

   Returns:
        return DataFrame after drop the specific columns 
   
   '''
   if not isinstance(df,pd.DataFrame):
        raise TypeError("df must be pandas DataFrame")
   
   if not isinstance(cols, list) or not all(isinstance(col, str) for col in cols):
    raise TypeError("cols must be a list of strings")

   if  not set(cols).issubset(df.columns):
       raise ValueError("One or more columns do not exist in the DataFrame")
    
   return df.drop(columns=cols)




def to_category(df:pd.DataFrame,cols:list[str])-> pd.DataFrame:
    '''
    Changing Data type of specific columns in dataframe to category 
    Args:
        df: Dataframe that you want to change data type of specific columns from it to category datatype
        cols: List of Columns name that you want to change there datatype  to category 
        
    Returns:
        return Dataframe with cols modified to category data type 
    '''
    if not isinstance(df,pd.DataFrame):
        raise TypeError("df must be pandas DataFrame")
    
    if not isinstance(cols, list) or not all(isinstance(col, str) for col in cols):
        raise TypeError("cols must be a list of strings")
    
    if  not set(cols).issubset(df.columns):
        raise ValueError("One or more columns do not exist in the DataFrame")

    for col in cols:
        if(df[col].dtype != 'category'):
            df[col]= df[col].astype('category')

    return df




def get_data_info(df):
    return pd.DataFrame({"data type" : df.dtypes, "num unique values":df.nunique()}).T


def null_info(df:pd.DataFrame)->pd.DataFrame:
    return pd.DataFrame({"null":df.isnull().sum() , 
                         "ratio": ((df.isnull().sum() / df.shape[0]) * 100).astype(float).round(2)}).T 