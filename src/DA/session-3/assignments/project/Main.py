
from preprocessing import Check_data_type,Drop_unnecessary_features,Read_data_file
from Config.config import FILE_PATH,COLS_TO_DROP

if __name__=="__main__":
    df=Read_data_file(file_path=FILE_PATH)
    print("\nOriginal Dataframe: \n",df)
    Drop_unnecessary_features(df,COLS_TO_DROP)
    print("DataFrame after drop unnecessary_columns : \n",df)
    print("Datatype and num of unique values DataFrame : \n",Check_data_type(df))
    