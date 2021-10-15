import pandas as pd
import boto3


def get_fish_dataframes():
    s3_client = boto3.client('s3')  # Establishes a variable containing boto3 containing to amazon s3
    bucket_name = 'data-eng-resources'  # Name of the bucket we're in

    # Gets the objects in the bucket that ends its name with the Key
    s3_pandas_object = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-mon.csv')
    # Using pandas to read the csv file into a dataframe
    # 'Body' is there because technically it is the only key, and everything is its value
    df_mon = pd.read_csv(s3_pandas_object['Body'])

    s3_pandas_object = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market-tues.csv')
    df_tues = pd.read_csv(s3_pandas_object['Body'])

    s3_pandas_object = s3_client.get_object(Bucket=bucket_name, Key='python/fish-market.csv')
    df_idk = pd.read_csv(s3_pandas_object['Body'])

    # Returning the 3 dataframes, 1 for each file
    return df_mon, df_tues, df_idk
