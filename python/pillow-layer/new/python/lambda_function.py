import json
import boto3
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    # Define the destination bucket
    destination_bucket = 'pdestinationbuckeet'
    destination_key = 'resized-' + source_key
    
    # Get the image from the source bucket
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    image_content = response['Body'].read()
    
    # Resize the image
    image = Image.open(BytesIO(image_content))
    image = image.resize((100, 100))  # Resize to 100x100 pixels
    
    # Save the resized image to a BytesIO object
    buffer = BytesIO()
    image.save(buffer, 'JPEG')
    buffer.seek(0)
    
    # Upload the resized image to the destination bucket
    s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=buffer, ContentType='image/jpeg')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image resized and uploaded successfully')
    }
