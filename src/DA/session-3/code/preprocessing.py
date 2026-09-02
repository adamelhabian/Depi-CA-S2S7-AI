
import pandas as pd 


def drop_cols(df:pd.DataFrame,cols:list[str])->pd.DataFrame:
   '''
   Drop specific cols from dataframe
   Args:

   Returns:
   
   '''
   return df.drop(columns=cols).head()



def get_data_info(df):
    return pd.DataFrame({"data type" : df.dtypes, "num unique values":df.nunique()}).T


def nul_info(df:pd.DataFrame)->pd.DataFrame:
    return pd.DataFrame({"null":df.isnull().sum() , "ratio":(df.isnull().sum()/df.shape[0])*100}) 