def stop_id_calculator(df):
    df.sort_values("stop_sequence",inplace = True)
    return df.stop_id

# Might not need, cause of valuceounts
#def route_parser(df):
#    
#    for ri in  df.route_id.unique():
#    