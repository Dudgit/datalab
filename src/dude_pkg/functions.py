from pandas import merge
import pandas as pd
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

def pre_network(table,gdata):
    gdata = pd.merge(gdata,table.loc[:,["stop_id","route_id"]],left_index=True,right_on="stop_id")
    nameDict = gdata.loc[:,["stop_id","stop_name"]].set_index("stop_id").to_dict()["stop_name"]
    table["stop_name"]= table.stop_id.map(lambda x:nameDict[x])
    source = []
    target = []
    for e1, e2 in zip(table.loc[0:len(table)-1,["stop_sequence","stop_name"]].values,table.loc[1:,["stop_sequence","stop_name"]].values):
        if e1[0] < e2[0]:
            source.append(e1[1])
            target.append(e2[1])

    df = pd.DataFrame(pd.Series(source),columns=["source"])
    df["target"] = target
    df = pd.merge(df,gdata.groupby("stop_name").first(),left_on="source",right_index=True)
    df = df.groupby(["source","target","route_id"]).first().reset_index()
    return df