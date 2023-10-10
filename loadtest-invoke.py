import boto3
import time

def lambda_handler(event, context):
    # Initialize Lambda client
    client = boto3.client('lambda')

    for _ in range(500):
        client.invoke(
            FunctionName='loadTest-1',
            InvocationType='Event'  # Use 'Event' for asynchronous execution
        )
  

    return {
        'statusCode': 200,
        'body': 'Invoked 1000 instances of the API Calling Lambda'
    }
