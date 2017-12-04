from sqlalchemy import create_engine
import pandas as pd
import numpy as np
# Uncomment to see all rows and columns in pythons shell output
#pd.options.display.max_rows = 999
#pd.options.display.max_columns = 9

def Main():
    engine = create_engine("mysql+mysqldb://root:root@localhost/anomalydb?charset=utf8mb4")
    df = pd.read_sql("main", engine)
    # Calculating standart deviation for each row
    sigma = df.groupby(['api_name', 'http_method'])['count_http_code_5xx'].transform(np.std)
    # In case count instanse > 3, is_anomaly takes the value 1, else 0
    df['is_anomaly'] = np.where(df['count_http_code_5xx'] > 3*sigma, '1', '0')
    # Rewritting db table main
    df.to_sql(name='main', con=engine, if_exists='replace', index = False, chunksize=4)

if __name__ == '__main__':
    Main()
