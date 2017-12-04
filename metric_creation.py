import csv
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
# Creating db connection

def Main():
    engine = create_engine("mysql+mysqldb://root:root@localhost/anomalydb?charset=utf8mb4")

    df = pd.read_csv('raw_data.csv', sep=',', parse_dates=True)
    # Setting index for time indexing
    df = df.set_index(['ts'])
    df.index = pd.to_datetime(df.index, format = '%Y-%m-%d %H:%M:%S')
    # Creating new table with api*mtd pairs for cases when the cod is an error.
    # Counting number of errors for each pair for each 15 mins
    two = df[df.cod >= 500].groupby(['api_name', 'mtd']).resample('15min').size()
    # Changing GroupBy type to DataFrame type
    two = two.reset_index()
    # Creating new column labels
    two.columns=['api_name', 'http_method', 'timeframe_start', 'count_http_code_5xx']
    # Rearraging column labels
    two.reindex(['timeframe_start','api_name', 'http_method', 'count_http_code_5xx'], axis=1)

    # Database output
    two.to_sql(name='main', con=engine, if_exists='append', index = False, chunksize=4)

if __name__ == '__main__':
    Main()

