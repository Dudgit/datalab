import sqlite3
import pandas as pd
rp, stp , sp ,tp = ("routes","stop_times","stops","trips")

def createSQL(table_name, df, conn = None):
    if conn == None:
        conn = sqlite3.connect('../../data/homework_data.db')
    df.to_sql(f'{table_name}', conn, if_exists='replace', index = False)

def main():
    routes = pd.read_csv(f"{rp}.txt",low_memory=False)
    createSQL("routes",routes)

    stops = pd.read_csv(f"{sp}.txt",low_memory=False)
    createSQL(sp,stops)

    stop_times = pd.read_csv(f"{stp}.txt",low_memory=False)
    createSQL(stp,stop_times)

    trips = pd.read_csv(f"{tp}.txt",low_memory=False)
    createSQL(tp,trips)

if __name__ == '__main__':
    main()


