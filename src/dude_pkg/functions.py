from pandas import merge
from pandas.core.frame import DataFrame
import networkx as nx

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

def create_network_data(table,snames): # -> pd.DataFrame
    """
    Description:  
    ------------  

    Creates and cleares the dataFrame for further use  

    Args:  
    -----  
    - table: pandas DataFrame, containing the informaiton  

    - snames: pandas DataFrame, read from stops.txt  
    """

    tmp = snames.loc[:,["stop_id","stop_name","stop_lat","stop_lon"]]
    tmp.set_index("stop_id", inplace=True)
    mynodes = table.stop_id.value_counts()
    gdata = merge(tmp,mynodes,left_index=True,right_index=True)
    gdata.rename({"stop_id":"stop_count"},inplace=True,axis=1)

    return gdata

def create_graph(pos): # -> networkx.classes.graph.Graph
    """
    Description:  
    ------------  

    Creates a network object for visualization  

    Args:  
    -----  

    - pos: dictionary, containing the names and the positions for visualization

    """
    G = nx.Graph()
    G.add_nodes_from(pos.keys())
    for n, p in pos.items():
        G.nodes[n]['pos'] = p
    return G