import io
import boto3


def upload_the_fish(df):
    s3_client = boto3.client('s3')
    bucket_name = 'data-eng-resources'

    # idk what this is but Danny has it
    str_buffer = io.StringIO()
    # Converting the dataframe to a csv, and the buffer is essential seemingly
    df.to_csv(str_buffer)

    # This uploads to the s3 bucket we're in , and names the file 'Matthew_fish.csv'
    # And puts it in the Data100 and fish folders
    s3_client.put_object(Body=str_buffer.getvalue(), Bucket=bucket_name, Key='Data100/fish/Matthew_fish.csv')
