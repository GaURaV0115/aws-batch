import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # Specify your bucket name  
    bucket_name = 'your-bucket-name'
    
    # List objects in the specified bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    # Check if the bucket is empty
    if 'Contents' not in response:
        return "No files found in the bucket."
    
    # Extract the latest file based on the LastModified timestamp
    latest_file = max(response['Contents'], key=lambda x: x['LastModified'])
    
    # Get the file key (name)
    latest_file_key = latest_file['Key']
    
    # Retrieve the latest file's content
    latest_file_obj = s3_client.get_object(Bucket=bucket_name, Key=latest_file_key)
    
    # Read the content of the file (assuming it's an Excel file)
    file_content = latest_file_obj['Body'].read()
    
    # Here you can perform your evaluation on file_content
    # For example, you could use pandas to read and process the Excel data
    
    return {
        'latest_file_key': latest_file_key,
        'file_content': file_content.decode('utf-8')  # Adjust based on your needs
    }