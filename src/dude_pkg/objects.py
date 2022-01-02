import pandas as pd

features = ["trip_id","route_id","stop_sequence","stop_id",
#"arrival_time","departure_time"
"direction_id"
]

PATH = "../data/"
rp, stp , sp ,tp = ("routes","stop_times","stops","trips")

routes = pd.read_csv(f"{PATH}{rp}.txt")
stop_times = pd.read_csv(f"{PATH}{stp}.txt")
stops = pd.read_csv(f"{PATH}{sp}.txt")
trips = pd.read_csv(f"{PATH}{tp}.txt")

table = pd.merge(trips,stop_times,on = "trip_id").loc[:,features] 