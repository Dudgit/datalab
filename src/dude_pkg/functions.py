from pandas import merge
features = ["trip_id","route_id","stop_sequence","stop_id",
#"arrival_time","departure_time"
"direction_id"
]
def stop_id_calculator(df):
    df.sort_values("stop_sequence",inplace = True)
    return df.stop_id

def mgm(df1,df2): # -> pd.Dataframe
    """
    Description:  
    ------------  

    My merge function. Merge 2 dataframes as pandas merge.

    Args:  
    ----  
    - df1: pandas DataFrame, trips or stop_times  
    - df2: pandas DataFrame, trips or stop_times (different from df1)  

    Return:  
    ------  

    Merged dataframe with specific features.  

    
    """
    tmp = merge(df1,df2,on = "trip_id")
    return tmp.loc[:,features] 