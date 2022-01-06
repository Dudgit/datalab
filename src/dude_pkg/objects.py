import pandas as pd
features = [
            #"trip_id",
            "route_id",
            "stop_sequence",
            "stop_id",
            #"arrival_time","departure_time"
            "direction_id"
            ]

PATH = "../data/"
rp, stp , sp ,tp = ("routes","stop_times","stops","trips")

table = pd.merge( 
                pd.read_csv(f"{PATH}{tp}.txt", low_memory=False)  ,
                pd.read_csv(f"{PATH}{stp}.txt", low_memory=False) ,
                on = "trip_id"
                ).loc[:,features]