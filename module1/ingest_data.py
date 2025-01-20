import pandas as pd
import argparse

import os
from time import time
from sqlalchemy import create_engine
import gzip
import shutil

def gunzip_file(file, output_file):
    with gzip.open(file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    url = params.url
    table_name = params.table_name
    
    csv_name = 'output.csv'
    # download the csv
    os.system(f"wget {url} -O {csv_name}.gz")
    gunzip_file(csv_name+".gz", csv_name)
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    
    df = next(df_iter)
    
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    df.head(n=0).to_sql(con=engine, name=table_name, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')
    
    while True:
        t_start = time()
        df = next(df_iter)
        
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()
        
        print('inserted another chunk..., took %.3f seconds' % (t_end - t_start))
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='user name for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table-name', help='name of the table where we will write the results')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    main(args)
