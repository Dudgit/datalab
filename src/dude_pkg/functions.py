from pandas import merge
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib
from pandas.core.frame import DataFrame

features = ["trip_id","route_id","stop_sequence","stop_id",
#"arrival_time","departure_time"
"direction_id"
]
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

def pre_network(table,gdata): # -> pd.Dataframe
    """
    Description:  
    ------------  

    Create the data, which will be used during the creation of the graph  

    Args:  
    -----  

    - table, pandas DataFrame , created from stop_names.txt  
    - gdata, pandas DataFrame, created from create_network_data function  

    Returns:  
    --------  

    pandas DataFrame, which will be added to the networkx graph object creator
    """
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

def create_draw_params(gdata,table,G,PATH,rp): # -> dict, dict
    """
    Description:  
    ------------  
    Creatie node specific description  
    Since the Graph groups the nodes, but the DataFrame does not  
    It could've been done via DataFrame.groupby() method, but it was safer  

    Args:  
    -----  

    - table, pandas DataFrame , created from stop_names.txt  
    - gdata, pandas DataFrame, created from create_network_data function  
    - G2, networkx Graph Object
    - PATH, string, path to data Folder
    - rp, string, route path

    returns:  
    ------------  
    
    dict of positions , dict of colors
    """

    tmp = pd.merge(pd.read_csv(f"{PATH}{rp}.txt").loc[:,["route_color","route_id"]],table,on="route_id")
    colordict = {"009FE3":"cyan","FFD800":"yellow","E41F18":"red","005CA5":"blue","4CA22F":"dark green"}
    change_color = lambda x : matplotlib.colors.hex2color(f"#{x}")
    tmp.route_color = tmp.route_color.map(change_color)
    posdict = gdata.loc[:,["stop_name","stop_count"]].set_index("stop_name").to_dict()["stop_count"]
    colordict = tmp.loc[:,["stop_name","route_color"]].set_index("stop_name").to_dict()["route_color"]
    return np.array([posdict[n] for n in G.nodes]), [colordict[n] for n in G.nodes]